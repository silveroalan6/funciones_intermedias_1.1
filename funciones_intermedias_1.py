# -------------------------
# 1. ACTUALIZAR VALORES
# -------------------------

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431


# -------------------------
# 2. ITERAR DICCIONARIO
# -------------------------

def iterarDiccionario(lista):
    for dic in lista:
        texto = ""
        for clave in dic:
            texto += f"{clave} - {dic[clave]}, "
        print(texto)


# -------------------------
# 3. ITERAR DICCIONARIO 2
# -------------------------

def iterarDiccionario2(llave, lista):
    for dic in lista:
        print(dic[llave])


# -------------------------
# 4. IMPRIMIR INFORMACION
# -------------------------

def imprimirInformacion(diccionario):
    for clave in diccionario:
        lista = diccionario[clave]
        print(len(lista), clave.upper())
        for item in lista:
            print(item)
        print()  # espacio


# -------------------------
# PRUEBAS (para ver que funciona)
# -------------------------

print("---- EJERCICIO 2 ----")
cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes2)

print("\n---- EJERCICIO 3 ----")
iterarDiccionario2("nombre", cantantes2)

print("\n---- EJERCICIO 4 ----")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)