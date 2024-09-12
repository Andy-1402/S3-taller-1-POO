from datetime import datetime
from components import Valida, Menu, gotoxy, borrarPantalla, JsonFile
import time

class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.__nombre = nombre
        self.__id_estudiante = id_estudiante
        self.__fecha_creacion = datetime.now()  # Cambiado a datetime.now() para incluir la hora
        self.__active = True

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def id_estudiante(self):
        return self.__id_estudiante

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')  # Convertido a cadena

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value

    def mostrar(self):
        return f"Nombre: {self.__nombre}, ID: {self.__id_estudiante}, Fecha Creación: {self.__fecha_creacion}, Activo: {self.__active}"

class CrudEstudiantes:
    def __init__(self):
        self.archivo = JsonFile("archivos/estudiantes.json")
        self.valida = Valida()

    def menu_estudiantes(self):
        opc = ''
        while opc != '5':
            borrarPantalla()
            menu_estudiantes = Menu("Menu Estudiantes", 
                                    ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 
                                    20, 10)
            opc = menu_estudiantes.menu()
            if opc == "1":
                self.create()
            elif opc == "2":
                self.update()
            elif opc == "3":
                self.delete()
            elif opc == "4":
                self.consult()
            print("Regresando al menú Estudiantes...")
            time.sleep(2)

    def create(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el nombre del estudiante: ")
        nombre = input()
        gotoxy(5, 6); print("Ingrese el ID del estudiante: ")
        id_estudiante = input()
        
        estudiante = Estudiante(nombre, id_estudiante)
        # Guardar en el archivo JSON
        self.archivo.save([{
            'nombre': estudiante.nombre,
            'id_estudiante': estudiante.id_estudiante,
            'fecha_creacion': estudiante.fecha_creacion,
            'active': estudiante.active
        }])
        gotoxy(5, 8); print("Estudiante guardado correctamente.")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del estudiante a actualizar: ")
        id_estudiante = input()
        estudiantes = self.archivo.read()
        for estudiante in estudiantes:
            if estudiante['id_estudiante'] == id_estudiante:
                gotoxy(5, 6); print(f"Nombre actual: {estudiante['nombre']}")
                gotoxy(5, 7); print("Ingrese el nuevo nombre: ")
                nuevo_nombre = input()
                estudiante['nombre'] = nuevo_nombre
                estudiante['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha y hora
                self.archivo.save(estudiantes)
                gotoxy(5, 9); print("Estudiante actualizado correctamente.")
                break
        else:
            gotoxy(5, 9); print("Estudiante no encontrado.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del estudiante a eliminar: ")
        id_estudiante = input()
        estudiantes = self.archivo.read()
        for estudiante in estudiantes:
            if estudiante['id_estudiante'] == id_estudiante:
                estudiante['active'] = False
                estudiante['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha y hora
                self.archivo.save(estudiantes)
                gotoxy(5, 7); print("Estudiante eliminado correctamente.")
                break
        else:
            gotoxy(5, 7); print("Estudiante no encontrado.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        estudiantes = self.archivo.read()
        gotoxy(5, 5); print("Estudiantes Registrados")
        y = 6
        for estudiante in estudiantes:
            if estudiante['active']:
                gotoxy(5, y); print(f"Nombre: {estudiante['nombre']}, ID: {estudiante['id_estudiante']}, Fecha Creación: {estudiante['fecha_creacion']}, Activo: {estudiante['active']}")
                y += 1
        gotoxy(5, y + 2); input("Presione una tecla para regresar...")
