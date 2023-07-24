class MainClass:
    def __init__(self, *args):
        self.args = args


    @staticmethod
    def method(*args):
        if len(args) != 1:
            raise TypeError

        for el in args:
            if el.isdigit():
                raise TypeError

        return args


el_method = MainClass(MainClass.method('1'))
print(el_method.__dict__)