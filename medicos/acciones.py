import medicos.medico as modelo
import consultorios.consultorio as consultorio

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1][1]}!! Vamos a crear un nuevo doctor...")

        consultor = consultorio.Consultorio(usuario[0])
        consultorios = consultor.listar()

        print("\nEstos son los consultorios disponibles:\n")
        for con in consultorios:
            print(f"Id: {con[0]} --- Nombre: {con[1]}")
        print("\n")

        nombre = input("Introduce el nombre del doctor(a): ")
        apellido = input("Introduce el apellido del doctor(a): ")
        genero = input("Introduce el genero del doctor(a): ")
        email = input("Introduce el email del doctor(a): ")
        direccion = input("Introduce la direccion del doctor(a): ")
        telefono = input("Introduce el telefono del doctor(a): ")

        while(True):
            consultorio_id = input("Introduce un id de un consultorio existente: ")
            med_id = consultor.buscar(consultorio_id)
            if len(med_id)> 0:
                break
        
        medico = modelo.Medico(nombre, apellido, genero, email, direccion, telefono, consultorio_id)
        guardar = medico.guardar()
        
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has dado de alta al doctor(a): {medico.nombre}")
        else:
            print(f"\nNo se guardo correctamente, intentalo más tarde: {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\n{usuario[1][1]} Estos son tus doctores:\n")
        medico =  modelo.Medico(usuario)
        medicos = medico.listar()

        for med in medicos:
            print(f"Nombre: {med[1]} {med[2]} | Registrado: {med[8]}")
    
    def eliminar(self, usuario):
        print(f"\n{usuario[1][1]}! Eliminar doctor(a): ")

        nombre = input("Introduce el nombre del doctor(a) a eliminar: ")

        medico = modelo.Medico(nombre)
        eliminar = medico.eliminar()

        if eliminar[0] >= 1:
            print(f"\nSe elimino al doctor(a): {medico.nombre}!!")
        else:
            print("Ha ocurrido un error, intentalo mas tarde")