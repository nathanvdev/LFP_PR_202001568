from msilib.schema import File
from sqlite3 import DatabaseError
from tkinter import filedialog, Tk

def FileChooser():
    FileText = ''
    text = ''
    Tk().withdraw()
    try:
        filename = filedialog.askopenfilename(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos data', '*.data'),
                         ('Archivos lfp', '*.lfp'),
                         ('Todos los archivos', '*.*'))
        )
        print(filename)
        with open(filename) as infile:
                FileText = infile.read()
                FileText = FileText.lower()

        for chartacter in FileText:
            if chartacter != '\"':
                if (chartacter != ' ' and chartacter != '\n' and chartacter != '\t'):
                    text += chartacter
        return text
    except:
        print('No se selecciono correctamente el archivo')
        return None


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
            ContentDataFile = FileChooser()
            Month_n = ''
            Year_n = ''
            Month = False
            Year = False
            Parenth = False

            for Character in ContentDataFile:

                if not Parenth and not Year:
                    if Character != ':':
                        pass

                        

                


        print(ContentDataFile)


            
        
            
            


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
