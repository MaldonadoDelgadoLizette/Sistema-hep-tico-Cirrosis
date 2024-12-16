"""
Modelado de Sistemas Fisiologicos
Beltrán Vega Sofía
Díaz Muruaga Carlos Manuel
Maldonado Delgado Lizette
Ingenieria Biomedica
Sistema Hepático

"""

#!pip install control
#!pip install slycot

import control
import numpy 
import matplotlib.pyplot as plt
import math

x0, t0, tF, dt = 0,0,30,1E-3
N = round ((tF-t0)/dt)+1 
t= numpy.linspace(t0,tF, N)  

#Funcion de tranferencia: Individuo saludable
R1 = 100
L = 1
C1 = 10E-6
R2 = 10
C2 = 100E-6

alpha3 = R2*L*C1*C2
alpha2 = L*C1 + L*C2 + R1*R2*C1*C2
alpha1 = R1*C1 + R2*C2 + R1*C2
alpha0 = 1
num=[alpha0]
den=[alpha3,alpha2,alpha1,alpha0]
sys=control.tf(num,den) #Funcion transferencia de control
print("Individuo sano(control): ")
print(sys)


########################################################

#Funcion de tranferencia: Individuo enfermo
R1 = 1E3
L = 2
C1 = 5E-6
R2 = 2E3
C2 = 50E-6

alpha3 = R2*L*C1*C2
alpha2 = L*C1 + L*C2 + R1*R2*C1*C2
alpha1 = R1*C1 + R2*C2 + R1*C2
alpha0 = 1
num=[alpha0]
den=[alpha3,alpha2,alpha1,alpha0]
sysE=control.tf(num,den) #Funcion transferencia del caso
print("Individuo enfermo (caso): ")
print(sysE)


#Controlador
Cr = 1E-6
Re = 4131.563867
Rr = 49917.55464
Ce = 1.3321E-6
numPID = [Re*Rr*Ce*Cr, Re*Ce+Rr*Cr, 1]
denPID = [Re*Cr, 0]
PID=control.tf(numPID,denPID)

#Sistema de control:Tratamiento
X=control.series(PID,sysE)
sysPID=control.feedback(X,1,sign=-1)
print("Sistema con tratamiento: ")
print(sysPID)


#Respiración normal
u=2.5*numpy.sin(math.pi*t) #Respiracion normal
a=1.5*numpy.sin(math.pi*t)
fig1=plt.figure()
ts, Vs = control.forced_response (sys,t,u,x0)
plt.plot (t, Vs, "-", color=[0, 1, 1], label = "$Vout(t):Control$") #Salida (lazo abierto)
ts, Ve = control.forced_response(sysE,t, a, x0)
plt.plot (t, Ve, "-", color=[0.75, 1, 0], label = "$Vout(t):Control$")
ts, pid = control.forced_response(sysPID,t, u, x0)
plt.plot (t, pid, ":", linewidth=4, color=[1, 0.5, 0], label = "$Vout(t):Tratamiento$")
plt.grid(False)
plt.xlim(0,20)
plt.ylim(-3,3)
plt.ylabel("$Concentración Plasmática(t)$")
plt.xlabel("$t$ [segundos]")
plt.title("Proceso Metabólico sano vs paciente enfermo")
plt.legend(bbox_to_anchor=(0.5,-0.23),loc="center",ncol=4)
plt.show ()
fig1.set_size_inches (10,4)
fig1.savefig("normal.png",dpi=600, bbox_inches="tight")
fig1.savefig("normal.pdf",dpi=600, bbox_inches="tight")




















