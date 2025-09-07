# 4).Se requiere un programa que modele el concepto de un planeta del sistema solar. Un planeta tiene los
#siguientes atributos:
#a. Un nombre de tipo String con valor inicial de null.
#b. Cantidad de satélites de tipo int con valor inicial de cero.
#c. Masa en kilogramos de tipo float con valor inicial de cero
#d. Volumen en kilómetros cúbicos de tipo float con valor inicial de cero.
#e. Diámetro en kilómetros de tipo int con valor inicial de cero.
#f.Distancia media al Sol en millones de kilómetros, de tipo int con valor inicial de cero.
#g.Tipo de planeta de acuerdo con su tamaño, de tipo string con valor inicial null.
#h. Observable a simple vista, de tipo booleano con valor inicial false.

#La clase debe incluir los siguientes métodos:
#a. La clase debe tener un constructor que inicialice los valores de sus respectivos atributos.
#b. Definir un método que imprima en pantalla los valores de los atributos de un planeta.
#c. Calcular la densidad un planeta, como el cociente entre su masa y su volumen.
#d. Determinar si un planeta del sistema solar se considera exterior.
#Un planeta exterior está situado más allá del cinturón de asteroides. El cinturón de asteroides
#se encuentra entre 2.1 y 3.4 UA. Una unidad astronómica (UA) es la distancia entre la Tierra y
#el Sol=149597870 Km.



#Se deben crear dos planetas y mostrar los valores de sus atributos en pantalla. Además, se debe
#imprimir la densidad de cada planeta y si el planeta es un planeta exterior del sistema solar.

class Planet:
    AU_IN_KM = 149597870  # 1 Unidad Astronómica (UA) en km

    def __init__(self, name=None, satellites=0, mass=0.0, volume=0.0,
                 diameter=0, distance_from_sun_km=0, planet_type=None,
                 visible_to_naked_eye=False):

        self.name = name
        self.satellites = satellites
        self.mass = mass                      # en kg
        self.volume = volume                  # en km³
        self.diameter = diameter              # en km
        self.distance_from_sun_km = distance_from_sun_km  # en km
        self.planet_type = planet_type
        self.visible_to_naked_eye = visible_to_naked_eye

    def show(self):
        """Imprime en pantalla los valores de los atributos del planeta"""
        print("----- Datos del planeta -----")
        print("Nombre:", self.name)
        print("Satélites:", self.satellites)
        print("Masa (kg):", self.mass)
        print("Volumen (km³):", self.volume)
        print("Diámetro (km):", self.diameter)
        print("Distancia media al Sol (km):", self.distance_from_sun_km)
        print("Tipo de planeta:", self.planet_type)
        print("Observable a simple vista:", self.visible_to_naked_eye)

    def density(self):
        """Calcula la densidad = masa / volumen"""
        if self.volume != 0:
            return self.mass / self.volume
        else:
            return None  # para evitar división por cero

    def is_exterior(self):
        """
        Determina si el planeta es exterior (más allá del cinturón de asteroides).
        El cinturón está entre 2.1 y 3.4 UA.
        """
        distance_in_AU = self.distance_from_sun_km / Planet.AU_IN_KM
        return distance_in_AU > 3.4  # más allá del cinturón de asteroides




if __name__ == "__main__":
    # Crear planeta Tierra
    earth = Planet(
        name="Tierra",
        satellites=1,
        mass=5.972e24,
        volume=1.08321e12,
        diameter=12742,
        distance_from_sun_km=149597870,  # 1 UA
        planet_type="Terrestre",
        visible_to_naked_eye=True
    )

    # Crear planeta Júpiter
    jupiter = Planet(
        name="Júpiter",
        satellites=79,
        mass=1.898e27,
        volume=1.431e15,
        diameter=139820,
        distance_from_sun_km=778e6,  # km aprox (5.2 UA)
        planet_type="Gaseoso gigante",
        visible_to_naked_eye=True
    )


    earth.show()
    print("Densidad (kg/km³):", earth.density())
    print("¿Es planeta exterior?:", earth.is_exterior())

    print()  # línea en blanco

    jupiter.show()
    print("Densidad (kg/km³):", jupiter.density())
    print("¿Es planeta exterior?:", jupiter.is_exterior())
