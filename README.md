# numerical-methods
## Metodo Newton_Raphson
Para crear el metodo Neton_Raphson desarrollamos una clase tabla_Newton_Raphson:
```python

from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcularC import calcularC
from Errores.errorR_secante import errorR_secante

class tabla_Newton_Raphson:
    def tabla_Newton_Raphson(self):
          #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcularC()
        instance_errorR = errorR_secante()
        #variables de valores de tabla ( iniciales )
        x1 = 1
        i = 0
      
        print("i | x1 | f(x1) | f´(x1) | x1+1 | Error relativo")
        flag = True 
        while(flag):
         x11 =instance_calcularC.calcular_nuevo_valor_nw(x1)
         error = instance_errorR.errorR_secante(x11,x1)
       
         
         print("{} | {} | {} | {} |  {} | {}% | ".format(i, x1, instance_evaluar.evaluar_nw_derivada(x1,0),  instance_evaluar.evaluar_nw_derivada(x1,1),x11, error))
         x1 = x11
        
         if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
         i=i+1

```


Para calcular el valor  de x1+1 se uso:
```python
  def calcular_nuevo_valor_nw(self,x1):
       isinstancia_evaluar = evaluar()
       return x1-(isinstancia_evaluar.evaluar_nw_derivada(x1,0)/isinstancia_evaluar.evaluar_nw_derivada(x1,1))

```
implemente las siguientes para calcuular la derivada 
```python

    def  evaluar_nw_derivada(self,a,n):
        x,y = sp.symbols('x y')
        function = (x**2)-7
        d = sp.diff(function,x,n)
        derivada_evaluada = d.subs(x,a)
        return derivada_evaluada

```


