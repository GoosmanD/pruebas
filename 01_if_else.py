# Tienes 5€ y vas a la tienda a por pan y leche, le preguntas al tendero cuanto vale para ver si lo puedes comprar.

dinero = 5

pan = int(input("¿Cuánto vale el pan?"))
leche = int(input("¿Cuánto vale la leche?"))

if (pan + leche) <= dinero:
    print("Compro el pan y la leche")
else:
    print("Me voy a casa a por mas dinero")

