from Abstract.Numero import *
from Abstract.Lexema import *
from Instrucciones.Texto import *
from Errores.Errores import *
promt = '>>>'
reserverd = {
    'Rclaves'           : 'claves',
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
    'Rparizq'           : '(',
    'Rparder'           : ')',
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

lexema = list(reserverd.values())
global n_linea
global n_columna
global instrucciones
global lista_lexemas

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []


def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0
    palabras_reservadas = ['Claves', 'imprimir', 'imprimirln', 'conteo', 'promedio', 'contarsi', 'datos', 'sumar',
                        'max', 'min', 'exportarReporte']
    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char == '"':       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna, 'TEXTO')
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("Claves"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'CLAVES')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0

        elif cadena.startswith("imprimir"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'IMPRIMIR')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("imprimirln"):
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna, 'IMPRIMIRLN')
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
            l = Lexema('(', n_linea, n_columna, 'PARIZQ')
            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                #! Armamos lexema como clase
                n = Numero(token, n_linea, n_columna)

                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0

        elif char == '[' or char == ']':
            # ! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna, 'CORCHETE')

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ';':

            c = Lexema(char, n_linea, n_columna, 'PUNTOYCOMA')

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == '=':
            c = Lexema(char, n_linea, n_columna, 'IGUAL')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ',':
            c = Lexema(char, n_linea, n_columna, 'COMA')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ')':
            c = Lexema(char, n_linea, n_columna, 'PARDER')
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == "\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        elif char == ' ' or char == '\r' or char == '.' or char == ':':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        else:
            lista_errores.append(Errores(char, "Léxico",n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

    return lista_lexemas


def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '"' or char == '\t' or char == '(' or char == ')':
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None

def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal =  False

    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True

        if char == ' ' or char == '\n' or char == '\t':
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            if char != ',': #! si no es una coma lo agregamos al numero
                numero += char
    return None, None

def Errores_Lexico():
    #llama a la lista de errores para obtener los datos y guardarlos en el archivo de salida
    global lista_errores
    formatoErrores = '{\n\t"errores":[\n'
    for i in range(len(lista_errores)):
        error = lista_errores[i]
        formatoErrores += error.operar(i+1)
        if i != len(lista_errores)-1:
            formatoErrores += ',\n'
        else:
            formatoErrores += '\n'
    formatoErrores += '\t]\n}'
    #retorna el formato de errores en el archivo de salida
    return print(formatoErrores)
