from datetime import datetime
from components import Valida, Menu, gotoxy, borrarPantalla, JsonFile
import time

class Nivel:
    def __init__(self, nombre, id_nivel):
        self.__nombre = nombre
        self.__id_nivel = id_nivel
        self.__fecha_creacion = datetime.now()  # Cambiado a datetime.now() para incluir la hora
        self.__active = True

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def id_nivel(self):
        return self.__id_nivel

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
        return f"Nombre: {self.__nombre}, ID: {self.__id_nivel}, Fecha Creación: {self.__fecha_creacion}, Activo: {self.__active}"

class CrudNiveles:
    def __init__(self):
        self.archivo = JsonFile("archivos/niveles.json")
        self.valida = Valida()

    def menu_niveles(self):
        opc = ''
        while opc != '5':
            borrarPantalla()
            menu_niveles = Menu("Menu Niveles", 
                               ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 
                               20, 10)
            opc = menu_niveles.menu()
            if opc == "1":
                self.create()
            elif opc == "2":
                self.update()
            elif opc == "3":
                self.delete()
            elif opc == "4":
                self.consult()
            print("Regresando al menú Niveles...")
            time.sleep(2)

    def create(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el nombre del nivel: ")
        nombre = input()
        gotoxy(5, 6); print("Ingrese el ID del nivel: ")
        id_nivel = input()
        
        nivel = Nivel(nombre, id_nivel)
        # Guardar en el archivo JSON
        self.archivo.save([{
            'nombre': nivel.nombre,
            'id_nivel': nivel.id_nivel,
            'fecha_creacion': nivel.fecha_creacion,
            'active': nivel.active
        }])
        gotoxy(5, 8); print("Nivel guardado correctamente.")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del nivel a actualizar: ")
        id_nivel = input()
        niveles = self.archivo.read()
        for nivel in niveles:
            if nivel['id_nivel'] == id_nivel:
                gotoxy(5, 6); print(f"Nombre actual: {nivel['nombre']}")
                gotoxy(5, 7); print("Ingrese el nuevo nombre: ")
                nuevo_nombre = input()
                nivel['nombre'] = nuevo_nombre
                nivel['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha y hora
                self.archivo.save(niveles)
                gotoxy(5, 9); print("Nivel actualizado correctamente.")
                break
        else:
            gotoxy(5, 9); print("Nivel no encontrado.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del nivel a eliminar: ")
        id_nivel = input()
        niveles = self.archivo.read()
        for nivel in niveles:
            if nivel['id_nivel'] == id_nivel:
                nivel['active'] = False
                nivel['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha y hora
                self.archivo.save(niveles)
                gotoxy(5, 7); print("Nivel eliminado correctamente.")
                break
        else:
            gotoxy(5, 7); print("Nivel no encontrado.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        niveles = self.archivo.read()
        gotoxy(5, 5); print("Niveles Registrados")
        y = 6
        for nivel in niveles:
            if nivel['active']:
                gotoxy(5, y); print(f"Nombre: {nivel['nombre']}, ID: {nivel['id_nivel']}, Fecha Creación: {nivel['fecha_creacion']}, Activo: {nivel['active']}")
                y += 1
        gotoxy(5, y + 2); input("Presione una tecla para regresar...")
