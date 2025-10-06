# T(n) = 4T(n/2) + O(n^2)
# T(n) = 3T(n/3) + O(n)
# T(n) = 5T(n/2) + O(n log n)

import math

def metodo_maestro(a, b, f_exp):
    log_ab = math.log(a, b)
    print(f"a={a}, b={b}, f(n)={f_exp}")
    print(f"n^(log_b(a)) = n^{log_ab:.4f}")
    if "n^2" in f_exp and abs(log_ab - 2) < 0.01:
        print("Caso 2 → T(n)=Θ(n^2 log n)")
    elif "n" in f_exp and abs(log_ab - 1) < 0.01:
        print("Caso 2 → T(n)=Θ(n log n)")
    elif "n log n" in f_exp and log_ab > 1.5:
        print(f"Caso 1 → T(n)=Θ(n^{log_ab:.4f})")
    print("-" * 40)

if __name__ == "__main__":
    metodo_maestro(4, 2, "n^2")
    metodo_maestro(3, 3, "n")
    metodo_maestro(5, 2, "n log n")
