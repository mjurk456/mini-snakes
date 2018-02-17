import unittest
import calculator

class TestCalculator(unittest.TestCase):


    def test_parenthesis(self):
        self.assertEqual(
            calculator.ExpressionCounter("126 * (123+9)").count(), \
            16632)
        self.assertEqual(
            calculator.ExpressionCounter("(12 - 9 + 36*10)* (123+9)").count(), \
            47916)
        self.assertEqual(
            calculator.ExpressionCounter("(((12+1)*5+3)*10)-136").count(), \
            544)
        self.assertEqual(
            calculator.ExpressionCounter("-9*-10 + (189+9-3)/7").count(),
            117)


    def test_minus(self):
        self.assertEqual(calculator.ExpressionCounter("-9--9").count(), \
                         0)
        self.assertEqual(calculator.ExpressionCounter("-9*-10").count(),
                         90)


    def test_errors(self):
        self.assertEqual(
            calculator.ExpressionCounter("z (-9--9)+++*9").count(), \
            None)
        self.assertEqual(
            calculator.ExpressionCounter("0.15-0.9").count(), \
            None)

if __name__ == "__main__":
    unittest.main()


        
