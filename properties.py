
class Property:
    def __init__(self, name, value, base_tax, owner=None):
        self.__name = name
        self.__value = value
        self.__base_tax = base_tax
        self.__tax_multiplier = 1
        self.owner = owner
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_value(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value
    
    def set_base_tax(self, base_tax):
        self.__base_tax = base_tax

    def get_base_tax(self):
        return self.__base_tax
    
    def set_tax_multiplier(self, multiplier):
        self.__tax_multiplier = multiplier

    def get_tax_multiplier(self):
        return self.__tax_multiplier