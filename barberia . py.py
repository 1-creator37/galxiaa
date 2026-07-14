# --- SISTEMA DE CONTROL DE PEDIDOS: BARBERÍA ---

# 1. Definimos los precios de cada cosa (Nuestras cajas de precios)
precios = {
    "1": ("Corte de cabello", 10.00),
    "2": ("Peinado con estilo", 6.00),
    "3": ("Gel premium", 4.00),
    "4": ("Barba completa", 8.00)
}

# Cajas para guardar lo que el cliente elija
carrito = []
total_pagar = 0.0

print("=========================================")
print("   💈 BIENVENIDO A LA BARBERÍA REINA 💈  ")
print("=========================================")
print("Selecciona los servicios que deseas (Escribe el número):")

# 2. Bucle para que el cliente elija todo lo que quiera
while True:
    print("\n--- NUESTRO MENÚ ---")
    for llave, datos in precios.items():
        print(f"[{llave}] {datos[0]} ...... ${datos[1]:.2f}")
    print("[0] Terminar pedido y ver total")
    
    opcion = input("\n¿Qué deseas agregar? (0 para finalizar): ")
    
    if opcion == "0":
        break  # Rompe el bucle y va a la cuenta final
    
    elif opcion in precios:
        servicio_elegido = precios[opcion][0]
        precio_elegido = precios[opcion][1]
        
        # Agregamos al carrito y sumamos al total
        carrito.append(servicio_elegido)
        total_pagar += precio_elegido
        print(f"✅ ¡Agregado! {servicio_elegido} (${precio_elegido:.2f})")
        print(f"Total acumulado actual: ${total_pagar:.2f}")
    else:
        print("❌ Opción no válida, intenta de nuevo.")

# 3. Pantalla final de la cuenta y el anticipo
print("\n=========================================")
print("          RESUMEN DE TU PEDIDO           ")
print("=========================================")

if total_pagar == 0:
    print("No seleccionaste ningún servicio. ¡Vuelve pronto!")
else:
    print("Servicios contratados:")
    for item in carrito:
        print(f" -> {item}")
    
    print("-----------------------------------------")
    print(f"💰 TOTAL DE LOS SERVICIOS: ${total_pagar:.2f}")
    
    # Calculamos el anticipo (por ejemplo, el 20% para asegurar la cita)
    anticipo = total_pagar * 0.20
    print(f"💳 ANTICIPO PARA RESERVAR (20%): ${anticipo:.2f}")
    print(f"💵 Saldo restante a pagar en caja: ${total_pagar - anticipo:.2f}")
    print("=========================================")
    print("¡Gracias por confiar en nosotros! Te esperamos.")
