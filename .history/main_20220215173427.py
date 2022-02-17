from selectors import EpollSelector
from tkinter import filedialog, Tk

def FileChooser():
    Tk.withdraw()
    File = filedialog.askopenfile(
        title = "Seleccione un archivo",
        initialdir = "/",
        filetypes = (
            ("Todos los Archivos", "*.*"),
            ("Archivos data", "*.data")
            ("Archivos lfp", "*.lfp")
        )
    )

    if File is None:
        print("No se selecciono un archivo\n")
        return None
    else:
        ContentFile = File.read()
        File.close()
        return ContentFile




















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

            if DataFile is not None:
                print(DataFile)
            else:
                print("no")
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
