import math
def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))

def fibonacci():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

fibo = fibonacci()

for x in fibo:
    if len(divisors(x)) > 1000:
        print('El primer numero con mas de 1000 divisores es: '+str(x))
        fibo.close()