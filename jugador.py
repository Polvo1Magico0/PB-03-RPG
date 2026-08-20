
class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.personaje = None

    def selecionar_personaje(self, personaje):

        self.personaje = personaje

        print(f"{self.nombre} seleccion al pj"
              f"{personaje.nombre}")

    def mostrar_personaje(self):

        if self.personaje is not None:
            print(f"el jugador {self.nombre}"
                  f" utiliza a {self.personaje.nombre}")
        else:
            print("El jugador no tiene un pj seleccionado")

