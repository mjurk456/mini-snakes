#!/usr/bin/env python3

from unidecode import unidecode

MORSE = {'A': '. —',   'B': '— . . .',  'C': '— . — .', 
    'D': '— . .',  'E': '.',   'F': '. . — .',
    'G': '— — .',  'H': '. . . .',  'I': '. .',
    'J': '. — — —',  'K': '— . —',  'L': '. — . .',
    'M': '— —',   'N': '— .',   'O': '— — —',
    'P': '. — — .',  'Q': '— — . —',  'R': '. — .',
    'S': '. . .',  'T': '—',   'U': '. . —',
    'V': '. . . —',  'W': '. — —',  'X': '— . . —',
    'Y': '— . — —',  'Z': '— —. .',
    
    '0': '— — — — —', '1': '. — — — —', '2': '. . — — —',
    '3': '. . . — —', '4': '. . . . —', '5': '. . . . .',
    '6': '— . . . .', '7': '— — . . .', '8': '— — — . .',
    '9': '— — — — .', ' ': '    ' 
    }

DIV = '   '
revMorse = dict((v, k) for k, v in MORSE.items())

introduction = """
***** INTERNATIONAL MORSE CODE *****
1. The length of a dot is one unit.
2. A dash is three units.
3. The space between parts of the same letter is one unit.
4. The space between letters is three units.
5. The space between words is seven units.

Input a sentence to translate into Morse code or Morse code string to translate
into a sentence. For exit press <Enter> without any input.
"""

def to_morse(s):
    a = unidecode(s).upper()
    result = ''
    for char in a:
        if char in MORSE:
            result = result + MORSE[char] + DIV
    if result.strip():
        return result.strip()
    else:
        return 'Wrong input'


def to_letters(s):
    a = s.replace('-','—').split(DIV)
    result = ''
    for item in a:
        item = item.strip()
        if item in revMorse:
            result = result + revMorse[item]
        if item == '':
            result =  result + ' '
    result = result.strip().replace('  ', ' ')
    if result:
        return result
    else:
        return 'Wrong input'


def main():
    print(introduction)
    while True:
        q = input("? ").strip()
        if q == '':
            return None
        else:
            if q[0] in "—.-":
                print(to_letters(q))
            else:
                print(to_morse(q))


if __name__ == "__main__":
    main()
