import citas.cita as modelo
import pacientes.paciente as paciente
import medicos.medico as medico

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1][1]}!! Vamos a crear una nueva cita...")

        titulo = input("Introduce el titulo de la cita: ")
        nota = input("Introduce una nota de la cita: ")

        print(f"\n{usuario[1][1]} Estos son tus pacientes:\n")
        pacient =  paciente.Paciente(usuario)
        pacientes = pacient.listar()

        for pte in pacientes:
            print(f"Id: {pte[0]} | Nombre: {pte[1]} {pte[2]} | Registrado el: {pte[10]}")
        
        while(True):
            paciente_id = input("Introduce un id de un paciente existente: ")
            pa_id = pacient.buscar(paciente_id)
            if len(pa_id)> 0:
                break
        
        sintomas = input("Introduce los sintomas del paciente: ")

        print(f"\n{usuario[1][1]} Estos son tus doctores:\n")
        doctor =  medico.Medico(usuario)
        doctores = doctor.listar()

        for doct in doctores:
            print(f"Id: {doct[0]} | Nombre: {doct[1]} {doct[2]} | Registrado el: {doct[8]}")
        
        while(True):
            medico_id = input("Introduce un id de un doctor existente: ")
            med_id = doctor.buscar(medico_id)
            if len(med_id)> 0:
                break

        reservacion = input("Introduce la fecha para la cita(en formato Año-mes-dia): ")
        
        cita = modelo.Cita(titulo, nota, paciente_id, sintomas, usuario[0], medico_id, reservacion)
        guardar = cita.guardar()
        
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has registrado la cita: {cita.titulo}")
        else:
            print(f"\nNo se guardo correctamente, intentalo más tarde: {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\n{usuario[1][1]} Estas son tus citas:\n")
        cita =  modelo.Cita('', '', '', '', usuario[0])
        citas = cita.listar()

        for cit in citas:
            print(f"Titulo: {cit[1]} | Reservada para el: {cit[8]}")
    
    def eliminar(self, usuario):
        print(f"\n{usuario[1][1]}! Eliminar citas: ")

        titulo = input("Introduce el titulo de la cita a eliminar: ")

        cita = modelo.Cita(titulo, '', '', '', usuario[0])
        eliminar = cita.eliminar()

        if eliminar[0] >= 1:
            print(f"\nSe elimino la cita: {cita.titulo}!!")
        else:
            print("Ha ocurrido un error, intentalo mas tarde")