class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total_price(self):
        total_price = sum(item["product"].price * item["quantity"] for item in self.items)
        return total_price

    def free_delivery(self):
        total_price = self.calculate_total_price() #this is return the value true and false only
        return total_price >= 1000

    def tex(self):
        total_price = self.calculate_total_price()
        return total_price * 0.18               #every type of the product get the 18 % tex

    def final_price(self):
        total_price = self.calculate_total_price()
        if total_price >= 1000:
            return total_price + self.tex()     #1000 hight then only add 18 %
        else:
            return total_price + self.tex() + 50  # Adding delivery charge if total < 1000
                                                  # low the 1000 then add tex and 50 extera amount