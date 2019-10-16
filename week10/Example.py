class Example:
    
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Example object with name: {}".format(self.__name)
   
    def get_name(self):
        return self.__name



