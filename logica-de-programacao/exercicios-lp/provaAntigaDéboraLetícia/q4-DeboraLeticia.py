n = int(input(""))

contador = 0

for i in range(1,n+1):
    if n % i == 0:
        contador = contador + 1
print(contador)
