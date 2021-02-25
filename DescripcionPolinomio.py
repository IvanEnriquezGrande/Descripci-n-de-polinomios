from libreria import *

#listas de las funciones
grado = 0
coeficientes = []
derivada = []
roots = []
pInflex = []

i = 0

#cifras significativas
c = 6
	
#introduce el grado del polinomio
print ("introduce el grado del polinomio")
grado = int(input())

# Una vez conocido el grado del polinomio, pedimos los (grado+1) coeficientes:
while (i <= grado):
    print ("introduce el coeficiente a_ ",i)
    coeficientes.append(float(input()))
    i += 1
    
#polinomio
print ("los coeficientes del polinomio son:")
print (coeficientes)

#derivada
derivada = deriv(grado, coeficientes)
print ("La derivada es:")
print (derivada)

#encontrar raices
roots = raicesComplex(grado, coeficientes, derivada, c)
print(f"Las raices son: {roots}")

#maximos y minimos de la función
maxMin(grado, coeficientes, derivada, c)

#puntos de inflexion
inflexion(grado, derivada, coeficientes)

