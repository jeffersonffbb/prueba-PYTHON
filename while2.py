print("Precios de las entradas para la sala de juego:")
print("Niños menores de 4 años entran gratis")
print("Ninos entre 4 años y 18 años pagan 4$")
print("Niños mayores de 18 años pagan 10$")

año=int(input("ingrese su edad porfavor:"))
if año<4:
    print("usted ingresa gratis...")
elif año>=4 and año<=18:
    print("usted debe pagar 4$...")
elif año>18 :
    print("usted debe pagar 10$...")
else:
    print("ingrese una edad correcta")