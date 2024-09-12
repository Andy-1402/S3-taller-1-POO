# menuAcademico.py

from periodo import CrudPeriodos
from nivel import CrudNiveles
from asignatura import CrudAsignaturas
from profesor import CrudProfesores
from estudiante import CrudEstudiantes
from nota import CrudNotas
from detailnotes import CrudDetalleNotas  # Importamos CrudDetalleNotas
from components import Menu, borrarPantalla, gotoxy
import time

class MenuAcademico:
    def __init__(self):
        self.crud_periodos = CrudPeriodos()
        self.crud_niveles = CrudNiveles()
        self.crud_asignaturas = CrudAsignaturas()
        self.crud_profesores = CrudProfesores()
        self.crud_estudiantes = CrudEstudiantes()
        self.crud_notas = CrudNotas()
        self.crud_detalle_notas = CrudDetalleNotas()  # Instancia para el detalle de notas

    def mostrar_menu_academico(self):
        opc = ''
        while opc != '8':  # Actualizamos la opción de salida a '8'
            borrarPantalla()
            menu_academico = Menu("Menú Académico", 
                                  ["1) Periodos Académicos", 
                                   "2) Niveles Educativos", 
                                   "3) Asignaturas", 
                                   "4) Profesores", 
                                   "5) Estudiantes", 
                                   "6) Notas", 
                                   "7) Detalle de Notas",  # Añadimos la opción para Detalle de Notas
                                   "8) Salir"], 
                                  20, 10)
            opc = menu_academico.menu()
            if opc == "1":
                self.crud_periodos.menu_periodos()
            elif opc == "2":
                self.crud_niveles.menu_niveles()
            elif opc == "3":
                self.crud_asignaturas.menu_asignaturas()
            elif opc == "4":
                self.crud_profesores.menu_profesores()
            elif opc == "5":
                self.crud_estudiantes.menu_estudiantes()
            elif opc == "6":
                self.crud_notas.menu_notas()
            elif opc == "7":
                self.crud_detalle_notas.detalle_de_notas()  # Llamada al menú de detalle de notas
            elif opc == "8":
                break
            else:
                gotoxy(5, 15); print("Opción no válida. Inténtelo de nuevo.")
                time.sleep(2)

if __name__ == "__main__":
    menu_academico = MenuAcademico()
    menu_academico.mostrar_menu_academico()
