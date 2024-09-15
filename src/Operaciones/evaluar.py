import sympy as sp
from sympy import cos, sin, log
import math
class evaluar:
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
    
    def evaluar_Funcion_raices(self,x):
        return round(x**3 - 5*x**2 + 7*x -3,4)
    

    def  evaluar_nw_derivada(self,a,n):
        x,y = sp.symbols('x y')
        function = (x**2)-7
        d = sp.diff(function,x,n)
        derivada_evaluada = d.subs(x,a)
        return derivada_evaluada



        
