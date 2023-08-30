
from ACP import ACP
from Bigote import Bigote
from correlation import Correlation
import sys

def main():
    op = '-1'

    try:
        file = sys.argv[1]
    except IndexError:
        print('Debe ingresar el nombre del archivo csv como argumento')
        exit()

    while op != '0':
        print('\t\t\t Menu ')
        print('1.- Caja bigote')
        print('2.- Correlacion')
        print('3.- PCA')
        print('4.- Cambiar archivo')
        print('0.- Salir')

        op = input('Ingrese una opcion: ')

        if op == '1':
            Bigote(file)
        elif op == '2':
            Correlation(file)
        elif op == '3':
            ACP(file)
        elif op == '0':
            print('Saliendo...')
        elif op == '4':
            file = input('Ingrese el nombre del archivo sin extension csv: ')
            try:
                with open(f'{file}.csv','r') as f:
                    pass
            except FileNotFoundError:
                print('El archivo csv no existe')
                exit()
        else:
            print('Opcion invalida')



if __name__ == __name__:
    main()
