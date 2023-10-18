import tkinter as tk

class Procesar:
    def __init__(self):
        pass

    def procesar_comentarios(self, cuadroTexto, cuadroTexto2):
        contenido_scrolltext1 = cuadroTexto.get("1.0", "end-1c")  # Obtiene el contenido del primer ScrollText

        lines = contenido_scrolltext1.split('\n')  # Divide el contenido en líneas
        comentario_activo = False
        comentario = ""

        for linea in lines:
            if comentario_activo:
                if linea.startswith("#"):
                    comentario += linea + "\n"
                else:
                    cuadroTexto2.insert(tk.END, comentario)
                    comentario_activo = False
                    comentario = ""
            elif linea.startswith("#COMENTARIO"):
                comentario = linea + "\n"
                comentario_activo = True

        # Si hay un comentario activo al final del contenido
        if comentario_activo:
            cuadroTexto2.insert(tk.END, comentario)

    def procesar_comentarios_multi(self, cuadroTexto, cuadroTexto2):
        contenido_scrolltext1 = cuadroTexto.get("1.0", "end-1c")  # Obtiene el contenido del primer ScrollText

        lineas = contenido_scrolltext1.split('\n')  # Divide el contenido en líneas
        comentario_activo = False
        comentario = ""

        for linea in lineas:
            if comentario_activo:
                if linea.strip().startswith('"""') or linea.strip().startswith("'''"):
                    # Comentario multilinea encontrado, finaliza el comentario
                    cuadroTexto2.insert(tk.END, comentario)
                    comentario_activo = False
                    comentario = ""
                else:
                    comentario += linea + "\n"
            elif linea.strip().startswith("#"):
                comentario = linea + "\n"
                comentario_activo = True
            else:
                cuadroTexto2.insert(tk.END, linea + "\n")
        cuadroTexto2.insert(tk.END, comentario)  # Si hay un comentario activo al final

