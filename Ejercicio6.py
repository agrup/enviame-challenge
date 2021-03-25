import random

def nexDistance():
    a = 0
    yield a
    a = 1
    yield a
    a = 1
    yield a
    a = 2
    b = 3
    while True:
        yield a
        a, b = b, a + b


def calcularDias(distancia):
    nueva_distancia = int(distancia/100)
    i=0
    rangos =  nexDistance()
    dias = 0
    for rango in rangos:
        if nueva_distancia == i:
            dias = rango
            rangos.close()
        i += 1
    return dias


for i in range(11):
    n = random.randint(0,1000)
    print('Para entregar un pedidio con distancia '+ str(n) + 'Km se necesitan '+ str(calcularDias(n)))