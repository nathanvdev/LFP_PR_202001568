
print("=============================\n"+
    "||1. Cargar Data           ||\n"+
    "||2. Cargar Instrucciones  ||\n"+
    "||3. Analizar              ||\n"+
    "||4. Reportes              ||\n"+
    "||5. Salir                 ||\n"+
    "=============================")
menu = input("Elige una opción:  ------->  ")
print(menu)

def PrincipalMenu(menu):
    switcher = {
        1:   "lasnkd",    
        2:   "asd",
        3:    "asdasd",          
        4:     "sdasd",        
        5:  "asfsd"
    }
    return switcher.get()