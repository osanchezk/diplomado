import numpy as np # Importamos numpy como el alias np
 
import scipy as sp# Importamos scipy como el alias sp
 
from scipy.optimize import fminbound # Importamos fmindbound desde scipy.optimize&amp;amp;nbsp;&amp;amp;nbsp;&amp;amp;nbsp; 
 
import matplotlib.pyplot as plt 
 
#definimos la funcion
 
def mi_funcion(x, a, b, c, d):
 
 y = -sp.cos(a*sp.pi*x/b) + c*x**d
 
 return y
 
 
 
# Definimos los coeficientes a, b, c, d
 
a = 2
 
b = 0.5
 
c = 0.05
 
d = 2
 
# Definimos el intervalo de busqueda del minimo
 
x1 = 0.2
 
x2 = 0.6
 
xt=sp.arange(0,1,.01)
 
yt = -np.cos(a*sp.pi*xt/b) + c*xt**d
 
# Calculamos del minimo local de la funcion entre x1 y x2 
 
x_minimo = fminbound(mi_funcion,x1,x2, args = (a,b,c,d))
 
ysol = mi_funcion(x_minimo, a, b, c, d)
 
# Presentamos la grafica y en pantalla el resultado
 
print (u'El minimo esta en x = %2.3f, y = %2.3f' %(x_minimo, ysol))
 
plt.plot(xt,yt)
 
plt.plot(x_minimo,ysol,'x')