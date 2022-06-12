import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Medico:

    def __init__(self, nombre="", apellido="", genero="", email="", direccion="", telefono="", consultorio_id=""):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.consultorio_id = consultorio_id

    def guardar(self):
        sql = "INSERT INTO medico VALUES(null, %s, %s, %s, %s, %s, %s, 1, NOW(), %s)"
        medico = (self.nombre, self.apellido, self.genero, self.email, self.direccion, self.telefono, self.consultorio_id)

        cursor.execute(sql, medico)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM medico"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def buscar(self, id):
        sql = f"SELECT * FROM medico WHERE id = {id}"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"DELETE FROM medico WHERE nombre LIKE '%{self.nombre}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]