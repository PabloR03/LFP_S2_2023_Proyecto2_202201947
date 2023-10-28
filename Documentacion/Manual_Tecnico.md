# LENGUAJES FORMALES DE PROGRAMACION B-
## Proyecto 2
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Pablo Andres Rodriguez Lima
Carne: 202201947
Correo: pabloa10rodriguez@gmail.com
```
---
## Descripción del Proyecto
Presentacion de programa para el manejo de archivos del tipo bizdata, bajo una interfaz grafica, para realizar operaciones en forma de arbol, pero con la principal funcion de detectar errores lexicos, tomando en cuenta que las palabras reservadas son palabras basicas que tambien tienen opciones de configurar al reporte
Requerimientos mínimos para el uso del programa
Python en su versión 2.8 o posteriores (se creó bajo la versión 3.11.4), Se recomienda un ide como Pycharm o bien un editor de texto con su extensión como Visual Studio Code. tambien tener instalada una version de Graphviz.


## Objetivos
* Objetivo General
    * Desarrollar y presentar un programa de software integral que permite usar una interfaz grafica para abrir, guardar y revisar errores lexicos asi como sus reportes.
* Objetivos Específicos
    * Crear una interfaz de usuario intuitiva y de fácil uso que posibilite editar texto para analizar.
    * Implementar un sistema de de operaciones del tipo iterativas para hacer arboles.

---

# Gramatica para realizar el AFD [Ver metodo del Arbol](https://github.com/PabloR03/LFP_S2_2023_Proyecto2_202201947/blob/main/Docs/AFD.xlsx)

	Claves = ["",""]
ER: reg = [ ({ ((Cr+)|(" Cr +") , )+ })+ ]
Terminales = {'Claves', igual, coriz, corder, comillas, coma, caracter}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/MZctWFM/5claves.png)

	Registros = [{,"",}{,"",}]
ER: reg = [ ({ ((Cr+)|(" Cr +") , )+ })+ ]
Terminales = {'Registros', igual, coriz, corder, llaiz, llader, comillas, coma, caracter}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10}
Inicio = {q0}

![Imagen 2](https://i.ibb.co/S5PZT71/5registros.png)

	#Comentario
ER: '#' Cr+
Terminales = {#,caracter}
No Terminales = {q0, q1, q2}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/x55Zhsd/5comentariounl.png)

	'''
ER: ' ' ' (Cr | \n )+ ' ' '
Terminales = {',caracter, '\n'}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/6Z4bm7H/5comentariovarli.png)

	imprimir("");
ER: i ( " Cr+ " ) ;
Terminales = {'imprimir',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/YTyHnLG/5imprimir.png)

	implimirln("");
ER: il ( " Cr+ " ) ;
Terminales = {'imprimirln',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/qRFj3kQ/5imprimirln.png)

	conteo();
ER: Con (  ) ;
Terminales = {'conteo',pariz, parder, puntcoma}
No Terminales = {q0, q1, q2, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/kqKcWjz/5conteo.png)

	datos();
ER: Dat (  ) ;
Terminales = {'imprimirln',pariz, parder, puntcoma}
No Terminales = {q0, q1, q2, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/7zxLZ0X/5datos.png)

	promedio("");
ER: pr ( " Cr+ " ) ;
Terminales = {'promedio',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/W2L0XCS/5promedio.png)

	contarsi("", );
ER: Cs ( " Cr+ " , Cr+ ) ;
Terminales = {'contarsi',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/pwnM9q8/5contarsi.png)

	sumar("");
ER: suma ( " Cr+ " ) ;
Terminales = {'sumar',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/ThhCdGV/5sumar.png)

	max("");
ER: max ( " Cr+ " ) ;
Terminales = {'max',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/b3vcFgW/5maz.png)

	min("");
ER: min ( " Cr+ " ) ;
Terminales = {'min',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/hKK7hcR/5min.png)

	exportarReporte("");
ER: exRep ( " Cr+ " ) ;
Terminales = {'exportarReporte',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3, q4, q5, q6, q7}
Inicio = {q0}

![Imagen 1](https://i.ibb.co/80M3Ldg/5exrep.png)

---

# Gramática independiente del contexto (Analizador Sintactico)

	Claves = ["",""]
Terminales = {'Claves', igual, coriz, corder, comillas, coma, texto}
No Terminales = {q0, q1, q2, q3}
Inicio = {q0}
Producciones:
< q0 >::= Claves igual < q1 >
< q1 >::= coriz < q2 > corder
< q2 >::= comillas texto commillas < q3 >
< q3 >::= coma < q2 > | e

	Registros = [{,"",}{,"",}]
Terminales = {'Registros', igual, coriz, corder, llaiz, llader, comillas, coma, texto}
No Terminales = {q0, q1, q2, q3, q4}
Inicio = {q0}
Producciones:
< q0 >::= Registros igual < q1 >
< q1 >::= coriz < q2 > corder
< q2 >::= llaiz < q3 > llader
< q3 >::= texto < q4 > | comillas texto comillas < q4 >
< q4 >::= coma < q3 > | e

	#Comentario
Terminales = {numeral, texto}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= numeral < q1 >
< q1 >::= texto < q2 > | e
< q2 >::= texto < q1 > | e

	'''
Terminales = {',texto, '\n'}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= ''' < q1 > '''
< q1 >::= texto < q2 > | \n < q2 > | e
< q2 >::= texto < q1 > | \n < q2 > | e

	imprimir("");
Terminales = {'imprimir',pariz, parder, texto, comilla, puntcoma}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= imprimir < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla

	implimirln("");
Terminales = {'imprimirln',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= imprimirln < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla

	conteo();
Terminales = {'conteo',pariz, parder, puntcoma}
No Terminales = {q0, q1}
Inicio = {q0}
Producciones:
< q0 >::= conteo < q1 > puntcoma
< q1 >::= pariz parder

	datos();
Terminales = {'imprimirln',pariz, parder, puntcoma}
No Terminales = {q0, q1}
Inicio = {q0}
Producciones:
< q0 >::= datos < q1 > puntcoma
< q1 >::= pariz parder

	promedio("");
Terminales = {'promedio',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= promedio < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla

	contarsi("", );
Terminales = {'contarsi',pariz, parder, coma, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2, q3}
Inicio = {q0}
Producciones:
< q0 >::= contarsi < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla < q3 >
< q3 >::= coma texto | coma e

	sumar("");
Terminales = {'sumar',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= sumar < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla

	max("");
Terminales = {'max',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= max < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla

	min("");
Terminales = {'min',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= min < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla

	exportarReporte("");
Terminales = {'exportarReporte',pariz, parder, caracter, comilla, puntcoma}
No Terminales = {q0, q1, q2}
Inicio = {q0}
Producciones:
< q0 >::= exportarReporte < q1 > puntcoma
< q1 >::= pariz < q2 > parder
< q2 >::= comilla texto comilla

---

## Clases y métodos utilizados

**App -interfaz grafica-**
* Clase ventana principal:
. Importaciones, tKinter y funciones del analizador lexico y sintactico .
    - Metodos y Funciones
![Imagen 2](https://i.ibb.co/b67GpGd/1app.png)
* Class Ventana:
Es una pestaña que se abre para mostrar la interfaz para mostrar los datos cargados, son dos textbox yno disponible para editar y otro solo para ver.
![Imagen 2](https://i.ibb.co/nz6tGYP/1-1defabrir.png)
* Def Abrir:
Es una funcion que se encarga de abrir un archivo y mostrarlo en la ventana principal.
![Imagen 2](https://i.ibb.co/JFqFTPG/1-2analizar.png)
* Def Analizar:
Es una funcion que se encarga de analizar el texto que se encuentra en el textbox y mostrarlo en el otro textbox, crea los reportes.

**Objetos**
* Clase Lexema
Es una clase la cual va a contener los datos de cada lexema, como su tipo, valor, fila y columna. para posteriormente guardarlos en una lista y mostrarlos en la interfaz y reportes.
![Imagen 2](https://i.ibb.co/RN7ZvG1/2-2lexemas.png)

* Clase Error
Es una clase la cual va a tener los datos de los errores, como su tipo, valor, fila y columna., en la cual se van a guardar los errores que se encuentren en el texto.
![Imagen 2](https://i.ibb.co/Q8WtCjw/2-1objetos.png)


**Analizador Lexico**
![Imagen 2](https://i.ibb.co/vDKvVBr/3analexico.png)
* Clase Analizador Lexico
    - Metodos y Funciones
* Es el analizador lexico, el cual se encarga de analizar el texto y separarlo en lexemas, para posteriormente guardarlos en una lista y mostrarlos en la interfaz y reportes.
![Imagen 2](https://i.ibb.co/tsBsVpH/3-1leerpalabrasreservadas.png)
* Los metodos que se encargan de leer las palabras reservadas las ordena como objetos y las almacena en una lista. para verificar los archivos de entrada.
![Imagen 2](https://i.ibb.co/WVww1Z8/3-2todaslaspalabrasreservadas.png)
* se muestran todos los casos del if para leer todas las palabras quemadas.
![Imagen 2](https://i.ibb.co/7V713S2/3-3armarlexemas.png)
* metodo que se encarga de armar los lexemas y se corta al encontrar un espacio, salto de linea o tabulacion segun se amerite, para posteriormente guardarlos en una lista y mostrarlos en la interfaz y reportes.
![Imagen 2](https://i.ibb.co/CPy9h7B/3-4reportes.png) 


**Analizador Sintactico**
![Imagen 2](https://i.ibb.co/9bcSGGF/4anasintactico.png)
* Clase Analizador Sintactico
    - Metodos y Funciones
* Es la clase en la cual va a ordenar todos los metodos y funciones para realizar el analisis sintactico.
![Imagen 2](https://i.ibb.co/hKZNqx2/4-1funcionalidad.png)
* recibe los lexemas y los analiza para para verificar que esten en el orden correcto, para posteriormente guardarlos en una lista y mostrarlos en la interfaz y reportes.
![Imagen 2](https://i.ibb.co/BqnqRkJ/4-2erroressintactivos.png)
* continua con las demas palabras reservadas y las analiza para verificar que esten en el orden correcto, para posteriormente guardarlos en una lista y mostrarlos en la interfaz y reportes.
![Imagen 2](https://i.ibb.co/HTMkx84/4-3demasclavesenotrdenyrepsintactivo.png)