from datetime import datetime
from components import Valida, Menu, gotoxy, borrarPantalla, JsonFile
import time

class Profesor:
    def __init__(self, nombre, id_profesor):
        self.__nombre = nombre
        self.__id_profesor = id_profesor
        self.__fecha_creacion = datetime.now()  # Cambiado a datetime.now() para incluir la hora
        self.__active = True

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def id_profesor(self):
        return self.__id_profesor

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
        return {
            "nombre": self.__nombre,
            "id_profesor": self.__id_profesor,
            "fecha_creacion": self.fecha_creacion,
            "active": self.__active
        }

class CrudProfesores:
    def __init__(self):
        self.archivo = JsonFile("archivos/profesores.json")
        self.valida = Valida()

    def menu_profesores(self):
        opc = ''
        while opc != '5':
            borrarPantalla()
            menu_profesores = Menu("Menú Profesores", 
                                   ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 
                                   20, 10)
            opc = menu_profesores.menu()
            if opc == "1":
                self.create()
            elif opc == "2":
                self.update()
            elif opc == "3":
                self.delete()
            elif opc == "4":
                self.consult()
            print("Regresando al menú Profesores...")
            time.sleep(2)

    def create(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el nombre del profesor: ")
        nombre = input()
        gotoxy(5, 6); print("Ingrese el ID del profesor: ")
        id_profesor = input()
        
        if not self.valida.validar_texto(nombre) or not self.valida.validar_id(id_profesor):
            gotoxy(5, 8); print("Error: Datos inválidos.")
            time.sleep(2)
            return

        profesores = self.archivo.read()
        for profesor in profesores:
            if profesor['id_profesor'] == id_profesor:
                gotoxy(5, 8); print("Error: ID de profesor ya registrado.")
                time.sleep(2)
                return

        nuevo_profesor = Profesor(nombre, id_profesor)
        profesores.append(nuevo_profesor.mostrar())
        self.archivo.save(profesores)
        gotoxy(5, 8); print("Profesor guardado correctamente.")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del profesor a actualizar: ")
        id_profesor = input()
        profesores = self.archivo.read()
        for profesor in profesores:
            if profesor['id_profesor'] == id_profesor:
                gotoxy(5, 6); print(f"Nombre actual: {profesor['nombre']}")
                gotoxy(5, 7); print("Ingrese el nuevo nombre: ")
                nuevo_nombre = input()

                if not self.valida.validar_texto(nuevo_nombre):
                    gotoxy(5, 9); print("Error: Nombre inválido.")
                    time.sleep(2)
                    return

                profesor['nombre'] = nuevo_nombre
                self.archivo.save(profesores)
                gotoxy(5, 9); print("Profesor actualizado correctamente.")
                break
        else:
            gotoxy(5, 9); print("Profesor no encontrado.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del profesor a eliminar: ")
        id_profesor = input()
        profesores = self.archivo.read()
        for profesor in profesores:
            if profesor['id_profesor'] == id_profesor:
                profesor['active'] = False
                self.archivo.save(profesores)
                gotoxy(5, 7); print("Profesor eliminado correctamente.")
                break
        else:
            gotoxy(5, 7); print("Profesor no encontrado.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        profesores = self.archivo.read()
        gotoxy(5, 5); print("Profesores Registrados")
        y = 6
        for profesor in profesores:
            if profesor['active']:
                gotoxy(5, y); print(f"Nombre: {profesor['nombre']}, ID: {profesor['id_profesor']}, Fecha Creación: {profesor['fecha_creacion']}, Activo: {profesor['active']}")
                y += 1
        gotoxy(5, y + 2); input("Presione una tecla para regresar...")
