a = "tatiana"
b = "alejandro"
class StringModules(object):
    def plus(self):
        print (a+b)

    def plusReverse(self):
        print (b+a)

class SymbolModules(object):
    def tSearch(self, arg):
       print ("letter 't' in {0} found {1} times".format(arg, arg.count("t")))

    def aSearch(self, arg):
        print ("letter a in {0} found {1} times".format(arg, arg.count("a")))




