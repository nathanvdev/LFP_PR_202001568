from tkinter import filedialog, Tk
ContenDataFIle = ""
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
        with open(filename) as infile:
                ContenDataFIle = infile.read().strip()
                print(str(ContenDataFIle))
                for caracter in ContenDataFIle:
                    print(caracter)
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
            DataFile = FileChooser()

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
