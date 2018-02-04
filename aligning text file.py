#!/usr/bin/env python3


def text_file_aligning(file, align, lineLength):
    """Splits text file into lines with given length and align these lines
       as given.
       Parameters:
       file - path to .txt file. String.
       align - type of aligning. One-symbol string.
          r - right
          l - left
          c - center
        lineLength - length of a line into which the text file fill be splitted.
          Integer.

        Returns:
        output on the screen
     """   
    if align == "r":
        pattern = "{:>"
    elif align == "l":
        pattern = "{:"
    elif align == "c":
        pattern = "{:^"
    pattern = pattern + str(lineLength) + "}"
    
    f = open(file, "r")
    for line in f:
        mappingSpaces = []
        start = 0
        while len(line) > lineLength:
            p = line[:lineLength].rfind(" ")
            print(pattern.format(line[:p]))
            line = line[p + 1:]
        else:
            print(pattern.format(line))
    f.close()
