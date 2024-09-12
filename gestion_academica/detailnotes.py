from datetime import datetime
from components import Valida, Menu, gotoxy, borrarPantalla, JsonFile
import time

# Clase modelo para representar cada detalle de nota
class DetalleNota:
    def __init__(self, id_detalle, estudiante, nota1, nota2, recuperacion=None, observacion=''):
        self.id = id_detalle
        self.estudiante = estudiante
        self.nota1 = nota1
        self.nota2 = nota2
        self.recuperacion = recuperacion
        self.observacion = observacion
        self.fecha_creacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.active = True  # Marca si el detalle está activo o eliminado

# Clase CrudDetalleNotas que maneja las operaciones CRUD
class CrudDetalleNotas:
    def __init__(self):
        self.archivo = JsonFile("archivos/detalle_notas.json")
        self.valida = Valida()

    # Menú principal de opciones para el CRUD
    def detalle_de_notas(self):
        opc = ''
        while opc != '5':  # Menú en bucle hasta que el usuario elija salir
            borrarPantalla()
            menu_notas = Menu("Menú de Notas", 
                              ["1) Añadir Nota", "2) Actualizar Nota", "3) Eliminar Nota", "4) Consultar Notas", "5) Salir"], 
                              20, 10)
            opc = menu_notas.menu()
            if opc == "1":
                self.addNota()  
            elif opc == "2":
                self.update()  
            elif opc == "3":
                self.delete()  
            elif opc == "4":
                self.consult() 
            print("Regresando al menú de Notas...")
            time.sleep(2)

    # Método para añadir una nueva nota
    def addNota(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del detalle de nota: ")
        id_detalle = input()
        gotoxy(5, 6); print("Ingrese el nombre del estudiante: ")
        estudiante = input()
        gotoxy(5, 7); print("Ingrese la primera nota: ")
        nota1 = float(input())
        gotoxy(5, 8); print("Ingrese la segunda nota: ")
        nota2 = float(input())
        gotoxy(5, 9); print("Ingrese la nota de recuperación (si aplica, de lo contrario presione Enter): ")
        recuperacion = input()
        recuperacion = float(recuperacion) if recuperacion else None
        gotoxy(5, 10); print("Ingrese alguna observación (si aplica, de lo contrario presione Enter): ")
        observacion = input()

        # Crear una instancia de DetalleNota (modelo de datos)
        detalle_nota = DetalleNota(id_detalle, estudiante, nota1, nota2, recuperacion, observacion)

        # Guardar en el archivo JSON
        self.archivo.save([{
            'id': detalle_nota.id,
            'estudiante': detalle_nota.estudiante,
            'nota1': detalle_nota.nota1,
            'nota2': detalle_nota.nota2,
            'recuperacion': detalle_nota.recuperacion,
            'observacion': detalle_nota.observacion,
            'fecha_creacion': detalle_nota.fecha_creacion,
            'active': detalle_nota.active
        }])

        gotoxy(5, 12); print("Detalle de nota añadido correctamente.")
        time.sleep(2)

    # Método para actualizar una nota existente
    def update(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del detalle de nota a actualizar: ")
        id_detalle = input()
        detalles = self.archivo.read()
        for detalle in detalles:
            if detalle['id'] == id_detalle:
                gotoxy(5, 6); print(f"Estudiante actual: {detalle['estudiante']}")
                gotoxy(5, 7); print("Ingrese la nueva primera nota: ")
                nueva_nota1 = float(input())
                detalle['nota1'] = nueva_nota1
                gotoxy(5, 8); print("Ingrese la nueva segunda nota: ")
                nueva_nota2 = float(input())
                detalle['nota2'] = nueva_nota2
                detalle['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha
                self.archivo.save(detalles)
                gotoxy(5, 10); print("Detalle de nota actualizado correctamente.")
                break
        else:
            gotoxy(5, 10); print("Detalle de nota no encontrado.")
        time.sleep(2)

    # Método para eliminar una nota (desactivarla)
    def delete(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del detalle de nota a eliminar: ")
        id_detalle = input()
        detalles = self.archivo.read()
        for detalle in detalles:
            if detalle['id'] == id_detalle:
                detalle['active'] = False
                detalle['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha
                self.archivo.save(detalles)
                gotoxy(5, 7); print("Detalle de nota eliminado correctamente.")
                break
        else:
            gotoxy(5, 7); print("Detalle de nota no encontrado.")
        time.sleep(2)

    # Método para consultar todas las notas
    def consult(self):
        borrarPantalla()
        detalles = self.archivo.read()
        gotoxy(5, 5); print("Detalles de Notas Registrados")
        y = 6
        for detalle in detalles:
            if detalle['active']:
                gotoxy(5, y); print(f"ID: {detalle['id']}, Estudiante: {detalle['estudiante']}, Nota 1: {detalle['nota1']}, Nota 2: {detalle['nota2']}, Recuperación: {detalle['recuperacion']}, Observación: {detalle['observacion']}, Fecha Creación: {detalle['fecha_creacion']}, Activo: {detalle['active']}")
                y += 1
        gotoxy(5, y + 2); input("Presione una tecla para regresar...")