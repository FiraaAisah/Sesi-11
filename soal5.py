def factorial(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    return faktorial

n = 5
hasil = factorial(n)
print(hasil)
