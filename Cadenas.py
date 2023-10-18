#from app import ventana_principal
#import tkinter as tk
#Patron, lexema y token
#patron = Secuencia de numeros
#lexema = 123456789
#token = Numero
#consola = ventana_principal()
reserved = {
    'Rclaves'           : 'Claves',
    'Rclave_1'          : 'clave_1',
    'Rclave_2'          : 'clave_2',
    'Rclave_3'          : 'clave_3',
    'Rclave_4'          : 'clave_4',
    'Rclave_5'          : 'clave_5',
    'Rregistros'        : 'Registros',
    'Rvalor_1'          : 'valor_1',
    'Rvalor_2'          : 'valor_2',
    'Rvalor_3'          : 'valor_3',
    'Rvalor_4'          : 'valor_4',
    'Rvalor_5'          : 'valor_5',
    'Rcomentariol'      : '#',
    'Rcomentarioll'     : " ''' ",
    'Rllaveapertura'    : '{',
    'Rllavecierre'      : '}',
    'Rcorcheteapertura' : '[',
    'Rcorchetecierre'   : ']',
    'Rcoma'             : ',',
    'Rpuntoycoma'       : ';',
    'Rpunto'            : '.',
    'Rigual'            : '=',
    'Rcomillas'         : '"',
    'Rimprimir'         : 'imprimir',
    'Rimprimirln'       : 'imprimirln',
    'Rconteo'           : 'conteo',
    'Rpromedio '        : 'promedio',
    'Rcontarsi'         : 'contarsi',
    'Rdatos'            : 'datos',
    'Rsumar'            : 'sumar',
    'Rmaximo'           : 'max',
    'Rminimo'           : 'min',
    'Rexportarreporte'  : 'exportarReporte',
    }
lexemas = list(reserved.values())
global lista_lexemas



def Comentariol(cadena):
    lexemas = []  # Creamos una lista para almacenar los lexemas encontrados
    puntero = 0
    while puntero < len(cadena):
        char = cadena[puntero]
        puntero += 1
        if char == '#':
            lexema = Armar_Comentariol(cadena[puntero-1:])
            if lexema is not None:
                lexemas.append(lexema)
    return lexemas
def Armar_Comentariol(cadena):
    lexema = ''
    for char in cadena:
        if char == '\n':
            #consola.cuadroTexto2.insert(tk.END, lexema)
            return lexema
        lexema += char
    return None

entrada = """#hola
#adios
COMENTARIO MULTILINEA 
hola esto es parte del comentario
'''   
COMENTARIO MULTILINEA 
esto tambien es parte del comentario
'''
claves = ["codigo", "producto", "precio_compra", "precio_venta", "stock"]
Registros = [
    {1, "Barbacoa", 10.50, 20.00, 6}
    {2, "Salsa", 13.00, 16.00, 7}
    {3, "Mayonesa", 15.00, 18.00, 8}
    {4, "Mostaza", 14.00, 16.00, 4}
]
imprimir("Reporte de ");
imprimir("Abarroteria");
imprimirln("Reporte de ");
imprimirln("Abarroteria");
datos();
conteo();
    promedio("producto");
contarsi("stock", 0);
    sumar("stock");
    max("precio_venta");
    min("precio_compra");
exportarReporte("Reporte HTML de abarroteria");
"""
lexemas = Comentariol(entrada)
print(lexemas)
