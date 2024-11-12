"""
This module provides a demonstration of the Varasto class, showing its basic 
usage and functionality. It initializes instances of the Varasto class with 
various values and performs actions such as adding to and removing items from 
the storage. It also demonstrates error handling for invalid inputs.
"""

from varasto import Varasto

def initialize_varastot():
    """
    Initializes Varasto instances for demonstration.
    
    Returns:
        tuple: A tuple containing two Varasto instances for juice and beer.
    """
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def display_initial_values(mehua, olutta):
    """
    Displays the initial values of the Varasto instances.
    """
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def display_olut_getters(olutta):
    """
    Displays getter values for the olutta Varasto instance.
    """
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def modify_mehuvarasto(mehua):
    """
    Demonstrates adding to and removing from the mehu Varasto instance.
    """
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def test_error_scenarios():
    """
    Demonstrates error scenarios when creating or modifying Varasto instances.
    """
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def test_olut_operations(olutta):
    """
    Tests adding to and removing from the olutta Varasto instance.
    """
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def test_mehu_operations(mehua):
    """
    Tests adding invalid values to 
    """
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    """
    Main function to demonstrate the usage of the Varasto class. It creates 
    instances of Varasto, displays initial values, modifies the contents, and 
    handles error scenarios. This function also tests the getter methods, 
    addition, and removal functionality of Varasto instances.
    """
    mehua, olutta = initialize_varastot()
    display_initial_values(mehua, olutta)
    display_olut_getters(olutta)
    modify_mehuvarasto(mehua)
    test_error_scenarios()
    test_olut_operations(olutta)
    test_mehu_operations(mehua)


if __name__ == "__main__":
    main()
