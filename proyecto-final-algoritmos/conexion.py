import mysql.connector 
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            port = '3306',
                                            password ='123456789')



    def inserta_producto(self,codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql='''INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()