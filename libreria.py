import cmath
import random

#Generar numeros aleatorios
def numeroRandom(coeficientes):
    nRandom = 0
    a = abs(coeficientes[0])
    #Tengo la hipotesis de que el termino independinte puede ser un indice para generar los numeros aleatorios
    #por default me gustaria crear un numero cercano a 0
    #caso base (termino idependiente es 0)
    if(a == 0):
        nRandom = random.randint(-20,20)
        return nRandom
    
    nRandom = random.randint(-a, a)
    return nRandom

#generar numeros complejos aleatorios
def numeroRandomComplex(coeficientes):
    return 0

#metodo de derivadas
def deriv(grado, coeficientes):
    return [coeficientes[i] * i for i in range(1, grado + 1)]

#metodo de horner (numeros reales)
def horner(grado, coeficientes, xi):
   pX = coeficientes[grado]
   i = grado - 1
   while(i >= 0):
       pX = coeficientes[i] + (pX * xi)
       i = i - 1
   return pX

#Obtener el valor de la raiz (complejas)
def newtonRapshonComplex(grado, coeficientes, derivada, c):
    #Tolerancia
    rootAprox = 0 
    error = 1
    vAnterior = 0
    tolerancia = 0.5*pow(10,2-c)
    
    #Valores de prueba (Modificar a random)
    print ("introduce el valor inicial de prueba")
    xi = complex(input())
    i = 0
    
    if((horner(grado-1, derivada, xi)) == 0):
            print("Horner es 0, ingresa otro el valor: ")
            xi = float(input())
            
    while (abs(error) >= tolerancia):  
        
        rootAprox = xi-(horner(grado, coeficientes, xi)/horner(grado-1, derivada, xi))
        #si raiz == 0
        if(rootAprox == 0):
            print("La raiz es 0")
            break;
        
        error = ((rootAprox - vAnterior)/rootAprox) * 100
        print(f"la aproximacion de la raiz numero   {i}  es :   {rootAprox}  con error   {error}")
        vAnterior = rootAprox
        # El valor que se acaba de obtener es la i-ésima aproximación actual. Una vez obtenida, se toma como el valor xi y se vuelve a meter al polinomio. 
        xi = rootAprox 
        i = i + 1     
    print ("La raiz es: " , rootAprox)
    return rootAprox

# Obtener el valor actual x_(i+1)
def newtonRapshon(grado, coeficientes, derivada, c):
    #Tolerancia
    rootAprox = 0 
    error = 1
    vAnterior = 0
    tolerancia = 0.5*pow(10,2-c)
    
    #Valores de prueba (Modificar a random)
    xi = numeroRandom(coeficientes)
    i = 0
    print(grado - 1)
    if((horner(grado - 1, derivada, xi)) == 0):
            print("Horner es 0, ingresa otro el valor: ")
            xi = float(input())
            
    while (abs(error) >= tolerancia):  
        
        rootAprox = xi-(horner(grado, coeficientes, xi)/horner(grado-1, derivada, xi))
        #si raiz == 0
        if(rootAprox == 0):
            print("La raiz es 0")
            break;
        
        error = ((rootAprox - vAnterior)/rootAprox) * 100
        print(f"la aproximacion de la raiz numero   {i}  es :   {rootAprox}  con error   {error}")
        vAnterior = rootAprox
        # El valor que se acaba de obtener es la i-ésima aproximación actual. Una vez obtenida, se toma como el valor xi y se vuelve a meter al polinomio. 
        xi = rootAprox 
        i = i + 1     
    print ("La raiz es: " , rootAprox)
    return rootAprox        

#raices reales del polinomio
def raices(grado, coeficientes, derivada, c = 6):
    j = 1
    nRaices = grado
    raiz = 0
    raices = []
    
    if(coeficientes[0] == 0):
        raices.append(0);
        nRaices = nRaices - 1;
        
    while(j <= nRaices ):
        raiz = newtonRapshon(grado, coeficientes, derivada, c)
        #prevencion de ciclado por no encontrar otra raiz
        exit = 0
        while(raiz in raices and (exit < 10)):
            raiz = newtonRapshon(grado, coeficientes, derivada, c)
            exit += 1
        raices.append(raiz)    
        j = j + 1
    return raices

#raices complejas del polinomio
def raicesComplex(grado, coeficientes, derivada, c = 6):
    j = 1
    nRaices = grado
    raices = []
    
    if(coeficientes[0] == 0):
        raices.append(0);
        nRaices = nRaices - 1;
        
    while(j <= nRaices ):
        raices.append(newtonRapshonComplex(grado, coeficientes, derivada, c))
        j = j + 1
    return raices

#puntos criticos (raices de la segunda derivada)       
def puntosCriticos(grado, derivada, c = 6):
    secondDev = []
    pCriticos = []
    gradoDev = grado - 1
    print("Grado de la derivada")
    print(gradoDev)
    secondDev = deriv(gradoDev, derivada)
    print("Primera derivada")
    print(derivada)
    print("Segunda derivada")
    print(secondDev)
    
    pCriticos = raices(gradoDev, derivada, secondDev, c)
    return pCriticos
       
def maxMin(grado, coeficientes, derivada, c):
    pCriticos = puntosCriticos(grado, derivada, c)
    print(f"Puntos criticos: {pCriticos}")
    gradoDev = grado - 1
    i = 0 
    while(i <= (len(pCriticos)) - 1):
        penDeriv = horner(gradoDev, derivada, (pCriticos[int(i)] + 0.001))
        if(penDeriv < 0):
            y = horner(grado, coeficientes, pCriticos[int(i)])
            print(f"Maximo local en el punto: {pCriticos[int(i)]} , {y} ")
        elif(penDeriv > 0):
            y = horner(grado, coeficientes, pCriticos[int(i)])
            print(f"Minimo local en el punto: ({pCriticos[int(i)]} , {y}) ")
        else:
            print("Error :c")
        i = i + 1
        
def inflexion(grado, derivada, coeficientes):
    candidatosInflex = []
    puntosInflex = []
    gradoDevSec = grado - 2
    gradoDevTer = gradoDevSec - 1
    seconDev = deriv(gradoDevSec + 1, derivada)
    print(f"Segunda Derivada: {seconDev}")
    tercerDev = deriv(gradoDevTer + 1, seconDev)
    print(f"Tercera derivada: {tercerDev}")
    print(f"Grado segunda derivada: {gradoDevSec}")
    print(f"Grado tercera derivada: {gradoDevTer}")
    candidatosInflex = raices(gradoDevSec, seconDev, tercerDev)
    print(f"Candidatos de inflexión: {candidatosInflex}")
    i = 0
    while(i <= len(candidatosInflex) - 1):
        pruebaMen = 0
        pruebaMay = 0
        pruebaMen = horner(gradoDevSec, seconDev, (candidatosInflex[i] - 0.001))
        pruebaMay = horner(gradoDevSec, seconDev, (candidatosInflex[i] + 0.001))
        #prueba de inflexion
        if((pruebaMen < 0) and (pruebaMay > 0)):
            puntosInflex.append(candidatosInflex[i])
            y = horner(grado, coeficientes, candidatosInflex[int(i)])
            print(f"Puntos de inflexion: {candidatosInflex[int(i)]}, {y}")
        #aumento del ciclo
        i += 1 
