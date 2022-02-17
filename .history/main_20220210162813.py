print("=============================\n"+
      "||1. Cargar Data           ||\n"+
      "||2. Cargar Instrucciones  ||\n"+
      "||3. Analizar              ||\n"+
      "||4. Reportes              ||\n"+
      "||5. Salir                 ||\n"+
      "=============================")

print("Elige una opción:  ------->", end='')
menu=input()


def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")
 
# Driver program
if __name__ == "__main__":
    argument=0
    print (numbers_to_strings(argument))