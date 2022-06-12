import pacientes.paciente as modelo

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1][1]}!! Vamos a crear un nuevo paciente...")

        nombre = input("Introduce el nombre del paciente: ")
        apellido = input("Introduce el apellido del paciente: ")
        genero = input("Introduce el genero del paciente: ")
        edad = input("Introduce la edad del paciente: ")
        email = input("Introduce el email del paciente: ")
        direccion = input("Introduce la direccion del paciente: ")
        telefono = input("Introduce el telefono del paciente: ")
        sintomas = input("Introduce los sintomas del paciente: ")
        
        paciente = modelo.Paciente(nombre, apellido, genero, edad, email, direccion, telefono, sintomas)
        guardar = paciente.guardar()
        
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has dado de alta al paciente: {paciente.nombre}")
        else:
            print(f"\nNo se guardo correctamente, intentalo más tarde: {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\n{usuario[1][1]} Estos son tus pacientes:\n")
        paciente =  modelo.Paciente(usuario)
        pacientes = paciente.listar()

        for pte in pacientes:
            print(f"Nombre: {pte[1]} {pte[2]} | Registrado el: {pte[10]}")
    
    def eliminar(self, usuario):
        print(f"\n{usuario[1][1]}! Eliminar paciente: ")

        nombre = input("Introduce el nombre del paciente a eliminar: ")

        paciente = modelo.Paciente(nombre)
        eliminar = paciente.eliminar()

        if eliminar[0] >= 1:
            print(f"\nSe elimino al paciente: {paciente.nombre}!!")
        else:
            print("Ha ocurrido un error, intentalo mas tarde")