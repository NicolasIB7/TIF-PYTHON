class Catalogo:
    productos = [] #Variable de clase
    
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
    
        if self.consultar_producto(codigo):
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
        self.productos.append(nuevo_producto)
        return True 

    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo: #Si es igual el producto existe
                return producto 
        return False
    
    def listar_productos(self):
        print()
        print("-"*50)
        for producto in self.productos:
            print(f'Codigo......: {producto["codigo"]}')
            print(f'Descripcion.: {producto["descripcion"]}')
            print(f'Cantidad....: {producto["cantidad"]}')
            print(f'Precio......: {producto["precio"]}')
            print(f'Imagen......: {producto["imagen"]}')
            print(f'Proveedor...: {producto["proveedor"]}')
            print("-"*50)
 
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False    

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True 
        return False 
    
    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 50)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 50)
        else:
            print("Producto no encontrado.")
   
 
# PROGRAMA PRINCIPAL (lo que antes eran funciones ahora son metodos de la clase)
        
#Agregamos productos a la lista 

catalogo = Catalogo()
catalogo.agregar_producto(1, 'Blend herbolaria', 10, 6000, 'HERBORALIA1-1.jpg', 100)
catalogo.agregar_producto(2, 'Blend pasiflora', 12, 6000, 'PASIFLORA.jpg', 101)
catalogo.agregar_producto(3, 'Blend floralina', 8, 6600, 'FLORALINA1.jpg', 102)
catalogo.agregar_producto(4, 'Blend limonelle', 10, 6600, 'LIMONELLE.jpg', 103)
catalogo.agregar_producto(5, 'Blend allegra', 5, 6600, 'ALLEGRA.jpg', 104)

#catalogo.listar_productos()

#Modificamos un producto para probar
#catalogo.modificar_producto(1, 'PROBANDO CAMBIOS', 4, 4000, 'PRUEBA', 107)

#catalogo.listar_productos()

#Eliminamos un producto
#catalogo.eliminar_producto(2)

#catalogo.listar_productos()

#catalogo.mostrar_producto(2)
