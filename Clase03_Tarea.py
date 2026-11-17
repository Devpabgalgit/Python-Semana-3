'''

CÓMO ENTREGAR
1. Sube tu código a GitHub (repositorio público).
2. Abre el chat del Tutor, escribe "Entrega Clase 3" y adjunta con el clip los archivos que se piden.
3. En el mismo mensaje pega, como texto (si ayuda, puedes adjuntar también capturas de pantalla):
   - La salida de los 5 casos de prueba.
   - El enlace a tu repositorio y la salida de: git log --oneline -3
   - Tu respuesta a: ¿por qué guardaste el inventario en un diccionario y no en una lista?
4. Nunca pegues contraseñas ni tokens reales: si los necesitas mostrar, enmascáralos (abc...).
Puedes entregar tantas veces como quieras: con 7 o más ganas el badge de la clase.


'''

P001={
"clave" : "P001",
"Producto" : "Arroz",
"Peso" : "1kg",
"Stock" : 120,
"minimo" : 50,
"precio" : 1150
}

P002={
"clave" : "P002",    
"Producto" : "Frijoles",
"Peso" : "1kg",
"Stock" : 35,
"minimo" : 40,
"precio" : 1450
}
P003={
"clave" : "P003",
"Producto" : "Aceite",
"Peso" : "1L",
"Stock" : 18,
"minimo" : 20,
"precio" : 2300
}
P004={
"clave" : "P004",
"Producto" : "Azucar",
"Peso" : "2kg",
"Stock" : 90,
"minimo" : 30,
"precio" : 1900
}
P005={
"clave" : "P005",
"Producto" : "Jabon de Barra",
"Peso" : "",
"Stock" : 12,
"minimo" : 25,
"precio" : 650
}

inventario = [P001,P002,P003,P004,P005]


def agregar_producto(clave, producto, peso, stock, minimo, precio):

   
 for i in inventario:
   if i["clave"] == clave:
      print("La clave ya existe debe utilizar otra")
      return
         
 clavenueva={
 "clave": clave,
 "Producto": producto,
 "Peso": peso,
 "Stock": stock,
 "minimo": minimo,
 "precio": precio
       } 
 inventario.append(clavenueva)
 print("Se ha agregado el producto nuevo al inventario. ")
      #contador==False



def buscar_producto(clave):
   for i in inventario:
      if i["clave"] == clave:
         print("La informaciòn de Producto es la siguiente: ", i)
         return  
   print("No se encontro ninguna producto")
      


def productos_bajo_minimo():
  
   listaproductosminimo=[]

   for i in inventario:
      if i["Stock"] < i["minimo"]:   
         listaproductosminimo.append(i["clave"])
         

   
   if len(listaproductosminimo) > 0:
      print("Lista de claves de productos con stock menor al minimo: ", listaproductosminimo)
   else:
      print("No se encontraron productos con stock menor al minimo.")



def valor_total_inventario(clave):

    for i in inventario:
        if i["clave"] == clave:

            valor_total = int(i["precio"] * i["Stock"])

            print("El valor total del stock para el producto", clave, "es:", valor_total)

            return valor_total

    print("No se encontro ningun producto con esa clave.")
    return 0
  




def encontrar_duplicados(lista_claves):

    duplicados = {}

    for clave in lista_claves:

        contador = 0

        for producto in inventario:

            if clave == producto["clave"]:
                contador = contador + 1

        if contador > 1:
            duplicados[clave] = contador

    if duplicados:
        print("¡Atencion! Se encontraron claves duplicadas:")

        for clave in duplicados:
            print("Clave:", clave, "- Aparece en", duplicados[clave], "productos.")

    else:
        print("Excelente: No se encontraron claves duplicadas.")

    return duplicados






rep = True


while rep==True:


  
   print("\n========== MENU PRINCIPAL ==========")
   print("1) Agregar producto")
   print("2) Ver inventario")
   print("3) Salir de la App")
   print("4) Buscar producto")
   print("5) Productos con stock menor al minimo")
   print("6) Sumar el stock de un producto")
   print("7) Consultar claves de producto duplicadas")
   print("====================================")

   menu = int(input("Seleccione una opcion: "))

   if menu==1:
     clavenueva=input("Ingrese la clave del producto nuevo: ")
     productonuevo=input("Ingrese el nombre del producto nuevo: ")
     pesonuevo=input("Ingrese el peso del producto nuevo: ")
     stocknuevo=int(input("Ingrese el stock del producto nuevo: "))
     minimonuevo=int(input("Ingrese el stock minimo del producto nuevo: "))
     precionuevo=float(input("Ingrese el precio del producto nuevo: "))
     agregar_producto(clavenueva, productonuevo, pesonuevo, stocknuevo, minimonuevo, precionuevo)
   elif menu==2:
    print(inventario)
   elif menu==3:
    print("\n==================================")
    print("Gracias por Usar la applicacion, Hasta Luego!")
    print("====================================")
    rep=False
   elif menu==4:
    clavebuscador=input("Ingrese la clave del producto que quiere buscar: ")
    buscar_producto(clavebuscador)
   elif menu==5:
    productos_bajo_minimo()
   elif menu==6:
    sumastock=input("Ingrese la clave del producto el cual quiere sumar su stock actual: ")
    valor_total_inventario(sumastock)
   elif menu==7:
    num_de_claves=int(input("Cuantas claves de producto desea ingresar? "))
    lista_claves=[]
    for i in range(num_de_claves):
       clave = input(f"Ingrese la clave numero {i+1} que desea consultar: ")
       lista_claves.append(clave)
    encontrar_duplicados(lista_claves)
   else:
    cont=int(input("Ingreso una opcion invalida, quiere volver a intentar?: 1) Si 2) No. "))
    if cont==1:
     rep=True
    else:
     print("Gracias por Usar la applicacion, Hasta Luego! ")
     rep=False

       
    
 
 



    


