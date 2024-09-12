from datetime import datetime
from components import Valida, Menu, gotoxy, borrarPantalla, JsonFile
import time

class Nota:
    def __init__(self, id_estudiante, id_asignatura, id_nivel, nota):
        self.__id_estudiante = id_estudiante
        self.__id_asignatura = id_asignatura
        self.__id_nivel = id_nivel
        self.__nota = nota
        self.__fecha_creacion = datetime.now()  # Cambiado a datetime.now() para incluir la hora

    @property
    def id_estudiante(self):
        return self.__id_estudiante

    @property
    def id_asignatura(self):
        return self.__id_asignatura

    @property
    def id_nivel(self):
        return self.__id_nivel

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, value):
        self.__nota = value

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')  # Convertido a cadena

    def mostrar(self):
        return f"ID Estudiante: {self.__id_estudiante}, ID Asignatura: {self.__id_asignatura}, ID Nivel: {self.__id_nivel}, Nota: {self.__nota}, Fecha Creación: {self.__fecha_creacion}"

class CrudNotas:
    def __init__(self):
        self.archivo = JsonFile("archivos/notas.json")
        self.valida = Valida()

    def menu_notas(self):
        opc = ''
        while opc != '5':
            borrarPantalla()
            menu_notas = Menu("Menu Notas", 
                              ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 
                              20, 10)
            opc = menu_notas.menu()
            if opc == "1":
                self.create()
            elif opc == "2":
                self.update()
            elif opc == "3":
                self.delete()
            elif opc == "4":
                self.consult()
            print("Regresando al menú Notas...")
            time.sleep(2)

    def create(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del estudiante: ")
        id_estudiante = input()
        gotoxy(5, 6); print("Ingrese el ID de la asignatura: ")
        id_asignatura = input()
        gotoxy(5, 7); print("Ingrese el ID del nivel: ")
        id_nivel = input()
        gotoxy(5, 8); print("Ingrese la nota: ")
        nota = input()
        
        nota_obj = Nota(id_estudiante, id_asignatura, id_nivel, nota)
        # Guardar en el archivo JSON
        self.archivo.save([{
            'id_estudiante': nota_obj.id_estudiante,
            'id_asignatura': nota_obj.id_asignatura,
            'id_nivel': nota_obj.id_nivel,
            'nota': nota_obj.nota,
            'fecha_creacion': nota_obj.fecha_creacion
        }])
        gotoxy(5, 10); print("Nota guardada correctamente.")
        time.sleep(2)

    def update(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del estudiante para actualizar la nota: ")
        id_estudiante = input()
        gotoxy(5, 6); print("Ingrese el ID de la asignatura: ")
        id_asignatura = input()
        gotoxy(5, 7); print("Ingrese el ID del nivel: ")
        id_nivel = input()
        notas = self.archivo.read()
        for nota in notas:
            if (nota['id_estudiante'] == id_estudiante and 
                nota['id_asignatura'] == id_asignatura and 
                nota['id_nivel'] == id_nivel):
                gotoxy(5, 8); print(f"Nota actual: {nota['nota']}")
                gotoxy(5, 9); print("Ingrese la nueva nota: ")
                nueva_nota = input()
                nota['nota'] = nueva_nota
                nota['fecha_creacion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Actualiza la fecha y hora
                self.archivo.save(notas)
                gotoxy(5, 11); print("Nota actualizada correctamente.")
                break
        else:
            gotoxy(5, 11); print("Nota no encontrada.")
        time.sleep(2)

    def delete(self):
        borrarPantalla()
        gotoxy(5, 5); print("Ingrese el ID del estudiante para eliminar la nota: ")
        id_estudiante = input()
        gotoxy(5, 6); print("Ingrese el ID de la asignatura: ")
        id_asignatura = input()
        gotoxy(5, 7); print("Ingrese el ID del nivel: ")
        id_nivel = input()
        notas = self.archivo.read()
        for nota in notas:
            if (nota['id_estudiante'] == id_estudiante and 
                nota['id_asignatura'] == id_asignatura and 
                nota['id_nivel'] == id_nivel):
                notas.remove(nota)
                self.archivo.save(notas)
                gotoxy(5, 9); print("Nota eliminada correctamente.")
                break
        else:
            gotoxy(5, 9); print("Nota no encontrada.")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        notas = self.archivo.read()
        gotoxy(5, 5); print("Notas Registradas")
        y = 6
        for nota in notas:
            gotoxy(5, y); print(f"ID Estudiante: {nota['id_estudiante']}, ID Asignatura: {nota['id_asignatura']}, ID Nivel: {nota['id_nivel']}, Nota: {nota['nota']}, Fecha Creación: {nota['fecha_creacion']}")
            y += 1
        gotoxy(5, y + 2); input("Presione una tecla para regresar...")
