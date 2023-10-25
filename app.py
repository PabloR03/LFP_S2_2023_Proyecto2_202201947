import tkinter as tk
from tkinter import Menu, messagebox, filedialog, scrolledtext
from tkinter.filedialog import asksaveasfilename
from analizador_lexico import Lexico
from analizador_sintactico import analizador_s
import webbrowser

analizador_lexico=Lexico()
analizador_sintactico=analizador_s()
prompt = '>>>'

class ventana_principal:
    def __init__(self, root):
        #ruta de archivo a analizar_Archivo
        self.archivo_analizado=True

        #datos de ventana principal
        self.root = root
        self.root.title("Manejo de Inventario - 202201947")
        self.root.geometry("1440x820")
        self.root.resizable(0,0)
        #cuadro que contiene a los botones
        barra_de_opciones = tk.Frame(root, bg="dodgerblue4")
        barra_de_opciones.pack(pady=5)
        barra_de_opciones.pack_propagate()
        barra_de_opciones.configure(width=1440, height=60)

        # boton de Abrir Archivo
        boton_abrir=tk.Menubutton(barra_de_opciones,text="Abrir")
        boton_abrir.place(x=750, y=10, width=140, height=40)
            #op del menu
        opA=Menu(boton_abrir,tearoff=0)
        boton_abrir["menu"]=opA
        opA.add_command(label="Abrir Archivo", command=self.Abrir)
        opA.add_command(label="Guardar Archivo", command=self.Guardar)

        # boton de Analizar Archivo
        boton_guardar=tk.Button(barra_de_opciones,text="Analizar", command=self.Analizar)
        boton_guardar.place(x=940, y=10, width=140, height=40)

        #boton de menu (desplegable) para los Reportes
        boton_archivo=tk.Menubutton(barra_de_opciones, text="Reportes")        
        boton_archivo.place(x=1130, y=10, width=140, height=40)
            #op del menu
        op=Menu(boton_archivo,tearoff=0)
        boton_archivo["menu"]=op
        op.add_command(label="Reporte de Tokens", command=self.repTokens)
        op.add_command(label="Reporte de Errores", command=self.repErrores)
        op.add_command(label="Reporte de Arbol de Derivacion")

        # Cuadro de texto editable
        cuadrotexto_frame = tk.Frame(root, bg="dodgerblue")
        self.cuadroTexto = scrolledtext.ScrolledText(cuadrotexto_frame, bg="White", width=100, height=40)
        self.cuadroTexto.grid(row=10, column=10, sticky="w")  # Usar "w" para pegarlo a la izquierda
        cuadrotexto_frame.pack(pady=10, side="left")  # Usar "left" para colocarlo a la izquierda

        # Cuadro de texto no editable
        cuadrotexto_frame2 = tk.Frame(root, bg="dodgerblue1")
        self.cuadroTexto2 = scrolledtext.ScrolledText(cuadrotexto_frame2, bg="White", width=70, height=40)
        self.cuadroTexto2.grid(row=0, column=1, sticky="e")  # Usar "e" para pegarlo a la derecha
        cuadrotexto_frame2.pack(pady=10, side="right")  # Usar "left" para colocarlo a la izquierda

    #Def para buscar archivo tipo .bozdata y abrirlo
    def Abrir(self):
        self.archivo_analizado=True
        texto_archivo = ""
        ruta = tk.Tk()
        ruta.withdraw()
        ruta.attributes('-topmost', True)
        try:
            self.ruta_seleccionada= nueva_ruta = filedialog.askopenfilename(filetypes=[("Archivos BizData", f"*.bizdata")])
            with open(nueva_ruta, encoding="utf-8") as archivo_json:
                texto_archivo = archivo_json.read()
            self.texto = texto_archivo
            # Elimina contenido del textArea para cargar el archivo
            self.cuadroTexto.delete(1.0, "end")
            # Copia la informacion del contenido
            self.cuadroTexto.insert(1.0, self.texto)
            messagebox.showinfo("ABRIR ... ", "Archivo cargado, puede seguir editandolo en el panel de texto")
        except:
            messagebox.showerror("ERROR ... ", "Archivo no cargado, revise que haya seleccionado uno y que sea de tipo .bizdata")
            return  
    
    #Def para guardar archivo que esta en el panel de texto
    def Guardar(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.cuadroTexto.get(1.0, "end")
            archivo = open(self.ruta_seleccionada, 'w', encoding="utf-8")
            archivo.write(self.texto)
            
            messagebox.showinfo("GUARDADO ... ", "Cambios Guardados, puede seguir en el analizador")
        except:
            messagebox.showerror("ERROR ... ", "Archivo no Guardado, revise la entrada")
            return
    
    def reporte(self):
        try:
            if self.archivo_analizado==True:
                messagebox.showinfo("Reporte", "Reporte Creado Correctamente.")
            else:
                messagebox.showerror("Error", "No se ha realizado el análisis de archivo.")
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error.: {str(e)}")

    def Analizar(self):
        #try:
            codigo_fuente = self.cuadroTexto.get(1.0, tk.END)
            analizador_lexico.analizador_lexico(codigo_fuente)
            analizador_lexico.reporte_tokens()
            analizador_lexico.reporte_errores_lexicos()
            print("***LISTA DE LEXEMAS***")
            for lexema in analizador_lexico.lista_lexemas:
                print("-++++-")
                print(lexema.lexema)
            print("**************************************")
            analizador_sintactico.analizador_sintactico(analizador_lexico.lista_lexemas)

            self.cuadroTexto2.delete(1.0, "end")
            self.cuadroTexto2.insert(1.0, analizador_sintactico.texto_imprimir)

            messagebox.showinfo("Análisis exitoso", "El código se analizó exitosamente.")
        #except Exception:
            #messagebox.showerror("ERROR")

    def repErrores(self):
        # Abre el archivo HTML en Chrome
        webbrowser.open("Reportes\\202201947_rErroresLexico.html")
        
    def repTokens(self):
        # Abre el archivo HTML en Chrome
        webbrowser.open("Reportes\\202201947_rTokens.html")




if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()