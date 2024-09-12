import os
import json
from datetime import date, datetime

class JsonFile:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)# dump:graba datos a un archivo json
      
    def read(self):
        try:
            with open(self.filename,'r') as file:
                data = json.load(file)# load:carga datos desde un archivo json
        except FileNotFoundError:
            data = []
        return data
     
    def find(self,atributo,buscado):
        try:
            with open(self.filename,'r') as file:
                datas = json.load(file)
                data = [item for item in datas if item[atributo] == buscado ]
        except FileNotFoundError:
            data = []
        return data
    
class Valida:
    @staticmethod
    def validar_texto(texto):
        return bool(texto.strip())

    @staticmethod
    def validar_id(id):
        return id.isdigit()

    @staticmethod
    def validar_fecha(fecha):
        try:
            date.fromisoformat(fecha)
            return True
        except ValueError:
            return False

class Menu:
    def __init__(self, title, options, x, y):
        self.title = title
        self.options = options
        self.x = x
        self.y = y

    def menu(self):
        gotoxy(self.x, self.y); print(self.title)
        for index, option in enumerate(self.options, start=1):
            gotoxy(self.x, self.y + index); print(option)
        gotoxy(self.x, self.y + len(self.options) + 1); return input("Elija una opción: ")

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')

def borrarPantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

def obtener_fecha_actual():
    return date.today().isoformat()

def obtener_hora_actual():
    return datetime.now().strftime('%H:%M:%S')
