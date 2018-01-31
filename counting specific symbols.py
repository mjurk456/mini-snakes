def counting_symbols(text, symbols):
    return len([x for x in text.lower() if x in symbols]) 
    
def main():
    print(counting_symbols("There's also the style of using a short unique prefix to group related names together. This is not used much in Python, but it is mentioned for completeness.", "aeiou"))
    
if __name__ == "__main__":
    main()
