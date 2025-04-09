# class for all the properties in the game
class Property:
    def __init__(self, name, value, base_tax, owner=None):
        self.__name = name
        self.__value = value
        self.__base_tax = base_tax
        self.__tax_multiplier = [1,5,15,45,80,125]
        self.__tax_rate = 0
        self.owner = owner


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def get_base_tax(self):
        return self.__base_tax * self.__tax_multiplier[self.__tax_rate]

    def set_tax_rate(self, tax_rate):
        self.__tax_rate = tax_rate

    def 