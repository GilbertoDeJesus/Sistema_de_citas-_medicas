import usuarios.usuario as modelo
import consultorios.acciones as consultorio
import consultorios.consultorio as conscon
import medicos.acciones as medico
import medicos.medico as medcon
import pacientes.acciones as paciente
import pacientes.paciente as pacicon
import citas.acciones as cita

class Acciones:

    def registro(self):
        print("Se procedera a realizar tu registro en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!")


    def login(self):
        print("Identificate en el sistema...")

        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario('', '', email, password).identificar()

        if usuario[0] >= 1:
            print(f"\nBienvenido de nuevo {usuario[1][1]}! Te has registrado el {usuario[1][5]}\n")
            self.proximasAcciones(usuario)
        else:
            print("\nEmail o password incorrectos!!")
    

    def proximasAcciones(self, usuario):
        print("""
        _________________________________________

                 Acciones disponibles:
        _________________________________________

        | - Registrar consultorio ---- [regco]  |
        | - Mostrar consultorio ------ [mosco]  |
        | - Eliminar consultorio ----- [elico]  |
        | - Registrar doctor --------- [regdo]  |
        | - Mostrar doctor ----------- [mosdo]  |
        | - Eliminar doctor ---------- [elido]  |
        | - Registrar paciente ------- [regpa]  |
        | - Mostrar paciente --------- [mospa]  |
        | - Eliminar paciente -------- [elipa]  |
        | - Registrar cita ----------- [regci]  |
        | - Mostrar cita ------------- [mosci]  |
        | - Eliminar cita ------------ [elici]  |
        | - Salir -------------------- [salir]  |
        _________________________________________
        """)

        accion = input("¿Que quieres hacer?: ")
        consul = consultorio.Acciones()
        medic = medico.Acciones()
        pacie = paciente.Acciones()
        citas = cita.Acciones()

        if accion == "regco":
            consul.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mosco":
            consul.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "elico":
            consul.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "regdo":
            if len(conscon.Consultorio().listar()) == 0:
                print("Necesitas crear un consultorio primero")
                self.proximasAcciones(usuario)
            else:
                medic.crear(usuario)
                self.proximasAcciones(usuario)
        
        elif accion == "mosdo":
            medic.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "elido":
            medic.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "regpa":
            pacie.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mospa":
            pacie.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "elipa":
            pacie.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "regci":
            if len(medcon.Medico().listar()) == 0 & len(pacicon.Paciente().listar()) == 0:
                print("Necesitas crear un consultorio primero")
                self.proximasAcciones(usuario)
            else:
                citas.crear(usuario)
                self.proximasAcciones(usuario)
        
        elif accion == "mosci":
            citas.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "elici":
            citas.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "salir":
            print("Adios ...")
            exit()