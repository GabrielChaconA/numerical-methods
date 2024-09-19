# numerical-methods
## Menu
Se incorporó unua clase Menu para falicilar la navegación por el codigo
```python
class Menu:
    option = 1
    def menu(self):
       isinstance_biseccion =tabla_Biseccion()
       isinstance_Falsa_posicion=tabla_Falsa_posicion()
       instansce_Punto_fijo = tabla_Punto_Fijo()
       instance_Secante = tabla_Secante()
       instance_Raioes_multiples = tabla_raices_multiples()
       instance_ne = tabla_Neton_Raphson()
       flag = True


       while(flag):
        option = int(input("\nBIENVENIDO A MENU PRINCIPAL\nSelecciones el metodo: \n1.Biseccion \n2. Falsa posicion \n3.Punto fijo\n4.Secante \n5. Raices multiples\n6.Newton Raphson \n"))
        if option == 1 :
            isinstance_biseccion.tabla_de_valores_Biseccion()
        if option == 2:
            isinstance_Falsa_posicion.tabla_de_valores_Falsa_posicion() 
        if option ==3 :
           instansce_Punto_fijo.tabla_Punto_Fijo()
        if option ==4 :
           instance_Secante.tabla_Secante()
        if option == 5:
           instance_Raioes_multiples.tabla_raices_multiples()
        if option == 6:
           instance_ne.tabla_Neton_Raphson()
        option = input("deasea continuar(1.si 2.no)")
        if  option != "1":
           flag =False
```

## Errores 
Se estableció una calse para encontrar el valor relativo
```python
class errorR:
    #aqui se utilizan los valores de la funcion evaluada en c, el actual y anterior
    error_Tolerable = 0.005
    def errorR(self, x2,x11):
        return round(abs(((x2-x11)/x2)*100),4)
```

## Calcular
En la clase calcular nuevo valor, se encuuentran los métodos para desarrollas las nuevas variables con sus debidas condiciones
``` python
class calcular_Nuevo_Valor:
    
    # calcular c en metodo biseccion, falsa posicion
    def calcular_Biseccion(self,a ,b ):
            return (a+b)/2
    
    def calcular_Falsa_Posicion(self, a, b):

     instancia_evaluar = evaluar()  
     return (((a * instancia_evaluar.evaluar_Funcion(b)) - (b * instancia_evaluar.evaluar_Funcion(a))) / (instancia_evaluar.evaluar_Funcion(b) - instancia_evaluar.evaluar_Funcion(a)))

    def calcular_nuevo_valor(self,x1,x11,fx11,fx1):
      return  ( x11-fx11*((x11-(x1))/(fx11-(fx1))))
    
    def calcular_nuevo_valor_raices_multiples(self,x1):
     isinstancia_evaluar = evaluar()
     return x1-(( isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,0)*isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,1))/(((isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,1))**2)-(  isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,0)*isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,2)  )))
   
   
    
    def calcular_nuevo_valor_nw(self,x1):
       isinstancia_evaluar = evaluar()
       return x1-(isinstancia_evaluar.evaluar_nw_derivada(x1,0)/isinstancia_evaluar.evaluar_nw_derivada(x1,1))

    

```

## Evaluar
Se colocaron todas las funciones, en caso de requerir el metodo una derivada se le implemento con la libreria sympy
``` python
import sympy as sp
from sympy import cos, sin, log
import math
class evaluar:
    ##Aqui se desarrollan todas las funciones de los metodos
    def evaluar_Funcion(self, a):
        return (math.exp(2*a)) -3
    
    def evaluar_Funcion_PF(self, a):
        return ((math.exp(a))-4*a)
    
    def evaluar_Funcion_derivada(self,a):
        return(math.exp(a)*(1/4))
    
    def evaluar_Funcion_secante(self, a):
        return (a**2)-7
    
    def evaluar_Funcion_raices_derivada(self,a,n):
        x,y = sp.symbols('x y')
        function = x**3 - 5*x**2 + 7*x -3
        d = sp.diff(function,x,n)
        derivada_evaluada = d.subs(x,a)
        return derivada_evaluada
    

    def  evaluar_nw_derivada(self,a,n):
        x,y = sp.symbols('x y')
        function = (x**2)-7
        d = sp.diff(function,x,n)
        derivada_evaluada = d.subs(x,a)
        return derivada_evaluada



```

## Reduccion polonomial
Para el metodo de muller realice este metodo para la reuccin del polinomio
```python
class reduccion_polinomio: 
    def __init__(self):
        self.flag = False

    def reduccion_Coeficientes(self, funcion, raiz):
        coef = self.coeficientes(funcion)
        coef_reducidos = self.dividir_polinomio(coef, raiz)
        polinomio_resultante = self.convertir_a_funcion(coef_reducidos)
        return str(polinomio_resultante)  # Convertir la expresión a string

    def coeficientes(self, funcion):
        # Convertir el polinomio a una lista de coeficientes
        return [int(coef) for coef in sp.Poly(funcion).all_coeffs()]

    def dividir_polinomio(self, coeficientes, raiz):
        resultado = []
        acumulador = coeficientes[0]
        resultado.append(acumulador)

        for coef in coeficientes[1:]:
            acumulador = acumulador * raiz + coef
            resultado.append(acumulador)

        return resultado[:-1]  # El último valor es el residuo, que debe ser 0

    def convertir_a_funcion(self, coeficientes):
        x = sp.Symbol('x')
        polinomio = 0
        grado = len(coeficientes) - 1
        for i, coef in enumerate(coeficientes):
            polinomio += coef * x**(grado - i)
        return sp.simplify(polinomio)

```

### A continuacón se mostraran los métodos desarrollados para este proyecto 
## Metodo biseccíon
``` python
class tabla_Biseccion:
    """ Esta tabla contiene los valores y la ejecucion del metodo "Biseccion" """
    def tabla_de_valores_Biseccion(self):
    
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        a = 0
        b = 1
        c_Anterior = 0
        error = 0


     

        print("a | b | f(a)| f(b)| c | f(c) |Error relativo")
        flag = True 
        while(flag):
         #valores de la tabal, actualizables 
         c = instance_calcularC.calcular_Biseccion(a, b)
         fa = instance_evaluar.evaluar_Funcion(a)
         fb = instance_evaluar.evaluar_Funcion(b)
         fc = instance_evaluar.evaluar_Funcion(c) 
         if a !=0 :
            error = instance_errorR .errorR(c,c_Anterior)
            if error <= instance_errorR .error_Tolerable:
               print("fin ")
               break

         print("{} | {} | {} |  {}| {} | {} | {}| ".format(a,b, fa, fb, c , fc, error))
         if fa*fb == 0:
            print("Es la raziz")
            flag = False
         if  fa*fb < 0:
             if fa*fc == 0:
              print("Es la raziz")
              flag = False
              
             
             if  fa*fc < 0:
                b = c
  
                
             if  fa*fc >0:
                a =c
               
            
         if  fa*fb >0:
            print(" necesitas otro valor de a")
            flag = False

         c_Anterior = c

```

## Metodo falsa posición
``` python
class tabla_Falsa_posicion:

     def tabla_de_valores_Falsa_posicion(self):
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        a = 0
        b = 1
        c_Anterior = 0
        error = 0

        print("a | b | f(a)| f(b)| c | f(c) |Error relativo")
        flag = True 
        while(flag):
         #valores de la tabal, actualizables 
         c = instance_calcularC.calcular_Falsa_Posicion(a,b)
         fa = instance_evaluar.evaluar_Funcion(a)
         fb = instance_evaluar.evaluar_Funcion(b)
         fc = instance_evaluar.evaluar_Funcion(c) 
         if a !=0 :
            error = instance_errorR .errorR(c,c_Anterior)
            if error <= instance_errorR .error_Tolerable:
               print("fin ")
               break

         print("{} | {} | {} |  {}| {} | {} | {}| ".format(a,b, fa, fb, c , fc, error))
         if fa*fb == 0:
            print("Es la raziz")
            flag = False
         if  fa*fb < 0:
             if fa*fc == 0:
              print("Es la raziz")
              flag = False
              
             
             if  fa*fc < 0:
                b = c
  
                
             if  fa*fc >0:
                a =c
               
            
         if  fa*fb >0:
            print(" necesitas otro valor de a")
            flag = False

         c_Anterior = c
     

```

## Metodo Punto fijo
``` python
class tabla_Punto_Fijo :
    def tabla_Punto_Fijo(self):
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla( iniciales )
        x1 = 0
        i = 0
      
        print("i | x1 | f(x1)| x1 +1 | Error relativo")
        flag = True 
        while(flag):
         x2=instance_evaluar.evaluar_Funcion_derivada(x1)
         error = instance_errorR.errorR(x2,x1)
         
         print("{} | {} | {}     | {}      | {}% | ".format(i,x1, instance_evaluar.evaluar_Funcion_PF(x1), x2, error))
         x1=x2
         if error < instance_errorR.error_Tolerable:
               print("fin ")
               break
 
         i=i+1

```

## Metodo  secante
``` python
class tabla_Secante:
    def tabla_Secante(self):
        
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        x1 = 0
        x11= 1
        i = 0
      
        print("i | x1 | x1 +1 | f(x1) | f(x1+1)| x1+2 | Error relativo")
        flag = True 
        while(flag):
         x2 =instance_calcularC.calcular_nuevo_valor(x1,x11,instance_evaluar.evaluar_Funcion_secante(x11),instance_evaluar.evaluar_Funcion_secante(x1))
         error = instance_errorR.errorR(x2,x11)
       
         
         print("{} | {} | {} | {} |  {} | {} | {}% | ".format(i, x1, x11, instance_evaluar.evaluar_Funcion_secante(x1),instance_evaluar.evaluar_Funcion_secante(x11),x2, error))
         x1 = x11
         x11 = x2
        
        
         if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
         i=i+1
```

## Metodo newton Raphson
``` python
class tabla_Neton_Raphson:
    def tabla_Neton_Raphson(self):
          #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        x1 = 1
        i = 0
      
        print("i | x1 | f(x1) | f´(x1) | x1+1 | Error relativo")
        flag = True 
        if instance_evaluar.evaluar_nw_derivada(x1,0) == 0:
            print(instance_evaluar.evaluar_nw_derivada(x1,0)+ " es la raiz")
        else:
         while(flag):
          x11 =instance_calcularC.calcular_nuevo_valor_nw(x1)
          error = instance_errorR.errorR(x11,x1)
       
         
          print("{} | {} | {} | {} |  {} | {}% | ".format(i, x1, instance_evaluar.evaluar_nw_derivada(x1,0),  instance_evaluar.evaluar_nw_derivada(x1,1),x11, error))
          x1 = x11
        
          if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
          i=i+1

```

## Raices multiples
``` python
class tabla_raices_multiples:
    def tabla_raices_multiples(self):
          #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        x1 = 0
        i = 0
      
        print("i | x1 | f(x1) | f´(x1) | f´´(x1)| x1+1 | Error relativo")
        flag = True 
        while(flag):
         x11 =instance_calcularC.calcular_nuevo_valor_raices_multiples(x1)
         error = instance_errorR.errorR(x11,x1)
         print("{} | {} | {} | {} |  {} | {} | {}% | ".format(i, x1, instance_evaluar.evaluar_Funcion_raices_derivada(x1,0), instance_evaluar.evaluar_Funcion_raices_derivada(x1,1),instance_evaluar.evaluar_Funcion_raices_derivada(x1,2),x11, error))
         x1 = x11
        
        
         if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
         i=i+1
```

## Muller
```python
class tabla_muller:

    def tabla_muller(self):
        
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        instance_reduccion = reduccion_polinomio()
        flag = True 
        x = sp.symbols('x')
        function = sp.sympify(x**4 - 13*x**2 + 36)
        x0 = 0
        x1 = 1
        x2=2
        
        while(True):   
        
         fx0 =  instance_evaluar.evaluar_muller(x0,0,function)
         fx1 = instance_evaluar.evaluar_muller(x1,0,function)
         fx2 = instance_evaluar.evaluar_muller(x2,0,function)
         h0 = instance_calcularC.calcular_h(x1,x0)
         h1 = instance_calcularC.calcular_h(x2,x1)
         s0 = instance_calcularC.calcular_s(fx1,fx0,h0)
         s1 = instance_calcularC.calcular_s(fx2, fx1,h1)
         a= instance_calcularC.variable_a(s1,s0, h1,h0)
         b= instance_calcularC.variable_b(a,h1,s1)
         c = fx2
         x3 = instance_calcularC.variable_x3(x2,c,b,a)
         error = instance_errorR.errorR(x3,x2)
         print(" x0    |    x1    |    x2    |    f(x0)   |     f(x1)   |     f(x2)   |     h0    |     h1   |     s0    |     s1    |     a    |     b    |    c    |  x3  |Error relativo    ")
         print("{}     |     {}     |      {}     |     {}     |     {}     |    {}     |     {}     |     {}     |     {}     |     {}     |    {}   |    {}    |    {}   |   {}    |     {}   % | ".format
                 (x0, x1, x2,fx0 ,fx1, fx2 , h0, h1,s0, s1,a,b,c,x3, error))
           
         x0 = x1
         x1= x2 
         x2=x3
         if fx0==0 or fx1==0 or fx2==0:
           print("Se requiere una reducciion de polinomio")
           function = instance_reduccion.reduccion_Coeficientes(function,2)
           x0 = 0
           x1 = 1
           x2=2
          
           
           
        
           if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
           





```