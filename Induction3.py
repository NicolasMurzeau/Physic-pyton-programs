#Programme TP3 Méca Murzeau Nicolas
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#importation des données
e_i=np.array([1.2396694214876,
7.53275109170306,
13.6363636363636,
19.1798941798942,
25.297619047619,
32.1428571428571,
38.5496183206107,
45.4927536231884,
56.1576354679803,
64.3646408839779
])
f=np.array([200.45,
1203.5,
2098.5,
2998.5,
3894.5,
5000.0,
5997.0,
7493.5,
8691.0,
9990.0

])


#Incertitudes
f_incertitude=np.array([0.015,
1.5,
6.5,
4.5,
11.5,
25,
9,
14.5,
25,
30
])
e_i_incertitude=np.array([0.0103305785123967
0.0328941095707557
0.184862983906046
0.233756053861874
0
0.388726919339164
0.294271895577181
0.648498214660786
0.769249435802859
0.631848844662861

])


#Tracer les points expérimentaux
plt.scatter(f,e_i ,label="Donnée expérimentale")
plt.errorbar(f,e_i,xerr=f_incertitude,yerr=e_i_incertitude, fmt='+')

#Definition de notre fonction
def func(x,m):
   return m*x
popt1, cov1 = curve_fit(func, f,e_i)


#Régression linéaire
plt.plot(f,func(f,*popt1),label="pente={:.3f}".format(popt1[0]))

print("pente1 = ", popt1[0])

#mise en page
plt.title("|e|/|i| en fonction de la fréquence", fontname="sans-serif", fontweight='bold', fontsize=17)
plt.ylabel("|e|/|i| (V/A)", fontweight='bold',fontsize=14)
plt.xlabel("Fréquence (Hz)", fontweight='bold',fontsize=14)
plt.text(10, 45, "Bobine de 1000 spires ", fontsize=14)
plt.legend(fontsize = 15)
plt.grid()
plt.tight_layout()
fig = plt.gcf()
fig.set_size_inches(9, 6)
plt.show()
