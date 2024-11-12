"""
Unit tests for the Varasto class, testing its initialization, 
adding and removing items, and validating expected behavior 
in various scenarios.
"""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """
    Test case for the Varasto class to verify correct initialization,
    adding to storage, removing from storage, and the maintenance of
    storage constraints.
    """
    def setUp(self):
        """
        Set up a Varasto instance with a capacity of 10 for testing.
        """
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """
        Test that the constructor creates an empty storage with a saldo of 0.
        """
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """
        Test that a new Varasto has the correct capacity as initialized.
        """
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """
        Test that adding items increases the saldo by the correct amount.
        """
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """
        Test that adding items decreases the available space correctly.
        """
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """
        Test that removing items returns the correct amount, 
        without exceeding the current saldo.
        """
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """
        Test that removing items increases the available space appropriately.
        """
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
