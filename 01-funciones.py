#Definimos una lista
productos = []

def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):   
    
    if consultar_producto(codigo):
        return False

    #Diccionario de datos
    nuevo_producto = {
        'codigo': codigo, 
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor 
    }
    productos.append(nuevo_producto)
    return True 

def consultar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo: #Si es igual el producto existe
            return producto 
    return False

def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor
            return True
    return False  

def listar_productos():
    print()
    print("-"*50)
    for producto in productos:
        print(f'Codigo......: {producto["codigo"]}')
        print(f'Descripcion.: {producto["descripcion"]}')
        print(f'Cantidad....: {producto["cantidad"]}')
        print(f'Precio......: {producto["precio"]}')
        print(f'Imagen......: {producto["imagen"]}')
        print(f'Proveedor...: {producto["proveedor"]}')
        print("-"*50)
  
def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return True  
    return False      
        
#Agregamos productos a la lista 
agregar_producto(1, 'Blend herbolaria', 10, 6000, 'HERBORALIA1-1.jpg', 100)
agregar_producto(2, 'Blend pasiflora', 12, 6000, 'PASIFLORA.jpg', 101)
agregar_producto(3, 'Blend floralina', 8, 6600, 'FLORALINA1.jpg', 102)
agregar_producto(4, 'Blend limonelle', 10, 6600, 'LIMONELLE.jpg', 103)
agregar_producto(5, 'Blend allegra', 5, 6600, 'ALLEGRA.jpg', 104)

cod_prod = int(input("Ingrese el codigo del producto: "))
producto = consultar_producto(cod_prod)
print(f'Resultado: {producto}')
if producto:
    print(f'Producto encontrado: {producto["codigo"]} - {producto["descripcion"]}')
else: 
    print(f'Producto {cod_prod} no encontrado.')

# #Listar productos
# print("***** LISTADO DE PRODUCTOS *****")
# listar_productos()
#print(productos)

# #Modificar un producto
# modificar_producto(1, 'PROBANDO CAMBIOS', 4, 4000, 'PRUEBA.jpg', 107)

# #Producto que no existe
# modificar_producto(9, 'PROBANDO CAMBIOS', 4, 4000, 'PRUEBA.jpg', 107)

# #Eliminar un producto
# eliminar_producto(1)

# print("***** LISTADO DE PRODUCTOS *****")
# listar_productos()
#print(productos)

