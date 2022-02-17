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

  

    print("=============================\n"+
    "||1. Cargar Data           ||\n"+
    "||2. Cargar Instrucciones  ||\n"+
    "||3. Analizar              ||\n"+
    "||4. Reportes              ||\n"+
    "||5. Salir                 ||\n"+
    "=============================")
    menu = input ("Elige una opción:  ------->  ")
    print(menu)



    # File = FileChooser()
    # if File is not None:
    #     print(File)
    # else:
    #     print("El archivo no es compatible\n")