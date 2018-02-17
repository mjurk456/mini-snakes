""" Counts a similar expressions with integers.
    Accepts strings like "123 - (96*3)/9".
    Returns a result rounded up to an integer.
"""

import re

class ExpressionCounter():
    def __init__(self, exp = ""):
        self.temp = ""
        if exp:
            self.set_expression(exp)
        else:
            self.expression = ""
        return None
        
    def set_expression(self, exp):
        self.expression = exp.replace(" ","")
                
        return None
        
    def count(self):
        self.parenthesis =  re.compile(r"(\()([+/*-0123456789]+)(\))")
        self.product = re.compile(r"(-?\d+)([/*])(-?\d+)")
        self.adding = re.compile(r"([+-]?\d+)")
        
        while True:
            try:
                
                return int(self.expression)
            except ValueError:
                while True: #()
                    a = self.parenthesis.search(self.expression)
                    if a == None:
                        k = self.it(self.expression)
                        if k:
                            self.expression = k
                            break
                        else:
                            return
                        
                    else:
                        # * /
                        temp = a.group(2)
                        k = self.it(temp)
                        if k:
                            self.expression = self.expression[:a.start()] \
                                          + self.it(temp) \
                                          + self.expression[a.end():]
                        else:
                            return
            
    
    def it(self, x):
        while True:
            b = self.product.search(x)
            if b:
                b1 = int(b.group(1))
                b3 = int(b.group(3))
                if b.group(2) == "*":
                    z = b1 * b3
                elif b.group(2) == "/":
                    z = b1 / b3
                x = x[:b.start()] \
                    + str(int(z)) \
                    + x[b.end():]             
            else:
                break
        x = x.replace("--", "+")
        c = self.adding.split(x)
        if c:
            try:
                z = sum([int(i) for i in c if i])
            except ValueError:
                print("Wrong symbol in expression: %s" % x)
                return
        else:
            z = 0
        return str(z)
        

def main():    
    
    testStr = "-9*-10 + (189+9-3)/7"
    n = ExpressionCounter(testStr)
    print(n.count())


if __name__ == "__main__":
    main()
