from datetime import datetime
from components import Valida, Menu, gotoxy, borrarPantalla, JsonFile
import time

class Asignatura:
    def __init__(self, nombre, id_asignatura):
        self.__nombre = nombre
        self.__id_asignatura = id_asignatura
        self.__fecha_creacion = datetime.now()  # Cambiado a datetime.now() para incluir la hora
        self.__active = True

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def id_asignatura(self):
        return self.__id_asignatura

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
        return f"Nombre: {self.__nombre}, ID: {self.__id_asignatura}, Fecha Creación: {self.__fecha_creacion}, Activo: {self.__active}"

class CrudAsignaturas:
    def __init__(self):
        self.archivo = JsonFile("archivos/asignaturas.json")
        self.valida = Valida()

    def menu_asignaturas(self):
        opc = ''
        while opc != '5':
            borrarPantalla()
            menu_asignaturas = Menu("Menu Asignaturas", 
                                    ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 
                                    20, 10)
            opc = menu_asignaturas.menu()
            if opc == "1":
                self.create()
            elif opc == "2":
                self.update()
            elif opc == "3":
                self.delete()
            elif opc == "4":
                self.consult()
            print("Regresando al menú Asignaturas...")
            time.sleep(2)

    def create(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el nombre de la asignatura: ")
        nombre = input()
        gotoxy(5, 6); print("Ingrese el ID de la asignatura: ")
        id_asignatura = input()
        
        asignatura = Asignatura(nombre, id_asignatura)
        # Guardar en el archivo JSON
        self.archivo.save([{
            'nombre': asignatura.nombre,
            'id_asignatura': asignatura.id_asignatura,
            'fecha_creacion': asignatura.fecha_creacion,
            'active': asignatura.active
        }])
        gotoxy(5, 8); print("Asignatura guardada correctamente.")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID de la asignatura a actualizar: ")
        id_asignatura = input()
        asignaturas = self.archivo.read()
        for asignatura in asignaturas:
            if asignatura['id_asignatura'] == id_asignatura:
                gotoxy(5, 6); print(f"Nombre actual: {asignatura['nombre']}")
                gotoxy(5, 7); print("Ingrese el nuevo nombre: ")
                nuevo_nombre = input()
                asignatura['nombre'] = nuevo_nombre
                asignatura['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha y hora
                self.archivo.save(asignaturas)
                gotoxy(5, 9); print("Asignatura actualizada correctamente.")
                break
        else:
            gotoxy(5, 9); print("Asignatura no encontrada.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID de la asignatura a eliminar: ")
        id_asignatura = input()
        asignaturas = self.archivo.read()
        for asignatura in asignaturas:
            if asignatura['id_asignatura'] == id_asignatura:
                asignatura['active'] = False
                asignatura['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha y hora
                self.archivo.save(asignaturas)
                gotoxy(5, 7); print("Asignatura eliminada correctamente.")
                break
        else:
            gotoxy(5, 7); print("Asignatura no encontrada.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        asignaturas = self.archivo.read()
        gotoxy(5, 5); print("Asignaturas Registradas")
        y = 6
        for asignatura in asignaturas:
            if asignatura['active']:
                gotoxy(5, y); print(f"Nombre: {asignatura['nombre']}, ID: {asignatura['id_asignatura']}, Fecha Creación: {asignatura['fecha_creacion']}, Activo: {asignatura['active']}")
                y += 1
        gotoxy(5, y + 2); input("Presione una tecla para regresar...")
