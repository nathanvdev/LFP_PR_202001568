from fileinput import filename
from msilib.schema import File, IniFile
from tkinter import filedialog, Tk

def FileChooser():
    try:
        filename = filedialog.askopenfilename(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos data', '*.data'),
                         ('Archivos lfp', '*.lfp'),
                         ('Todos los archivos', '*.*'))
        )
        print(filename)
    except:
        print('No se selecciono correctamente el archivo')
        return None
        
def ImportDataFile():
    ContenDataFIle = ''
    try:
        DataFile = FileChooser()
        with open(DataFile) as iniFile:
            ContenDataFIle = iniFile.read().strip()
            ContenDataFIle = ContenDataFIle.lower()
            print(str(ContenDataFIle))
    except:
        print('no sirvio')
        


if __name__ == '__main__':
    while True:
        Menu = input ('''=============================
||1. Cargar Data           ||
||2. Cargar Instrucciones  ||
||3. Analizar              ||
||4. Reportes              ||
||5. Salir                 ||
=============================
Elige una opción:  ------->  ''')

        if Menu == '1':
            ImportDataFile()


        elif Menu == '2':
            pass
        elif Menu == '3':
            pass
        elif Menu == '4':
            pass
        elif Menu == '5':
            print('\nGracias por utilizar este programa')
            break
        else:
            print("Elija una opcion valida")
