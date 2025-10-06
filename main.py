from recurrencias import metodo_maestro
from algoritmos import merge_sort, quick_sort, binary_search
from personas_busqueda import busqueda_divide_y_venceras, cargar_personas

import random

def menu():
    print("\n=== Taller Método Maestro ===")
    print("1. Resolver recurrencias")
    print("2. Ejecutar algoritmos (MergeSort / QuickSort / Búsqueda Binaria)")
    print("3. Analizar búsqueda en base de datos")
    print("4. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        print("\n📘 Resolviendo recurrencias con Método Maestro:\n")
        metodo_maestro(4, 2, "n^2")
        metodo_maestro(3, 3, "n")
        metodo_maestro(5, 2, "n log n")

    elif opcion == "2":
        print("\n⚙️ Ejecutando algoritmos...\n")
        datos = [random.randint(1, 1000) for _ in range(30)]

        print("Datos originales:", datos[:10])
        print("\nMerge Sort:", merge_sort(datos.copy())[:10])
        print("Quick Sort:", quick_sort(datos.copy())[:10])

        datos_ordenados = sorted(datos)
        objetivo = datos_ordenados[10]
        indice = binary_search(datos_ordenados, objetivo)
        print(f"Búsqueda Binaria: valor {objetivo} encontrado en índice {indice}")

    elif opcion == "3":
        print("\n📊 Análisis sobre base de datos personas:\n")
        df = cargar_personas("personas_desordenadas.sql")
        print("Total de registros cargados:", len(df))

        letra = input("Buscar personas cuyo nombre empiece por: ").upper()
        resultado = busqueda_divide_y_venceras(df, letra)

        print(f"\nPersonas encontradas: {len(resultado)}")
        print("Ejemplo de resultados:")
        print(resultado.head())
        print("\nComplejidad teórica: T(n) = 2T(n/2) + O(n) → O(n log n)")
   
    elif opcion == "4":
        print("\n👋 Saliendo del programa... ¡Hasta luego!")
        return False

    else:
        print("\n⚠️ Opción no válida. Intenta nuevamente.")
    
    return True


def main():
    continuar = True
    while continuar:
        menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()
