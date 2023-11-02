from Objetos.Error import Error
#importar para crear una ventana emergente
from tkinter import Menu, messagebox, filedialog, scrolledtext
def promedio_clave(lista_clave, lista_registro, clave):
    if clave not in lista_clave:
        return None

    indice_clave = lista_clave.index(clave)
    valores_clave = [float(registro[indice_clave]) for registro in lista_registro if isinstance(registro[indice_clave], (int, float))]

    if not valores_clave:
        return 0

    promedio = sum(valores_clave) / len(valores_clave)
    return promedio


def contarsi_clave(lista_clave, lista_registro, clave, valor):
    if clave not in lista_clave:
        return None  # La clave no está en lista_clave
    indice_clave = lista_clave.index(clave)
    contador = 0
    valor_float = float(valor)  # Convierte el valor a float

    for registro in lista_registro:
        if (len(registro) > indice_clave and 
            isinstance(registro[indice_clave], (int, float)) and 
            float(registro[indice_clave]) == valor_float):
            contador += 1

    return contador


def datos_consola(lista_clave, lista_registro):
    texto=""
    for registro in lista_registro:
        registro_formateado = ', '.join(f'{clave}: {valor}' for clave, valor in zip(lista_clave, registro))
        texto=texto+registro_formateado+"\n"
    return texto

def sumar_clave(lista_clave, lista_registro, clave):
    if clave not in lista_clave:
        return None

    indice_clave = lista_clave.index(clave)
    valores_clave = [float(registro[indice_clave]) for registro in lista_registro if isinstance(registro[indice_clave], (int, float))]

    if not valores_clave:
        return 0

    suma = sum(valores_clave)
    return suma



def maximo_clave(lista_clave, lista_registro, clave):
    if clave not in lista_clave:
        return None  # La clave no está en la lista_clave
    indice_clave = lista_clave.index(clave)
    valores_clave = [float(registro[indice_clave]) for registro in lista_registro if isinstance(registro[indice_clave], (int, float))]
    if not valores_clave:
        return None  # No hay valores válidos para calcular el máximo
    maximo = max(valores_clave)
    return maximo


def minimo_clave(lista_clave, lista_registro, clave):
    if clave not in lista_clave:
        return None  # La clave no está en la lista_clave
    indice_clave = lista_clave.index(clave)
    valores_clave = [float(registro[indice_clave]) for registro in lista_registro if isinstance(registro[indice_clave], (int, float))]
    if not valores_clave:
        return None  # No hay valores válidos para calcular el mínimo
    minimo = min(valores_clave)
    return minimo

def exportar_reporte(titulo, lista_clave, lista_registro):
    nombre_archivo = "Reportes/202201947_rConsola.html"
    html = f"""<!DOCTYPE html>
                <html>
                <head>
                    <title>{titulo}</title>
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
                    <h1 style="text-align:center">{titulo}</h1>
                    <div class="tabla-container">
                        <table>
                            <tr>
                                <!-- Encabezados de la tabla -->
                                {"".join(f"<th>{clave}</th>" for clave in lista_clave)}
                            </tr>
                            {"".join("<tr>" + "".join(f"<td>{valor}</td>" for valor in registro) + "</tr>" for registro in lista_registro)}
                        </table>
                    </div>
                </body>
                </html>"""
    with open(nombre_archivo, "w") as archivo:
        archivo.write(html)


class analizador_s:
    def __init__(self):
        self.lista_clave = []
        self.lista_registro = []
        self.lista_error_sintactico = []
        self.texto_imprimir=""
        self.n_linea = 1
        self.n_columna = 1

    def analizador_sintactico(self, lista_lexemas):
        while lista_lexemas:
            lexema = lista_lexemas.pop(0)
            
            if lexema.lexema == 'Claves':
                igual = lista_lexemas.pop(0)
                if igual.lexema == '=':
                    corchete_izq = lista_lexemas.pop(0)
                    if corchete_izq.lexema == '[':
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            if lex.lexema == '"':
                                continue
                            elif lex.lexema == ',':
                                continue
                            elif lex.lexema == ']':
                                print("Análisis Clave Completado")
                                break
                            else:
                                self.lista_clave.append(lex.lexema)
                    #else: 
                        #print("Error sintáctico en la declaración de claves se esperaba un '['")
                        #self.lista_error_sintactico.append(Error("[", "Sintáctico", self.n_linea, self.n_columna))
                        #self.reporte_errores_sintacticos()
                        #break
                #else: #! para detectar errores sintácticos
                    #messagebox.showinfo("Error Sintactico", "Error sintáctico en la declaración de claves se esperaba un '='")
                    #print("Error sintáctico en la declaración de claves se esperaba un '='")
                    #.lista_error_sintactico.append(Error("=", "Sintáctico", self.n_linea, self.n_columna))
                    #self.reporte_errores_sintacticos()
                    #break
            #else: 
                #print("Error sintáctico en la declaración de claves se esperaba un 'Claves'")
                #self.lista_error_sintactico.append(Error("Claves", "Sintáctico", self.n_linea, self.n_columna))
                #self.reporte_errores_sintacticos()
                #break

            if lexema.lexema == 'Registros':
                igual = lista_lexemas.pop(0)
                if igual.lexema == '=':
                    corchete_izq = lista_lexemas.pop(0)
                    if corchete_izq.lexema == '[':
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            if lex.lexema == ']':
                                print("Análisis Registro Completado")
                                break  # Terminar cuando se encuentra ']'
                            elif lex.lexema == '{':
                                nuevo_registro = []
                                while lista_lexemas:
                                    lex = lista_lexemas.pop(0)
                                    if lex.lexema == '"':
                                        continue
                                    elif lex.lexema == ',':
                                        continue
                                    elif lex.lexema == '}':
                                        self.lista_registro.append(nuevo_registro)
                                        break  # Terminar cuando se encuentra '}'
                                    else:
                                        nuevo_registro.append(lex.lexema)

            if lexema.lexema == 'imprimirln':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    print("Análisis imprimirln Completado")
                                    self.texto_imprimir+=texto.lexema

            if lexema.lexema == 'conteo':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    parentesis = lista_lexemas.pop(0)
                    if parentesis.lexema == ')':
                        punto_coma = lista_lexemas.pop(0)
                        if punto_coma.lexema == ';':
                            print("Análisis Conteo Completado")
                            conteo=len(self.lista_registro)
                            self.texto_imprimir+=str(conteo)

            if lexema.lexema == 'datos':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    parentesis = lista_lexemas.pop(0)
                    if parentesis.lexema == ')':
                        punto_coma = lista_lexemas.pop(0)
                        if punto_coma.lexema == ';':
                            print("Análisis datos Completado")
                            datos=datos_consola(self.lista_clave, self.lista_registro)
                            self.texto_imprimir+=datos

            if lexema.lexema == 'promedio':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    promedio=promedio_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if promedio is None:
                                        print("No Existe el campo: "+ texto.lexema)
                                    else:
                                        self.texto_imprimir+=str(promedio)

            if lexema.lexema == 'contarsi':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            coma=lista_lexemas.pop(0)
                            if coma.lexema==",":
                                numero=lista_lexemas.pop(0)
                                parentesis = lista_lexemas.pop(0)
                                if parentesis.lexema == ')':
                                    punto_coma = lista_lexemas.pop(0)
                                    if punto_coma.lexema == ';':
                                        contador=contarsi_clave(self.lista_clave, self.lista_registro, texto.lexema, numero.lexema)
                                        if contador is None:
                                            print("No Existe el campo: "+ texto.lexema)
                                        else:
                                            self.texto_imprimir+=str(contador)

            if lexema.lexema == 'sumar':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    suma=sumar_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if suma is None:
                                        print("No Existe el campo: "+ texto.lexema)
                                    else:
                                        self.texto_imprimir+=str(suma)

            if lexema.lexema == 'max':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    max=maximo_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if max is None:
                                        print("No Existe el campo: "+ texto.lexema)
                                    else:
                                        self.texto_imprimir+=str(max)

            if lexema.lexema == 'min':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    min=minimo_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if min is None:
                                        print("No Existe el campo: "+ texto.lexema)
                                    else:
                                        self.texto_imprimir+=str(min)

            if lexema.lexema == 'exportarReporte':
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    print("Análisis reporte Completado")
                                    exportar_reporte(texto.lexema, self.lista_clave, self.lista_registro)

            if lexema.lexema == 'imprimir':
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    print("Análisis imprimir Completado")
                                    self.texto_imprimir+=texto.lexema
    
    def reporte_errores_sintacticos(self):
        nombre_archivo = "Reportes/202201947_rErroresSintacticos.html"
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
        for error in self.lista_error_sintactico:
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
                        <title>Reporte De Errores Sintacticos</title>
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
                        <h1 style="text-align:center">Reporte de Errores Sintactico</h1>
                        <div class="tabla-container">
                            {tabla_html}
                        </div>
                    </body>
                    </html>"""

        with open(nombre_archivo, "w") as archivo:
            archivo.write(html)

