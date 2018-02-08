#!/usr/bin/env python3
""" Validator PESEL.
    Przekazuje się zmienną typu string z numerem PESEL
    do sprawdzenia.
    Zwraca True, jeśli numer jest poprawny, i odpowiednio False.
    Algorytm sprawdzenia PESElu został wzięty stąd:
    http://www.infor.pl/prawo/gmina/dowod-osobisty/262184,Jak-sprawdzic-czy-masz-poprawny-PESEL.html
"""
import unittest


def check_pesel(peselNr):
    if len(peselNr) < 11:
        return False
    if not peselNr.isdigit():
        return False
    final = 0
    checkArray = [1,  3, 7, 9, 1,  3, 7,  9, 1, 3]
    final = sum([int(peselNr[i]) * checkArray[i] for i in range (10)])
    return (10 - int(str(final)[-1])) == int(peselNr[-1])

class PeselTest(unittest.TestCase):

    def test_correct_pesel(self):
        self.assertTrue(check_pesel("92121510595"))
        self.assertTrue(check_pesel("99810235403"))

    def test_wrong_pesel(self):
        self.assertFalse(check_pesel("44051401358"))
        self.assertFalse(check_pesel("51401358"))


if __name__ == "__main__":
    unittest.main()
