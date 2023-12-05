import mysql.connector

class Catalogo:
    
    def __init__(self, host, user, password, database): #init metodo inicializacion de la clase
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True) #porque sino devuelve tupla #conexion llamando al metodo cursor
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT)''')
        #creamos tabla llamada productos
        self.conn.commit()
        
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        producto_existe = self.cursor.fetchone()
        if producto_existe:
             return False #para que no lo agregue y salga
         
        sql = f"INSERT INTO productos (codigo, descripcion, cantidad, precio, imagen_url, proveedor) VALUES ({codigo}, '{descripcion}', {cantidad}, {precio}, '{imagen}', {proveedor})" 
        self.cursor.execute(sql) #ejecutamos consulta
        self.conn.commit() #comfirmamos
        return True

    def consultar_producto(self, codigo):
    # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")#si pegas eso en php consultas
        return self.cursor.fetchone()  
    
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        sql = f"UPDATE productos SET descripcion = '{nueva_descripcion}', cantidad = {nueva_cantidad}, precio = {nuevo_precio}, imagen_url = '{nueva_imagen}', proveedor = {nuevo_proveedor} WHERE codigo = {codigo}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0
        
    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")
     
    def listar_productos(self):
    # Mostramos en pantalla un listado de todos los productos en la tabla
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()#todos los productos
        print("-" * 40)
        for producto in productos:
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)
        
    def eliminar_producto(self, codigo):
    # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    

#------------------------------------------------------------
#Programa principal

catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')

# Agregamos productos

catalogo.agregar_producto(1, 'Blend herbolaria', 10, 6000, 'HERBORALIA1-1.jpg', 100)
catalogo.agregar_producto(2, 'Blend pasiflora', 12, 6000, 'PASIFLORA.jpg', 101)
catalogo.agregar_producto(3, 'Blend floralina', 8, 6600, 'FLORALINA1.jpg', 102)
catalogo.agregar_producto(4, 'Blend limonelle', 10, 6600, 'LIMONELLE.jpg', 103)
catalogo.agregar_producto(5, 'Blend allegra', 5, 6600, 'ALLEGRA.jpg', 104)

# Consultamos un producto y lo mostramos
# cod_prod = int(input("Ingrese el código del producto: "))
# producto = catalogo.consultar_producto(cod_prod)
# if producto:
#     print(f"Producto encontrado: {producto['codigo']} - {producto['descripcion']}")
# else:
#     print(f'Producto {cod_prod} no encontrado.')

#catalogo.mostrar_producto(1)
#catalogo.modificar_producto(1, 'PROBANDO CAMBIOS', 4, 4000, 'PRUEBA', 107)
#catalogo.mostrar_producto(1)

catalogo.listar_productos()
# catalogo.eliminar_producto(1)
# catalogo.listar_productos()
