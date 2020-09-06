# import traceback
import inspect

a = "tatiana"
b = "alejandro"


class PrintModules(object):

    @staticmethod
    def printStraight():
        """ Button function: """
        PrintModules.prints()

    @staticmethod
    def prints():
        """ Convenience function: """
        print(a)


class SymbolModules(object):

    @staticmethod
    def tSearch():
        """ Button function: returns how many times 't' in string 'tatiana' """
        toolTip = "tooltip string"
        print("letter 't' in {0} found {1} times".format(a, a.count("t")))

    @staticmethod
    def aSearch():
        """ Button function: returns how many times 'a' in string 'alejandro'"""
        print("letter a in {0} found {1} times".format(b, b.count("a")))

    @staticmethod
    def noSearch():
        """nothing"""
        return
