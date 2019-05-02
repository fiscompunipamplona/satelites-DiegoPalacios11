print("altura dado un periodo")
G=6.67e-11
m=5.97e24
r=6371000
pi=3.1416
t=float(input("ingrese el periodo"))
h=(((G*m*t**2)/3*pi**2)**1/3)-r
print("el valor de la altura es: ",h)
print("altura en tiempos determinados")
dia1=86400
nomin=5400
cuamin=2700
h1=(((G*m*dia1**2)/3*pi**2)**1/3)-r
h2=(((G*m*nomin**2)/3*pi**2)**1/3)-r
h3=(((G*m*cuamin**2)/3*pi**2)**1/3)-r
print("la altura para 24 horas es: ",h1)
print("la altura para 90 min es: ",h2)
print("la altura para 45 min es: ",h3)
print("altura de un dia geosincronico")
g=86.148
hg=(((G*m*g**2)/3*pi**2)**1/3)-r
dia2=h1-hg
print("la diferencia de altura es:",dia2)
