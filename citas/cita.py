import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:

    def __init__(self, titulo="", nota="", paciente_id="", sintomas="", usuario_id="", medico_id="", reservacion=""):
        self.titulo = titulo
        self.nota = nota
        self.paciente_id = paciente_id
        self.sintomas = sintomas
        self.usuario_id = usuario_id
        self.medico_id = medico_id
        self.reservacion = reservacion

    def guardar(self):
        sql = "INSERT INTO cita VALUES(null, %s, %s, %s, %s, %s, %s, NOW(), %s)"
        cita = (self.titulo, self.nota, self.paciente_id, self.sintomas, self.usuario_id, self.medico_id, self.reservacion)

        cursor.execute(sql, cita)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM cita WHERE usuario_id = {self.usuario_id}"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"DELETE FROM cita WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]