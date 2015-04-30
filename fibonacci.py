# fibonacci hausaufgabe

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()
for i in gen:
    print(i)
    if i > 10e3: break
