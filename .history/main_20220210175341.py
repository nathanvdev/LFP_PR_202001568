
pop = True
while pop == True:

    print("=============================\n"+
        "||1. Cargar Data           ||\n"+
        "||2. Cargar Instrucciones  ||\n"+
        "||3. Analizar              ||\n"+
        "||4. Reportes              ||\n"+
        "||5. Salir                 ||\n"+
        "=============================")

    menu = input("Elige una opción:  -------> ")

    if menu == 1:
        print("escogiste cargar data")
    if menu == 5:
        pop == False

