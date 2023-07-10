class vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 4
    
class coche(vehiculo):
    velocidad = "160 km"
    cilindrada = 1.3
    
automovil = coche()
print("el automovil es de color", automovil.color)
print("el automovil tiene", automovil.ruedas, "puertas")
print("el automovil va a una velocidad de", automovil.velocidad)