#Ejercicio Recursividad - Suma de valores absolutos

lista_numeros = [-3, 4.5, -2, 0, -1.25]

def suma_abs(lista_numeros):
    """
    Devuelve la suma del valor absoluto de una lista de números (recursiva).
    """
    if not lista_numeros:
        return 0.0
    return abs(lista_numeros[0]) + suma_abs(lista_numeros[1:])

resultado = suma_abs(lista_numeros)
print(f"La suma de los valores absolutos es: {resultado}")


#Ejemplo de uso:



    


#Ejercicio POO

class Atleta:
    def __init__(self, nombre, pais, edad, disciplina):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
        self.disciplina = disciplina

    def __str__(self):
        return f"Atleta: {self.nombre}, Pais: {self.pais}, Edad: {self.edad} años, Disciplina: {self.disciplina}"
    

    class Competicion:
        def __init__(self):
            self.atletas = []

    def agregar_atleta(self, atleta):
        if atleta in self.atletas:
            print(f"Error: El atleta {atleta.nombre} ya existe.")
            return
        self.atletas.append(atleta)

    def eliminar_atleta(self, nombre):
        for atleta in self.atletas:
            if atleta.nombre == nombre:
                self.atletas.remove(atleta)
                print(f"Atleta {nombre} eliminado.")
                return
        print(f"Error: El atleta {nombre} no existe.")

    def mostrar_atletas(self):
        print("ATLETAS EN LA COMPETICIÓN:")
        if not self.atletas:
            print("No hay atletas registrados.")
        else:
            for atleta in self.atletas:
                print(atleta)

    def buscar_disciplina(self, disciplina):
        encontrados = [atleta for atleta in self.atletas if atleta.disciplina == disciplina]
        if encontrados:
            print(f"Atletas en la disciplina '{disciplina}':")
            for atleta in encontrados:
                print(atleta)
        else:
            print(f"No se encontraron atletas en la disciplina '{disciplina}'.")

    



#Ejercicio diccionarios

ventas = [
    {"titulo": "Cien años de soledad", "ventas": 120},
    {"titulo": "Don Quijote de la Mancha", "ventas": 150},
    {"titulo": "La sombra del viento", "ventas": 95},
    {"titulo": "El principito", "ventas": 180}
]

def consultar_ventas(titulo):
    """
    Consulta las ventas de un libro por su título.
    """
    for libro in ventas:
        if libro["titulo"].lower() == titulo.lower():
            return f"El libro '{libro['titulo']}' ha vendido {libro['ventas']} copias."
    return f"El libro '{titulo}' no se encuentra en el registro de ventas."



