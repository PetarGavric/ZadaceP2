n = 15

def parni_brojevi(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def neparni_brojevi(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

print("Parni brojevi:")
for broj in parni_brojevi(n):
    print(broj)

print("\nNeparni brojevi:")
for broj in neparni_brojevi(n):
    print(broj)
