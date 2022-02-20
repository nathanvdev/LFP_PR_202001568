from os import startfile
from tkinter import filedialog, Tk
import matplotlib.pyplot as Plt
from Product import Product
from Instructions import Graphic
from PIL import Image
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from msilib.schema import Environment

Month_n = ''
Year_n = ''

GName = ''
Gtype = ''
Gtittle = ''
Xtittle = ''
Ytittle = ''

ProductsList = []
ListaGancia = []
Ventas = []



def FileChooser(Type):
    FileText = ''
    text = ''
    Tk().withdraw()
    try:
        # filename = 'F:/Bibliotecas/Documents/U/2022/Primer Semestre/Lab Lenguajes/Proyectos/LFP_PR_202001568/prueba1.data'
        # filename = 'F:/Bibliotecas/Documents/U/2022/Primer Semestre/Lab Lenguajes/Proyectos/LFP_PR_202001568/InstruccionesPrueba.lfp'
        filename = filedialog.askopenfilename(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos data', "*.{}".format(Type)),
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
            ContentDataFile = FileChooser('data')
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

            GName = ''
            Gtype = ''
            Gtittle = ''
            Xtittle = ''
            Ytittle = ''

            InstructionsData = FileChooser('lfp')
            Instructions = ''
            for Character in InstructionsData:
                if Character != '<' and Character != '¿'and Character != '?'and Character != '>' and Character != 'â':
                    Instructions += Character
            
            Instructions = Instructions.split(',')

            ZName = False
            ZGraphic = False
            ZTittle= False
            ZTittleX = False
            ZTittleY = False

            for g in Instructions:
                if not g.find('nombre') and not ZName:
                    print(g)
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
                    Ytittle = tmp[1]
                    ZTittleY = True

        elif Menu == '3':
            Plt.close()
            GraphicX = []
            GraphicY = []


            for P in ProductsList:
                Profit = P.getPrice()*P.getQuant()
                Profit = round(Profit, 2)
                GraphicX.append(P.getName())
                GraphicY.append(Profit)

            if Gtype == 'barras':

                print(GraphicX)
                print(GraphicY)
                print('-Titulo: ', GName, ' -x ', Xtittle, ' -y ',Ytittle)
                Plt.bar(GraphicX, GraphicY)
                Plt.title(GName.upper())
                Plt.xlabel(Xtittle.upper())
                Plt.ylabel(Ytittle.upper())
                Plt.savefig('./{}.png'.format(GName+'-'+Gtype))
                print(GName+'-'+Gtype)
                imgLinea = Image.open('./{}.png'.format(GName+'-'+Gtype))
                imgLinea.show()

            elif Gtype == 'pie':

                print(GraphicX)
                print(GraphicY)
                print('-Titulo: ', GName, ' -x ', Xtittle, ' -y ',Ytittle)
                Plt.pie(GraphicY ,labels=GraphicX, autopct='%0.1f%%', pctdistance=0.8, shadow=True, startangle=90, rotatelabels=False)
                Plt.title(GName.upper())
                Plt.xlabel(str(Xtittle).upper(), labelpad=20)
                Plt.ylabel(Ytittle.upper(), labelpad=80)
                Plt.savefig('./{}.png'.format(GName+'-'+Gtype))
                imgLinea = Image.open('./{}.png'.format(GName+'-'+Gtype))
                imgLinea.show()
                

            elif Gtype == 'lã ­neas' or 'lineas':
                print(GraphicX)
                print(GraphicY)
                print('-Titulo: ', GName, ' -x ', Xtittle, ' -y ',Ytittle)
                Plt.plot(GraphicX,GraphicY)
                Plt.title(GName.upper())
                Plt.xlabel(Xtittle.upper())
                Plt.ylabel(Ytittle.upper())
                Plt.savefig('./{}.png'.format(GName+'-'+Gtype))
                imgLinea = Image.open('./{}.png'.format(GName+'-'+Gtype))
                imgLinea.show()

            else:
                print('Por favor indica el tipo de grafica que deseas')




        elif Menu == '4':
            
            ListaGancia = ProductsList.copy()
            Ventas = ProductsList.copy()
         
            for i in range(len(ListaGancia)-1):
                for j in range(len(ListaGancia)-1):
                    if ListaGancia[j].getGanancia() < ListaGancia[j+1].getGanancia():
                        xw = ListaGancia[j]
                        ListaGancia[j] = ListaGancia[j+1]
                        ListaGancia[j+1] = xw
            
            for ii in range(len(Ventas)-1):
                for jj in range(len(Ventas)-1):
                    if Ventas[jj].getQuant() < Ventas[jj+1].getQuant():
                        xww = Ventas[jj]
                        Ventas[jj] = Ventas[jj+1]
                        Ventas[jj+1] = xww

            for p in ListaGancia:
                print(p.getGanancia())
            print('--------')
            MasVendido = Ventas[0].getName()
            MenosVendido = Ventas[len(Ventas)-1].getName()
            print(MasVendido)
            print(MenosVendido)

            cacapopo = Environment(loader=FileSystemLoader('./'), autoescape = select_autoescape(['html']))
            
            template = cacapopo.get_template('plantilla.html')

            html_file = open('index.html', 'w+', encoding='utf-8')
            html_file.write(template.render(Ventas = Ventas))
            html_file.close()

            startfile('index.html')

        elif Menu == '5':
            print('\nGracias por utilizar este programa')
            break
        else:
            print("Elija una opcion valida")
