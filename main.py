# "Цикл for. Элементы списка. Полезные функции в цикле", модуль 2_4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
n = len(numbers)
k = 0  # количество делителей
for i in [numbers]:
    for i in range(2, n+1):   # число 1 не является ни простым, ни составным числом
        for j in range(2, i//2 + 1):
            if i %  j == 0:  # проверяем делится ли число без остатка
                k = k + 1
        if k == 0:            # если количество делителей 0, то проверяемое число - простое
            primes.append(i)  # вносим его в список primes
        else:
            k = 0
            not_primes.append(i)  # вносим число в список not_primes
    break
print(primes)
print(not_primes)