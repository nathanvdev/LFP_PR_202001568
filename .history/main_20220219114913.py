from tkinter import filedialog, Tk
import matplotlib.pyplot as Plt
from Product import Product
from Instructions import Graphic
# from PIL import Image

Month_n = ''
Year_n = ''

GName = ''
Gtype = ''
Gtittle = ''
Xtittle = ''
Ytittle = ''

ProductsList = []


def FileChooser():
    FileText = ''
    text = ''
    Tk().withdraw()
    try:
        # filename = 'F:/Bibliotecas/Documents/U/2022/Primer Semestre/Lab Lenguajes/Proyectos/LFP_PR_202001568/prueba1.data'
        # filename = 'F:/Bibliotecas/Documents/U/2022/Primer Semestre/Lab Lenguajes/Proyectos/LFP_PR_202001568/InstruccionesPrueba.lfp'
        filename = filedialog.askopenfilename(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos data', '*.data'),
                         ('Archivos lfp', '*.lfp'),
                         ('Todos los archivos', '*.*'))
        )
        print(filename)
        with open(filename) as infile:
                FileText = infile.read().strip()
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

            ZName = False
            ZGraphic = False
            ZTittle= False
            ZTittleX = False
            ZTittleY = False

            

            

            for g in Instructions:
                if not g.find('nombre') and not ZName:
                    tmp = g.split(":")
                    GName = tmp[1]
                    ZName = True

                if not g.find('grafica') and not ZGraphic:
                    tmp = g.split(":")
                    print('--grafica ' , tmp[1])
                    Gtype = tmp[1]
                    ZGraphic = True

                if not g.find('titulo') and not ZTittle:
                    tmp = g.split(":")
                    print('--titulo ',tmp[1])
                    Gtittle = tmp[1]
                    ZTittle = True

                if not g.find('titulox') and not ZTittleX:
                    tmp = g.split(":")
                    print('--titulox ',tmp[1])
                    Xtittle =tmp[1]
                    ZTittleX = True

                if not g.find('tituloy') and not ZTittleY:
                    tmp = g.split(":")
                    print('--tituloy ',tmp[1])
                    Ytittle =tmp[1]
                    ZTittleY = True

        elif Menu == '3':
            print(ProductsList)





        elif Menu == '4':
            pass
        elif Menu == '5':
            print('\nGracias por utilizar este programa')
            break
        else:
            print("Elija una opcion valida")
