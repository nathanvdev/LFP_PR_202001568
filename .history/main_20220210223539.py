from tkinter import filedialog, Tk

def FileChooser():
    Tk().whithdraw()
    Document = filedialog.askopenfile(
        title= "Elige el archivo",
        initialdir= "./",
        filetypes= (
            ("Archivos data", "*.data")
        )
    )

    if Document is None:
        print("No seleccionó correctamente el archivo\n")
        return None
    else:
        ContentFile = Document.read()
        Document.close
        return ContentFile


# print("=============================\n"+
#     "||1. Cargar Data           ||\n"+
#     "||2. Cargar Instrucciones  ||\n"+
#     "||3. Analizar              ||\n"+
#     "||4. Reportes              ||\n"+
#     "||5. Salir                 ||\n"+
#     "=============================")
# menu = input("Elige una opción:  ------->  ")
# print(menu)

# def PrincipalMenu(menu):
#     switcher = {
#         1:   "lasnkd",    
#         2:   "asd",
#         3:    "asdasd",          
#         4:     "sdasd",        
#         5:  "asfsd"
#     }
#     return switcher.get(menu, "default")



if __name__ == '__main__':
    File = FileChooser()
    if File is not None:
        print(File)
    else:
        print("El archivo no es compatible\n")