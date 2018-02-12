#!/usr/bin/env python3
""" Aktualnie obowiązujący średni kurs walut w odniesieniu do PLN.
    Pobierany jest ze strony nbp.pl.
    Użytkownik może wybrać walutę lub zobrazić tabelę w całości.
"""

import json
import requests


def kurs_walut(waluta):
    """ Zwraca aktualny kurs dla zadanej waluty / PLN.
        Parametr:
           waluta - String
        Zwraca:
           Float
    """
    url = 'http://api.nbp.pl/api/exchangerates/rates/a/%s/?format=json' \
          % waluta
    kursData = ""
    response = requests.get(url)
    response.raise_for_status()
    if response.text[0] == "<": #niekedy zwróci HTML
        return -1
    else:
        kursData = json.loads(response.text)
        return kursData['rates'][0]['mid']
    

def wszystkie_kursy():
    url = 'http://api.nbp.pl/api/exchangerates/tables/a/?format=json'
    kursAll = ""
    respAll = requests.get(url)
    respAll.raise_for_status()
    table = []
    
    if respAll.text[0] == "<": #niekedy zwróci HTML
        table.append(-1)
    else:
        kursAll = json.loads(respAll.text)
        for item in kursAll[0]['rates']:
            table.append("%s %s %f" % (item['currency'], \
                                   item['code'], \
                                   item['mid']))
    return table    



def main():
    print("""Program do sprawdzenia aktualnego kursu walut zgodnie z nbp.pl.
Aby sprawdzić wszystkie kursy, wprowadź 'all'.
Aby sprawdzić konkterną walutę, wprowadź jej nazwę, np. 'eur'.
Aby skończyć, po prostu naciśnij <Enter>.""")
    while True:
        userChoice = input("? ").lower()
        if userChoice == "all":
            for i in wszystkie_kursy():
                print(i)
        elif userChoice == "":
            break
        else:
            try:
                a = kurs_walut(userChoice)
                if a == -1:
                    raise ValueError
                print(a)
            except ValueError:
                print("Problem z serwerem, spróbuj później")
            except:
                print("Zła waluta")
          
          
    


if __name__ == '__main__':
    main()
