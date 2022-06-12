print(f"\nNombre: Gilberto Angel de Jesus Suarez\nGrupo: 9 A\nMateria: Desarrollo para dispositivos inteligentes\nFecha: 12/06/2022\n")
"""
Proyecto python + MySQL:
1. Abrir el asistente
2. Login y registro
3. Si elegimos registro, creara un usuario en la bd
4. Si elegimos login, identificara al usuario y nos preguntara
5. Opciones CRUD para consultorios, Usuarios, Doctores, Pacientes y Citas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()