from PySide2 import QtGui, QtWidgets, QtCore
from importlib import reload
import sys
import methodNames
import inspect

reload(methodNames)

method_names = {}

for name, obj_l1 in inspect.getmembers(methodNames):
    if inspect.isclass(obj_l1):
        print(obj_l1.__name__)
        obj_l2 = inspect.getmembers(obj_l1, predicate=inspect.isfunction)

        valueNames = tuple(i[0] for i in obj_l2 if 'Button function:' in i[1].__doc__)
        valueDetails = tuple(i[1].__doc__ for i in obj_l2 if 'Button function:' in i[1].__doc__)
        valueDict = {'valueNames': valueNames, 'valueDetails': valueDetails}
        method_names[obj_l1.__name__] = valueDict
        print(method_names)


methods_names1 = {'StringModules': {'valueNames': ('plus', 'plusReverse'),
                                    'valueDetails': (
                                    'concatenate words in straight order', 'concatenate words in reverse order')
                                    },
                  'SymbolModules': {'valueNames': ('tSearch', 'aSearch'),
                                    'valueDetails': ('returns how many times "t" in string "tatiana"',
                                                     'returns how many times "a" in string "alejandro"')
                                    }
                  }


def doOpenUI():
    """
    Function used to call the instanciation of the tool avoiding
    the duplicate of leaving extra class behind
    """
    dial = None
    for qt in QtWidgets.QApplication.topLevelWidgets():
        if qt.__class__.__name__ == 'TestUi':
            dial = qt
            print(dial)

        if not dial:
            dial = TestUi(methods_names1)
            return dial
        else:
            dial.close()
            dial = TestUi(methods_names1)
            return dial


class TestUi(QtWidgets.QMainWindow):
    def __init__(self, dict_names, parent=None):
        super(TestUi, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.setWindowTitle('Dynamic Buttons')
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        central_layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(central_layout)

        for key, value in dict_names.items():
            setattr(self, key, TestWidget(key, value))
            central_layout.addWidget(getattr(self, key))


class TestWidget(QtWidgets.QMainWindow):
    # the class describing the widget for the class from methodNames
    def __init__(self, key, value, parent=None):
        super(TestWidget, self).__init__(parent)

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        widget.setMinimumSize(120, 80)

        layout = QtWidgets.QVBoxLayout()
        widget.setLayout(layout)
        layout.setContentsMargins(20, 10, 30, 10)

        label = QtWidgets.QLabel()
        label.setText(key)
        label.setMinimumSize(120, 15)
        # label.setAlignment()
        layout.addWidget(label)

        for i in range(len(value['valueNames'])):
            button = QtWidgets.QPushButton()
            button.setText(value['valueNames'][i])
            if value['valueDetails'][i]:
                button.setToolTip(value['valueDetails'][i])
            button.setMinimumSize(120, 15)
            layout.addWidget(button)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = TestUi(methods_names1)
    win.show()
    sys.exit(app.exec_())
