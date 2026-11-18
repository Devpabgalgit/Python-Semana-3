# TICKET 3 — Inventario de bodega (DistriPura)
# Todo en este archivo, con funciones. Las funciones DEVUELVEN valores: no usan input() ni print().

# Inventario inicial: un diccionario donde la clave es el código del producto.
#agregar_producto(inventario, clavenueva, productonuevo, pesonuevo, stocknuevo, minimonuevo, precionuevo)


def agregar_producto(inventario, codigo, nombre, peso, stock, minimo, precio):
    if codigo in inventario:
        print("La clave para el producto ya está siendo utilizada, debe utilizar otra.")
        return False

    inventario[codigo] = {
        "clave": codigo,
        "Producto": nombre,
        "Peso": peso,
        "Stock": stock,
        "minimo": minimo,
        "precio": precio,
    }
    print("Se ha agregado el producto nuevo al inventario.")
    return True
               



def buscar_producto(inventario, codigo):
    if codigo in inventario:
        return inventario[codigo]
    return None
        


def productos_bajo_minimo(inventario):
    
    lista = []
    for codigo, datos in inventario.items():
        if datos["Stock"] < datos["minimo"]:
            lista.append(codigo)
    return lista


def valor_total_inventario(inventario):
    total = 0
    for datos in inventario.values():
        total += datos["precio"] * datos["Stock"]
    return float(total)


def encontrar_duplicados(lista_codigos):
    conteo = {}
    for codigo in lista_codigos:
        conteo[codigo] = conteo.get(codigo, 0) + 1

    duplicados = {}
    for codigo, veces in conteo.items():
        if veces > 1:
            duplicados[codigo] = veces

    return duplicados



inventario = {"P001":{"clave": "P001","Producto": "Arroz","Peso": "1kg","Stock": 120,"minimo": 50,"precio": 1150},
               "P002":{"clave": "P002","Producto": "Frijoles","Peso": "1kg","Stock": 35,"minimo": 40,"precio": 1450},
               "P003":{"clave" : "P003","Producto" : "Aceite","Peso" : "1L","Stock" : 18,"minimo" : 20,"precio" : 2300},
               "P004":{"clave" : "P004","Producto" : "Azucar","Peso" : "2kg","Stock" : 90,"minimo" : 30,"precio" : 1900},
               "P005":{"clave" : "P005","Producto" : "Jabon de Barra","Peso" : "","Stock" : 12,"minimo" : 25,"precio" : 650}
               }


rep = True


while rep==True:


  
    print("\n========== MENU PRINCIPAL ==========")
    print("1) Agregar producto")
    print("2) Buscar producto")
    print("3) Productos con stock menor al minimo")
    print("4) Sumar el stock total de un producto")
    print("5) Consultar claves de producto duplicadas")
    print("6) Salir de la Appicacion")
    print("====================================")

    menu = int(input("Seleccione una opcion: "))

    if menu==1:
        clavenueva=input("Ingrese la clave del producto nuevo: ")
        productonuevo=input("Ingrese el nombre del producto nuevo: ")
        pesonuevo=input("Ingrese el peso del producto nuevo: ")
        stocknuevo=int(input("Ingrese el stock del producto nuevo: "))
        minimonuevo=int(input("Ingrese el stock minimo del producto nuevo: "))
        precionuevo=float(input("Ingrese el precio del producto nuevo: "))
        agregar_producto(inventario, clavenueva, productonuevo, pesonuevo, stocknuevo, minimonuevo, precionuevo)
    elif menu==2:
         clavebuscador = input("Ingrese la clave del producto que quiere buscar: ")
         producto = buscar_producto(inventario, clavebuscador)

         if producto is None:
            print("No se encontró ningún producto con esa clave.")
         else:
            print("La información del producto es la siguiente:")
            for campo, valor in producto.items():
                print(f"  {campo}: {valor}")
    elif menu==3:
      bajos = productos_bajo_minimo(inventario)

      if len(bajos) > 0:
        print("Productos con stock menor al mínimo:", bajos)
      else:
        print("No se encontraron productos con stock menor al mínimo.")
    elif menu==4:
        total= valor_total_inventario(inventario)
        print(f"El valor total del stock actual es {total} colones")
    elif menu == 5:
        num_de_claves = int(input("¿Cuántas claves desea ingresar? "))
        lista_claves = []
        for i in range(num_de_claves):
           clave = input(f"Ingrese la clave número {i+1}: ")
           lista_claves.append(clave)

        duplicados = encontrar_duplicados(lista_claves)

        if duplicados:
            print("¡Atención! Se encontraron claves duplicadas:")
            for clave, veces in duplicados.items():
                print(f"  Clave: {clave} - aparece {veces} veces.")
        else:
            print("Excelente: no se encontraron claves duplicadas.")
    elif menu==6:
                print("\n==================================")
                print("Gracias por Usar la applicacion, Hasta Luego!")
                print("====================================")
                rep=False
    else:
        cont=int(input("Ingreso una opcion invalida, quiere volver a intentar?: 1) Si 2) No. "))
        if cont==1:
            rep=True
        else:
            print("Gracias por Usar la applicacion, Hasta Luego! ")
            rep=False

       
    