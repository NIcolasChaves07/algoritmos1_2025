num = int(input("Informe um número"))
tabuaN = 1
result = None
for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")