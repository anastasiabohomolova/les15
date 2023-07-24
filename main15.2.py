class MainClass:
    def __init__(self, arg):
        self.arg = arg

    @classmethod
    def method(cls, a):
        el = list(a)
        n = []
        for i in el:
            if isinstance(i, tuple):
                for el in i:
                    if isinstance(el, str):
                        n.append(el)

            elif isinstance(i, str):
                n.append(i)
        print(n)
        return cls(a)


d = {'name': ['Daria', 25], ('work',):['manager', 9], 'skills':['language', 3]}
new_obj = MainClass.method(d)
#print(new_obj.__dict__)