# fibonacci hausaufgabe

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a + b

gen = fibonacci()
for i in gen:
    print(i)
    if i > 10000: break
