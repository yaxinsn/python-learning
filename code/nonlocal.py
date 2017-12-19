

def createCounter():
    n = 0

    def counter():
        nonlocal n
        n += 1
        return n

    return counter



fa=createCounter();

print(fa());
print(fa());
print(fa());
print(fa());
print(fa());
print(fa());
