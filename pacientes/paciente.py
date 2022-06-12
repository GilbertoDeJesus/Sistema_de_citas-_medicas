import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Paciente:

    def __init__(self, nombre="", apellido="", genero="", edad="", email="", direccion="", telefono="", sintomas=""):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.sintomas = sintomas

    def guardar(self):
        sql = "INSERT INTO paciente VALUES(null, %s, %s, %s, %s, %s, %s, %s, 1, %s, NOW())"
        paciente = (self.nombre, self.apellido, self.genero, self.edad, self.email, self.direccion, self.telefono, self.sintomas)

        cursor.execute(sql, paciente)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM paciente"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def buscar(self, id):
        sql = f"SELECT * FROM paciente WHERE id = {id}"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"DELETE FROM paciente WHERE nombre LIKE '%{self.nombre}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]