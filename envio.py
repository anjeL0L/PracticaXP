def calcular_costo_envio(monto):
    if monto < 500:
        return 100
    elif monto <= 999.99:
        return 50
    else:
        return 0


monto = float(input("Ingresa el monto de la compra: "))
costo_envio = calcular_costo_envio(monto)

print(f"El costo de envío es: ${costo_envio}")