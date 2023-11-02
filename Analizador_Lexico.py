from Objetos.Lexema import Lexema
from Objetos.Error import Error
import os

class Lexico:

    def __init__(self):
        self.lista_lexemas = []
        self.lista_errores = []
        self.n_linea = 1
        self.n_columna = 1

    def analizador_lexico(self, cadena):
        lexema = ''
        puntero = 0

        while cadena:
            char = cadena[puntero]
            puntero += 1

            if char == '"':       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
                l = Lexema('"', self.n_linea, self.n_columna, 'COMILLA')
                self.lista_lexemas.append(l)
                lexema, cadena = self.armar_cadena(cadena[puntero:])
                if lexema and cadena:
                    self.n_columna += 1
                    #Armar lexema como clase
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'TEXTO')
                    self.lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('"', self.n_linea, self.n_columna, 'COMILLA')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif char == "'":       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
                l = Lexema("'", self.n_linea, self.n_columna, 'COMILLA_SIMPLE')
                self.lista_lexemas.append(l)
                lexema, cadena = self.armar_comentario(cadena[puntero:])
                if lexema and cadena:
                    self.n_columna += 1
                    #Armar lexema como clase
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'TEXTO')
                    self.lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema("'", self.n_linea, self.n_columna, 'COMILLA_SIMPLE')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("#"):
                lexema, cadena = self.armar_cadena(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'COMENTARIO 1 LINEA')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0

            elif cadena.startswith("Claves"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'CLAVES')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0

            elif cadena.startswith("Registros"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'REGISTROS')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0

            elif cadena.startswith("imprimirln"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'IMPRIMIRLN')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("imprimir"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'IMPRIMIR')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("conteo"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'CONTEO')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("promedio"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'PROMEDIO')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("contarsi"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'CONTARSI')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("datos"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'DATOS')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("sumar"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'SUMAR')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0
            
            elif cadena.startswith("max"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'MAX')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("min"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'MIN')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif cadena.startswith("exportarReporte"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    l = Lexema(lexema, self.n_linea, self.n_columna, 'EXPORTAR_REPORTE')
                    self.lista_lexemas.append(l)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                l = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS_IZQUIERDO')
                self.lista_lexemas.append(l)
                self.n_columna += 1
                puntero = 0

            elif char.isdigit():
                token, cadena = self.armar_numero(cadena)
                if token is not None and cadena:
                    self.n_columna += 1
                    #! Armamos lexema como clase
                    if token == 0:
                        tipo_lexema = "ENTERO"  # Si el token es 0, considerarlo como un número entero
                    else:
                        tipo_lexema = "NUMERO"
                    n = Lexema(token, self.n_linea, self.n_columna, tipo_lexema)

                    self.lista_lexemas.append(n)
                    self.n_columna += len(str(token)) + 1
                    puntero = 0


            elif char == '[' or char == ']':
                # ! Armamos lexema como clase
                c = Lexema(char, self.n_linea, self.n_columna, 'CORCHETES')
                self.lista_lexemas.append(c)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            

            elif char == '{' or char == '}':
                # ! Armamos lexema como clase
                c = Lexema(char, self.n_linea, self.n_columna, 'LLAVES')

                self.lista_lexemas.append(c)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1

            elif char == ';':
                c = Lexema(char, self.n_linea, self.n_columna, 'PUNTO_Y_COMA')
                self.lista_lexemas.append(c)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1

            elif char == '=':
                c = Lexema(char, self.n_linea, self.n_columna, 'IGUAL')
                self.lista_lexemas.append(c)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1

            elif char == ',':
                c = Lexema(char, self.n_linea, self.n_columna, 'COMA')
                self.lista_lexemas.append(c)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1

            elif char == ')':
                c = Lexema(char, self.n_linea, self.n_columna, 'PARENTESIS_DERECHO')
                self.lista_lexemas.append(c)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1

            elif char == "\t":
                self.n_columna += 4
                cadena = cadena[4:]
                puntero = 0

            elif char == "\n":
                cadena = cadena[1:]
                puntero = 0
                self.n_linea += 1
                self.n_columna = 1

            elif char == ' ' or char == '\r':
                self.n_columna += 1
                cadena = cadena[1:]
                puntero = 0

            else:
                self.lista_errores.append(Error(char, "Léxico",self.n_linea, self.n_columna))
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1

    def armar_lexema(self, cadena):
        lexema = ''
        puntero = ''
        for char in cadena:
            puntero += char
            if char == '"' or char == '\n' or char == '\t' or char == '(' or char == ')' or char == ' ':
                return lexema, cadena[len(puntero):]   
            else:
                lexema += char
        return None, None

    def armar_cadena(self, cadena):
        lexema = ''
        puntero = ''
        for char in cadena:
            puntero += char
            if char == '"' or char == '\n':
                return lexema, cadena[len(puntero):]   
            else:
                lexema += char
        return None, None

    def armar_comentario(self, cadena):
        lexema = ''
        puntero = ''
        for char in cadena:
            puntero += char
            if char == "'":
                return lexema, cadena[len(puntero):]   
            else:
                lexema += char
        return None, None

    def armar_numero(self, cadena):
        numero = ''
        puntero = ''
        is_decimal =  False
        for char in cadena:
            puntero += char
            if char == '.':
                is_decimal = True
            if char=="," or char==")" or char == ' ' or char == '\n' or char == '\t' or char=="}":
                if is_decimal:
                    return float(numero), cadena[len(puntero)-1:]
                else:
                    return int(numero), cadena[len(puntero)-1:]
            elif char != ',' or char != ')':
                    numero += char
        return None, None

    def reporte_tokens(self):
        nombre_archivo = "REportes/202201947_rTokens.html"
        # Generar la tabla HTML
        tabla_html = """
        <table>
            <tr>
                <th>Lexema</th>
                <th>Token</th>
                <th>Fila</th>
                <th>Columna</th>
            </tr>
            """
        for lexema_obj in self.lista_lexemas:
            fila_html = f"""
            <tr>
                <td>{lexema_obj.lexema}</td>
                <td>{lexema_obj.tipo}</td>
                <td>{lexema_obj.fila}</td>
                <td>{lexema_obj.columna}</td>
            </tr>"""
            tabla_html += fila_html
        tabla_html += "</table>"
        html = f"""<!DOCTYPE html>
                    <html>
                    <head>
                        <title>Reporte De Tokens</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                background-color: #fff;
                            }}
                            .tabla-container {{
                                text-align: center;
                                margin: 20px auto;
                                width: 80%;
                            }}
                            .tabla-container table {{
                                width: 100%;
                                border-collapse: collapse;
                            }}
                            .tabla-container th, .tabla-container td {{
                                padding: 8px 12px;
                                border: 1px solid #444;
                            }}
                            .tabla-container th {{
                                background-color: #333;
                                color: white;
                            }}
                            .tabla-container tr:nth-child(even) {{
                                background-color: #f2f2f2;
                            }}
                            .tabla-container tr:nth-child(odd) {{
                                background-color: #fff;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1 style="text-align:center">Reporte De Tokens</h1>
                        <div class="tabla-container">
                            {tabla_html}
                        </div>
                    </body>
                    </html>"""
        with open(nombre_archivo, "w") as archivo:
            archivo.write(html)

    def reporte_errores_lexicos(self):
        nombre_archivo = "Reportes/202201947_rErroresLexico.html"
        # Generar la tabla HTML
        tabla_html = """
        <table>
            <tr>
                <th>Token</th>
                <th>Tipo Error</th>
                <th>Fila</th>
                <th>Columna</th>
            </tr>
            """
        for error in self.lista_errores:
            fila_html = f"""
            <tr>
                <td>{error.error}</td>
                <td>{error.tipo}</td>
                <td>{error.fila}</td>
                <td>{error.columna}</td>
            </tr>"""
            tabla_html += fila_html
        tabla_html += "</table>"
        html = f"""<!DOCTYPE html>
                    <html>
                    <head>
                        <title>Reporte De Errores</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                background-color: #f2f2f2;
                            }}
                            .tabla-container {{
                                text-align: center;
                                margin: 20px auto;
                                width: 80%;
                            }}
                            .tabla-container table {{
                                width: 100%;
                                border-collapse: collapse;
                            }}
                            .tabla-container th, .tabla-container td {{
                                padding: 8px 12px;
                                border: 1px solid #444;
                            }}
                            .tabla-container th {{
                                background-color: #333;
                                color: white;
                            }}
                            .tabla-container tr:nth-child(even) {{
                                background-color: #f2f2f2;
                            }}
                            .tabla-container tr:nth-child(odd) {{
                                background-color: #fff;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1 style="text-align:center">Reporte de Errores Lexico</h1>
                        <div class="tabla-container">
                            {tabla_html}
                        </div>
                    </body>
                    </html>"""
        with open(nombre_archivo, "w") as archivo:
            archivo.write(html)

    def grafica_arbol_derivación(self):
        try:
            # Tu código para generar el archivo DOT
            lista_lexema = self.lista_lexemas.copy()
            nombre_archivo = "Reportes/Reporte_Arbol_de_Derivacion"
            f = open(nombre_archivo + '.dot', 'w')
            texto_g = """
                graph "" {
                    subgraph cluster_0 {
                        label="Prueba"
                    }"""
            contador_subgrafo=1
            contador_nodo=1
            while lista_lexema:
                lexema = lista_lexema.pop(0)
                if lexema.lexema == "imprimir" or  lexema.lexema == "imprimirln" or  lexema.lexema == "conteo" or  lexema.lexema == "promedio" or  lexema.lexema == "contarsi" or lexema.lexema == "datos" or lexema.lexema == "sumar" or  lexema.lexema == "max" or  lexema.lexema == "min" or  lexema.lexema == "exportarReporte":
                    texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{\n"""
                    nodo_actual = lexema.lexema
                    contador_actual=contador_nodo
                    contador_nodo+=1
                    texto_g += """n00"""+str(contador_actual)+"""[label="""+f'"'+nodo_actual+f'"'+"""];\n"""
                    while lista_lexema:
                        lex = lista_lexema[0]
                        if lex.lexema == ';':
                            texto_g += """n00"""+str(contador_nodo)+""" [label="""+f'"'+str(lex.lexema)+f'"'+"""];\n"""
                            texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                            break
                        if lex.lexema !='"':
                            texto_g += """n00"""+str(contador_nodo)+""" [label="""+f'"'+str(lex.lexema)+f'"'+"""];\n"""
                            texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                            contador_nodo+=1
                        else:
                            texto_g += """n00"""+str(contador_nodo)+""" [label="""+f'"'+"``"+f'"'+"""];\n"""
                            texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                            contador_nodo+=1
                        lista_lexema.pop(0)
                    texto_g += """\n}"""
                    contador_subgrafo+=1
                    contador_nodo+=1
            texto_g += """\n}"""
            f.write(texto_g)
            f.close()
            os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
            os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
            # Luego, intenta convertir el archivo DOT a PDF
            os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
            print("Archivo PDF generado exitosamente.")
        except Exception as e:
            print(f"Error al generar el archivo PDF: {str(e)}")
