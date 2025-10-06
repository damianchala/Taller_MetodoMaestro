import pandas as pd
import re
import time

# ------------------------------------------------------------
# Cargar datos desde el archivo SQL (personas_desordenadas.sql)
# ------------------------------------------------------------
def cargar_personas(sql_file):
    """
    Lee un archivo .sql con instrucciones INSERT INTO y extrae los datos
    de las columnas: id, nombre, direccion, telefono, email, fecha_nacimiento.
    """
    with open(sql_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Buscar todos los grupos dentro de VALUES (...) usando re.DOTALL
    datos = re.findall(
        r"INSERT INTO personas.*?VALUES\s*\((.*?)\);",
        content,
        re.DOTALL | re.IGNORECASE
    )

    registros = []
    for d in datos:
        # Extraer valores respetando comas dentro de texto
        partes = re.findall(r"'(.*?)'|(\d+)", d)
        valores = []
        for texto, numero in partes:
            valor = texto if texto != "" else numero
            valores.append(valor.strip())

        # Asegurar 6 columnas
        if len(valores) == 6:
            registros.append(valores)

    # Crear DataFrame
    columnas = ["id", "nombre", "direccion", "telefono", "email", "fecha_nacimiento"]
    df = pd.DataFrame(registros, columns=columnas)

    # Limpiar espacios
    for c in columnas:
        df[c] = df[c].astype(str).str.strip()

    return df


# ------------------------------------------------------------
# Búsqueda con método Divide y Vencerás
# ------------------------------------------------------------
def busqueda_divide_y_venceras(df, letra):
    """
    Busca recursivamente las personas cuyo nombre comience con una letra dada.
    Complejidad teórica: T(n) = 2T(n/2) + O(n) = O(n log n)
    """
    if len(df) <= 1:
        if len(df) == 0:
            return df
        return df[df["nombre"].str.upper().str.startswith(letra.upper(), na=False)]

    mitad = len(df) // 2
    izq = df.iloc[:mitad]
    der = df.iloc[mitad:]

    resultado_izq = busqueda_divide_y_venceras(izq, letra)
    resultado_der = busqueda_divide_y_venceras(der, letra)

    return pd.concat([resultado_izq, resultado_der])


# ------------------------------------------------------------
# Mostrar resultados completos y ordenados
# ------------------------------------------------------------
def mostrar_resultados(df):
    """
    Muestra todas las columnas ordenadas y sin truncar en consola.
    """
    if df.empty:
        print("\n⚠️ No se encontraron resultados.")
        return

    # Ajustar pandas para mostrar todas las columnas
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 250)
    pd.set_option("display.colheader_justify", "center")
    pd.set_option("display.max_rows", 20)

    print("\n✅ Resultados encontrados (primeras 20 filas):\n")
    print(df[["id", "nombre", "direccion", "telefono", "email", "fecha_nacimiento"]].head(20).to_string(index=False))

    # Guardar resultados en CSV
    df.to_csv("resultados_busqueda.csv", index=False, encoding="utf-8-sig")
    print("\n📁 Resultados guardados en: resultados_busqueda.csv")


# ------------------------------------------------------------
# Prueba directa (opcional)
# ------------------------------------------------------------
if __name__ == "__main__":
    df = cargar_personas("personas_desordenadas.sql")
    print(f"✅ Total de registros cargados: {len(df)}")

    letra = input("\nBuscar personas cuyo nombre empiece por: ").upper()

    inicio = time.time()
    resultado = busqueda_divide_y_venceras(df, letra)
    fin = time.time()

    mostrar_resultados(resultado)

    print(f"\n⏱ Tiempo de búsqueda: {fin - inicio:.4f} segundos")
    print("📘 Complejidad teórica: T(n) = 2T(n/2) + O(n) = O(n log n)")
