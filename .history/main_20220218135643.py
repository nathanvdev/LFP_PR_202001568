from tkinter import filedialog, Tk

from Product import Product

Month_n = ''
Year_n = ''
ProductsList = []

def FileChooser():
    FileText = ''
    text = ''
    Tk().withdraw()
    try:
        # filename = 'F:/Bibliotecas/Documents/U/2022/Primer Semestre/Lab Lenguajes/Proyectos/LFP_PR_202001568/prueba1.data'
        filename = 'F:/Bibliotecas/Documents/U/2022/Primer Semestre/Lab Lenguajes/Proyectos/LFP_PR_202001568/InstruccionesPrueba.lfp'
        # filename = filedialog.askopenfilename(
        #     initialdir = './',
        #     title = 'Selecciona un archivo',
        #     filetypes = (('Archivos data', '*.data'),
        #                  ('Archivos lfp', '*.lfp'),
        #                  ('Todos los archivos', '*.*'))
        # )
        # print(filename)
        with open(filename) as infile:
                FileText = infile.read().strip()
                FileText = FileText.lower()

        for chartacter in FileText:
            if chartacter != '\"':
                if (chartacter != ' ' and chartacter != '\n' and chartacter != '\t'):
                    text += chartacter
        print(str(text))
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
            Month = False
            Year = False
            Parenth = False
            DataProducts = ''

            for Character in ContentDataFile:

                if Character == ':':
                    Month = True
                if Character == '=':
                    Year = True
                if Character == '(':
                    Parenth = True
                if Character == ')':
                    break

                if not Month:
                    Month_n += Character
                if Month and not Year and Character != ':':
                    Year_n += Character
                if Parenth and Character != '(' and Character !='[' and Character != ']':
                    DataProducts += Character
                    
            
            DataProducts = DataProducts.split(';')
            DataProducts.pop()

            for Prroduct in DataProducts:
                tmpProduct = Prroduct.split(',')
                name = tmpProduct[0]
                price = tmpProduct[1]
                quant = tmpProduct[2]
                ProductsList.append(Product(name, price, quant))

            for P in ProductsList:
                P.presentProduct()

        elif Menu == '2':
            InstructionsData = FileChooser()
            Instructions = ''
            for Character in InstructionsData:
                if Character != '<' and Character != '¿'and Character != '?'and Character != '>' and Character != 'â':
                    Instructions += Character
            Instructions = Instructions.split(',')
            print(Instructions)
            x = Instructions[0].find('nombre')
            print(Instructions[x])

            print(x)




        elif Menu == '3':
            pass
        elif Menu == '4':
            pass
        elif Menu == '5':
            print('\nGracias por utilizar este programa')
            break
        else:
            print("Elija una opcion valida")
