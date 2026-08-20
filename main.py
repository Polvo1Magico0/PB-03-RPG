from jugador import Jugador
from mago import Mago
from objeto import Objeto

#Método principal

def main():

    # CREAR JUGADOR
    nuevo_jugador = Jugador("Eric")

    # CREAR PJS
    magician = Mago("Gandalf", 10, 100, 80)

    # ASOCIAR JUGADOR CON EL PJ
    nuevo_jugador.selecionar_personaje(magician)
    nuevo_jugador.mostrar_personaje()

    # ATAQUE DEL MAGO
    magician.atacar()

    #CREAR OBJETOS

    pocion = Objeto("Pocion de vida", "consumible")
    staff = Objeto("Staff del Arcangel", "Arma")

    # AGREGAR AL INVENTARIO
    magician.inventario.agregar_objeto(pocion)
    magician.inventario.agregar_objeto(staff)

    #MOSTRAR INVENTARIO
    magician.inventario.mostrar_inventario()

if __name__== "__main__":
    main()