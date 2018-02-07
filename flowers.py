#!/usr/bin/env python3

"""Class for flower evidence in a flower shop.

Public methods:  
    .sell(x) = deduct x from the total number of items
    .get_items() = shows number of items in the evidence
    .set_items(x) = sets number of items 
    .set_price(x) = sets price x for one item
    .total_store_price() = shows total price of items in the store
    .total_sold() = shows number of items sold during the day
    .total_receipts() = shows receipts during the day
"""


class Flower():


    def __init__(self, num = 0, price = 0):
        self.num = num
        self.price = price
        self.start = num
        return None
    

    def sell(self, x):
        self.num = self.num - x
        return None
    

    def get_items(self):
        return self.num
    

    def set_items(self, x):
        if self.num == 0:
            self.start = x
        self.num = x
        return None
    

    def set_price(self, x):
        self.price = x
        return None
    

    def get_price(self):
        return self.price
    

    def total_store_price(self):
        return self.num * self.price
    

    def total_sold(self):
        return self.start - self.num
    

    def total_receipts(self):
        return self.total_sold() * self.price
    

def main():
    roza = Flower(70, 5)
    tulipan = Flower(225, 0.75)
    bez = Flower(15, 5)
    print('{:*^80}'.format("DEMONSTRACJA KLASY UŻYTKOWNIKA Flowers"))
    print("\nW magazynie jest %d róż, %d tulipanów i %d bzu." \
          % (roza.get_items(), tulipan.get_items(), bez.get_items()))
    print("Razem kwiaty kosztują %f zł." \
          % (roza.total_store_price() + tulipan.total_store_price() \
           + bez.total_store_price()))
    print("W ciągu dnia sprzedano tylko 5 tulipanów i dlatego je przeceniono.")
    tulipan.set_price(0.10)
    tulipan.sell(5)
    print("Nowa cena jest %f zł." % tulipan.price)
    print("W magazynie zostało %d tulipanów o ogólnej wartości %f zł"\
          % (tulipan.num, tulipan.total_store_price()))
    roza.sell(56)
    bez.sell(5)
    roza.sell(5)
    print("W ciągu dnia sprzedano też %d róż i %d bzu." \
          % (roza.total_sold(), bez.total_sold()))
    print("Dzienny zysk dla wszystkich kwiatów wyniósł %f zł.\n" \
          % (roza.total_receipts() + tulipan.total_receipts() \
             + bez.total_receipts()))
    print("{:*^80}".format("END"))


if __name__ == "__main__":
    main()
