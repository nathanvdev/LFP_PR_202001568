from tkinter import filedialog, Tk

def FileChooser():
    Tk().withdraw()
    Document = filedialog.askopenfile(
        title = "Elige el archivo",
        initialdir = "./",
    )

    if Document is None:
        print("No seleccionó correctamente el archivo\n")
        return None
    else:
        ContentFile = Document.read()
        Document.close
        return ContentFile


if __name__ == '__main__':
    while True:
        print("=============================\n"+
        "||1. Cargar Data           ||\n"+
        "||2. Cargar Instrucciones  ||\n"+
        "||3. Analizar              ||\n"+
        "||4. Reportes              ||\n"+
        "||5. Salir                 ||\n"+
        "=============================")
        Menu = input ('''============================="+
                        "||1. Cargar Data           ||
                        "||2. Cargar Instrucciones  ||
                        "||3. Analizar              ||
                        "||4. Reportes              ||
                        "||5. Salir                 ||
                        "=============================
                        Elige una opción:  ------->  ''')
        if Menu == '1':
            pass
        elif Menu == '2':
            pass
        elif Menu == '3':
            pass
        elif Menu == '4':
            pass
        elif Menu == '5':
            break
        else:
            print("Elija una opcion valida")




    # File = FileChooser()
    # if File is not None:
    #     print(File)
    # else:
    #     print("El archivo no es compatible\n")