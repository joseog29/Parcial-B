# Parcial-B

Duración:    dos horas (120 minutos)

Antes de comenzar:

●	No dé la vuelta al examen hasta que se le indique. 
●	Todos los dispositivos electrónicos deben estar guardados en la mochila y apagados o sin sonido. En caso contrario debe indicarse al profesor los motivos por los que debe tenerse el teléfono con sonido antes de comenzar el examen. 
●	Se permite el uso de calculadoras, aunque su utilización no es necesaria para la realización del examen. 
●	El uso de cualquier dispositivo electrónico o el plagio o copia conlleva el suspenso del examen y de la evaluación ordinaria, acudiendo directamente a la evaluación extraordinaria según el artículo 9 del reglamento sobre pruebas de evaluación y su revisión.
●	Artículo  9.º.  De  la  utilización  de  métodos  ilícitos  para  la  superación  de  las  pruebas  de  evaluación. “Cualquier evidencia de plagio,  de copia del examen de un compañero, o cualquier intento de  obtener  de  forma  fraudulenta  las  respuestas  a  las  preguntas  de  una  prueba  de  evaluación, será penalizada con el suspenso en la convocatoria ordinaria y extraordinaria y podrá suponer la apertura de expediente y la aplicación de las  correspondientes  sanciones,  pudiendo  llegar  a  sustanciarse  en  la  expulsión  de  la  Universidad del alumno o alumnos implicados,  conforme a lo establecido en los arts. 29 y siguientes del Reglamento del Alumnado de esta Universidad. “
●	No se podrá abandonar la sala o el lugar del examen hasta que no haya finalizado el examen completo.


Resultados de aprendizaje que se evalúan en este examen:

●	Ser capaz de programar en un lenguaje de programación utilizando estructuras de datos comunes 
●	Ser capaz de implementar algoritmos básicos. 
●	Ser capaz de probar adecuadamente los programas desarrollados. 
 
Ejercicio 1 (1,5 punto) Tiempo estimado: 10 minutos. Responda a las cuestiones:
La calificación máxima de esta parte tipo test es de 1 punto. Tenga en cuenta que:
●	Para cada pregunta, sólo existe una respuesta correcta.
●	Cada respuesta correcta sumará 0.10 puntos.
●	Cada respuesta incorrecta restará 0.10 puntos.
●	Las preguntas no contestadas ni suman ni restan puntuación.

1.	¿Cuál es la complejidad temporal promedio de acceso a un elemento en un diccionario de Python?
A) O(n^2)
B) O(n)
C) O(1)
D) O(log n) 
2.	¿Qué método se usa para buscar un valor en un diccionario sin provocar una excepción si la clave no existe?
A) dict.search()
B) dict.get()
C) dict.lookup()
D) dict.find() 
3.	¿Cuál es la complejidad temporal del algoritmo de ordenamiento por inserción en el peor caso?
A) O(log n)
B) O(n log n)
C) O(n^2)
D) O(n) 
4.	¿Qué condición es esencial para que una función recursiva no provoque un error de desbordamiento de pila (stack overflow)?
A) Que imprima el resultado en cada llamada.
B) Que tenga una condición de parada.
C) Que tenga una llamada a sí misma.
D) Que use variables globales. 
5.	¿Cuál es el propósito del método mágico __str__ en una clase de Python?
A) Convertir el objeto en un número
B) Inicializar atributos
C) Representar el objeto como cadena legible
D) Comparar dos objetos 
6.	¿Cuál es la complejidad temporal del algoritmo de búsqueda binaria en una lista ordenada?
A) O(n log n)
B) O(log n)
C) O(1)
D) O(n) 
7.	¿Qué hace la función super() en una clase hija?
A) Llama a métodos de la clase hija
B) Elimina atributos heredados
C) Crea una nueva instancia
D) Llama a métodos de la clase padre 
8.	¿Cuál de los siguientes métodos mágicos permite definir el comportamiento del operador == en una clase personalizada?
A) __compare__
B) __eq__
C) __match__
D) __cmp__ 
9.	¿Cuál es la complejidad temporal en el peor caso de comprobar si un elemento está en una lista (x in list)?
A) O(n)
B) O(n^2)
C) O(log n)
D) O(1) 
10.	¿Cuál es la complejidad temporal de añadir un elemento al final de una lista en Python (usando append) en promedio?
A) O(n^2)
B) O(1)
C) O(log n)
D) O(n) 
11.	¿Qué ocurre si una clase hija redefine un método de la clase padre?
A) El método redefinido en la clase hija se ejecuta en función de la clase del objeto.
B) Se produce un error de compilación.
C) El método de la clase padre se ejecuta siempre.
D) Ambos métodos se ejecutan automáticamente. 
12.	¿Cuál de las siguientes estructuras permite almacenar elementos sin duplicados y con acceso rápido?
A) Diccionario
B) Tupla
C) Lista
D) Conjunto (set) 
13.	¿Cuál de las siguientes operaciones sobre conjuntos (set) tiene una complejidad promedio de tiempo constante?
A) x in set
B) set.remove(x)
C) Todas las anteriores
D) set.add(x) 
14.	¿Qué tipo de colección es más adecuada para representar pares clave-valor con acceso rápido por clave?
A) Diccionario
B) Tupla
C) Lista
D) Conjunto 
15.	¿Cuál es el método mágico que se ejecuta al crear una nueva instancia de una clase para inicializar sus atributos?
A) __init__
B) __build__
C) __new__
D) __create__ 
 
Ejercicio 1 (1 punto) Tiempo estimado: 10 minutos.  
Teoría: Que es la recursividad. Que elementos se deben cumplir para que un algoritmo recursivo sea correcto.
Práctica: Escribe una función recursiva que devuelva la suma del valor absoluto de una lista de números. Escribe un código de prueba con una llamada a la función.
 
Ejercicio 3 (1,5 puntos): 15 minutos. 
Teoría: Compara el comportamiento de los siguientes métodos. Indica en que casos se usan y cual es su complejidad temporal. 
1.	Búsqueda secuencial.
2.	Búsqueda binaria.
Práctica: Escribe el código de al menos uno de ellos.
 
Ejercicio  ( 2,5 puntos): 20 minutos. Análisis de ventas de libros con listas y diccionarios
Descripción:
En este ejercicio, deberás demostrar tu comprensión de las estructuras de datos en Python, específicamente listas y diccionarios. Se te proporcionará una lista de libros con su número de ventas. Tu tarea será consultar las ventas de un libro específico y determinar cuál ha sido el libro más vendido.
Enunciado:
Dada la siguiente lista de diccionarios, donde cada diccionario representa un libro y su número de ventas:
ventas = [
    {"titulo": "Cien años de soledad", "ventas": 120},
    {"titulo": "Don Quijote de la Mancha", "ventas": 150},
    {"titulo": "La sombra del viento", "ventas": 95},
    {"titulo": "El principito", "ventas": 180}
]
Parte Teórica:
1. Explica brevemente las diferencias entre una lista y un diccionario en Python.
2. ¿Cuándo es más apropiado usar una lista y cuándo un diccionario? Justifica tu respuesta en función del tipo de acceso, la estructura de los datos y la eficiencia.
Parte Práctica:
Escribe una función consultar_ventas(ventas): que reciba la lista de libros y retorne el libro más vendido con sus ventas.
resultado = libro_mas_vendido(ventas)
print(resultado)
# {'titulo': 'El principito', 'ventas': 180}


































 
Ejercicio 4: (3,5 puntos) Gestión de atletas en una competición
Se desea desarrollar un sistema básico para gestionar la participación de atletas en una competición deportiva.
Para ello, se propone modelar dos clases:
•	Atleta: representa a un deportista que participa en la competición.
•	Competición: representa el evento deportivo que agrupa a varios atletas.
La relación entre las clases debe ser de agregación, ya que la competición incluye atletas, pero estos pueden existir independientemente de la competición.
Requisitos:
1.	La clase Atleta debe tener al menos los siguientes atributos:
o	nombre (cadena de texto)
o	pais (cadena de texto)
o	edad (entero)
o	disciplina (cadena de texto, por ejemplo: 100m, salto largo, natación)
2.	La clase Competición debe tener:
o	Una lista de atletas
o	Métodos para: 
	Agregar un atleta a la competición
	Eliminar un atleta por nombre
	Mostrar todos los atletas inscritos
	Buscar atletas por disciplina
3.	Implementa un pequeño programa que:
o	Cree varios atletas
o	Los agregue a una competición
o	Realice algunas operaciones como búsqueda y eliminación
o	Muestre la lista final de participantes
 

<img width="499" height="351" alt="image" src="https://github.com/user-attachments/assets/35e2d7b1-0815-4337-ba46-f53b0a785780" />
