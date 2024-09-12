from datetime import datetime
from components import Valida, Menu, gotoxy, borrarPantalla, JsonFile
import time

class Periodo:
    def __init__(self, nombre, id_periodo):
        self.__nombre = nombre
        self.__id_periodo = id_periodo
        self.__fecha_creacion = datetime.now()  # Cambiado a datetime.now() para incluir la hora
        self.__active = True

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def id_periodo(self):
        return self.__id_periodo

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
            "id_periodo": self.__id_periodo,
            "fecha_creacion": self.fecha_creacion,
            "active": self.__active
        }

class CrudPeriodos:
    def __init__(self):
        self.archivo = JsonFile("archivos/periodos.json")
        self.valida = Valida()

    def menu_periodos(self):
        opc = ''
        while opc != '5':
            borrarPantalla()
            menu_periodos = Menu("Menú Periodos", 
                                ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 
                                20, 10)
            opc = menu_periodos.menu()
            if opc == "1":
                self.create()
            elif opc == "2":
                self.update()
            elif opc == "3":
                self.delete()
            elif opc == "4":
                self.consult()
            print("Regresando al menú Periodos...")
            time.sleep(2)

    def create(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el nombre del periodo: ")
        nombre = input()
        gotoxy(5, 6); print("Ingrese el ID del periodo: ")
        id_periodo = input()
        
        if not self.valida.validar_texto(nombre) or not self.valida.validar_id(id_periodo):
            gotoxy(5, 8); print("Error: Datos inválidos.")
            time.sleep(2)
            return
        
        periodos = self.archivo.read()
        for periodo in periodos:
            if periodo['id_periodo'] == id_periodo:
                gotoxy(5, 8); print("Error: ID de periodo ya registrado.")
                time.sleep(2)
                return

        nuevo_periodo = Periodo(nombre, id_periodo)
        periodos.append(nuevo_periodo.mostrar())
        self.archivo.save(periodos)
        gotoxy(5, 8); print("Periodo guardado correctamente.")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del periodo a actualizar: ")
        id_periodo = input()
        periodos = self.archivo.read()
        for periodo in periodos:
            if periodo['id_periodo'] == id_periodo:
                gotoxy(5, 6); print(f"Nombre actual: {periodo['nombre']}")
                gotoxy(5, 7); print("Ingrese el nuevo nombre: ")
                nuevo_nombre = input()

                if not self.valida.validar_texto(nuevo_nombre):
                    gotoxy(5, 9); print("Error: Nombre inválido.")
                    time.sleep(2)
                    return

                periodo['nombre'] = nuevo_nombre
                self.archivo.save(periodos)
                gotoxy(5, 9); print("Periodo actualizado correctamente.")
                break
        else:
            gotoxy(5, 9); print("Periodo no encontrado.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del periodo a eliminar: ")
        id_periodo = input()
        periodos = self.archivo.read()
        for periodo in periodos:
            if periodo['id_periodo'] == id_periodo:
                periodo['active'] = False
                self.archivo.save(periodos)
                gotoxy(5, 7); print("Periodo eliminado correctamente.")
                break
        else:
            gotoxy(5, 7); print("Periodo no encontrado.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        periodos = self.archivo.read()
        gotoxy(5, 5); print("Periodos Registrados")
        y = 6
        for periodo in periodos:
            if periodo['active']:
                gotoxy(5, y); print(f"Nombre: {periodo['nombre']}, ID: {periodo['id_periodo']}, Fecha Creación: {periodo['fecha_creacion']}, Activo: {periodo['active']}")
                y += 1
        gotoxy(5, y + 2); input("Presione una tecla para regresar...")
