import time
print("Contagem regressiva de 10 segundos:")

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

    print("Fogo!")