test1= "Colombia"
test2= "Argentina"

#print(test1)
lista = [test2, test1, "Oso"]

#print(lista[1], "vs", lista[0])

def test():
    return test1

#print(test())

#print(len("diegognzalez"))


tupla1 = ("Python", "Django")

#print(tupla1[1])

#print(sum([1,2,4]))#Autosuma

#print(sorted([1,9,3,8,15,7]))#Ordena

car = "Taxi"
"""
if (car == "Taxi"):
    print(car)
elif(car == "OSO"):
    print("No es un Taxi")

"""

product = ["Papas", 19000]

if(product[0] == "pollo"):
    print(product[0])
    if(product[1] >= 18000):
        print("Tiene Promocion del 5%", ":", product[1]-((product[1]*5)/100))
    else:
        print("No Tiene Promocion")
elif(product[0] == "Papas"):
    print("Protucto sin Descuento")
else:
    print("El Producto no se encuentra en la lista")


"""for i in range(4):
    print(i)"""

x=1
while x <= 10:
    print(x)
    x +=1








