class PreciousStone:
    def __init__(self, carats, price, name, public_int_field, public_str_field):
        self.carats = carats
        self.__price = price
        self.__name = name
        self.public_int_field = public_int_field
        self.public_str_field = public_str_field

    def get_carats(self):
        return self.carats

    def set_carats(self, carats):
        self.carats = carats

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return (f"PreciousStone(name: {self.__name}, carats: {self.carats}, "
                f"price: {self.__price}, public_int_field: {self.public_int_field}, "
                f"public_str_field: {self.public_str_field})")

    def __repr__(self):
        return (f"PreciousStone(name={self.__name!r}, carats={self.carats!r}, "
                f"price={self.__price!r}, public_int_field={self.public_int_field!r}, "
                f"public_str_field={self.public_str_field!r})")

    def __del__(self):
        print(f"Deleting instance of PreciousStone with name: {self.__name}")

def main():
    stone1 = PreciousStone(1.5, 5000, "Diamond", 1, "Expensive stone")
    stone2 = PreciousStone(2.0, 7000, "Ruby", 2, "Rare and valuable")
    stone3 = PreciousStone(3.0, 10000, "Emerald", 3, "Precious green gem")

    print(stone1)
    print(stone2)
    print(stone3)

    print(stone1.get_name())
    stone1.set_price(5500)
    print(stone1.get_price())

if __name__ == "__main__":
    main()
