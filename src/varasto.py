"""
This module provides the Varasto class, which simulates a simple storage unit.
It supports setting initial volume and balance, as well as adding to and removing
from the storage with proper validation to handle edge cases.
"""

class Varasto:
    """
    A class to represent a storage unit with a maximum capacity (volume).
    It allows managing the current balance, adding to the storage, and
    removing from the storage, ensuring that the balance does not exceed
    the capacity or go below zero.
    """

    def __init__(self, tilavuus, alku_saldo=0):
        """
        Initializes the Varasto instance with a specified capacity (tilavuus) 
        and an optional initial balance (alku_saldo).

        Args:
            tilavuus (float): The maximum capacity of the storage.
            alku_saldo (float, optional): The initial balance of the storage.
                                          Defaults to 0.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        """
        Calculates the remaining capacity in the storage.

        Returns:
            float: The remaining capacity (tilavuus - saldo).
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Adds a specified amount to the storage if it is positive and
        does not exceed the remaining capacity.

        Args:
            maara (float): The amount to add to the storage.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Removes a specified amount from the storage if it is positive and 
        does not exceed the current balance.

        Args:
            maara (float): The amount to remove from the storage.

        Returns:
            float: The amount actually removed, which may be less than 
                   requested if the balance is insufficient.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """
        Returns a string representation of the storage, including the 
        current balance and remaining capacity.

        Returns:
            str: A string in the format "saldo = <balance>, vielä tilaa <remaining capacity>".
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
