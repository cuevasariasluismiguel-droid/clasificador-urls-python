
D_w = (input("Ingrese una direccion web:"))

if D_w.startswith("https://"): 
    print("La direccion web inicia con https://") 
else:
    print("La direccion web no inicia con https://")   

if D_w.endswith(".com"):
    print("Dominio comercial")
    
elif D_w.endswith(".edu"):
    print("Dominino educativo")

elif D_w.endswith(".org"):
    print("Dominio de organizacion") 

else:
    print("Dominio no reconocido")        
