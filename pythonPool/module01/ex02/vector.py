import sys


def check_vector(vector):
    if type(vector) is int and vector > 0:
        newVector = []
        for i in range(0, vector):
            item = []
            item.append(i)
            newVector.append(item)
        return newVector

    if type(vector) is tuple:
        newVector = []
        for i in range(vector[0], vector[1]):
            item = []
            item.append(i)
            newVector.append(item)
        return newVector

    if type(vector) is list:
        if type(vector[0]) is list:
            for value in vector:
                if len(value) != 1:
                    print("Column Must have lists of size one floats or int")
                    return False
                if type(value[0]) not in (int, float):
                    print("Column Values should be of type int or float")
                    return False
            return "Column"
        if type(vector[0]) in (int, float):
            for value in vector:
                if type(value) not in (int, float):
                    print("Row should contain only int or float values")
                    return False
            return "Row"
    return False


class Vector:
    def __init__(self, values):
        if type(check_vector(values)) is list:
            self.values = check_vector(values)
            if check_vector(self.values) == "Column":
                self.shape = (len(self.values), 1)
            elif check_vector(self.values) == "Row":
                self.shape = (1, len(self.values))
        elif check_vector(values) in ("Column", "Row"):
            self.values = values
            if check_vector(self.values) == "Column":
                self.shape = (len(self.values), 1)
            elif check_vector(self.values) == "Row":
                self.shape = (1, len(self.values))
        elif check_vector(values) is False:
            sys.exit()

    def __add__(self, value):
        if isinstance(value, Vector) and isinstance(self, Vector):
            if self.shape == value.shape:
                newVector = []
                if self.shape[0] != 1:
                    anotherValue = []
                    for item1, item2 in zip(self.values, value.values):
                        anotherValue = []
                        anotherValue.append(item1[0] + item2[0])
                        newVector.append(anotherValue)
                    return newVector
                else:
                    for item1, item2 in zip(self.values, value.values):
                        newVector.append(item1 + item2)
                    return newVector
            else:
                print("Only Vectors of the same dimensions")
                sys.exit()
        else:
            print("Only Vectors")
            sys.exit()

    def __radd__(self, value):
        newValue = self.__add__(self, value)
        return newValue

    def __sub__(self, value):
        if isinstance(value, Vector) and isinstance(self, Vector):
            if self.shape == value.shape:
                newVector = []
                if self.shape[0] != 1:
                    anotherValue = []
                    for item1, item2 in zip(self.values, value.values):
                        anotherValue = []
                        anotherValue.append(item1[0] - item2[0])
                        newVector.append(anotherValue)
                    return newVector
                else:
                    for item1, item2 in zip(self.values, value.values):
                        newVector.append(item1 - item2)
                    return newVector
            else:
                print("Only Vectors of the same dimensions")
                sys.exit()
        else:
            print("Only Vectors")
            sys.exit()

    def __rsub__(self, value):
        return self.__sub__(value, self)

    def __mul__(self, value):
        if isinstance(self, Vector) and type(value) in (int, float):
            if check_vector(self.values) == "Row":
                newValue = []
                for item in self.values:
                    newValue.append(item * value)
            if check_vector(self.values) == "Column":
                newValue = []
                for item in self.values:
                    anotherValue = []
                    anotherValue = item[0] * value
                    newValue.append(anotherValue)
                return newValue
        else:
            print("only Scalars (int, float)")
            sys.exit()

    def __rmul__(value, self):
        return self.__mul__(value, self)

    def __truediv__(self, value):
        if isinstance(self, Vector) and type(value) in (int, float):
            if value == 0:
                print("can't div by 0")
                sys.exit()
            if check_vector(self.values) == "Row":
                newValue = []
                for item in self.values:
                    newValue.append(item / value)
            if check_vector(self.values) == "Column":
                newValue = []
                for item in self.values:
                    anotherValue = item[0] / value
                    newValue.append(anotherValue)
                return newValue
        else:
            print("only Scalars (int, float)")
            sys.exit()

    def __rtruediv__(self, value):
        print("A scalar cannot be divided by a Vector.")
        sys.exit()

    def __str__(self):
        return f"\n\rVector = {self.values}\
            \n\rShape = {self.shape}"

    def __repr__(self):
        return f"\n\rVector = {self.values}\
            \n\rShape = {self.shape}"

    def dot(self, vector):
        if isinstance(self, Vector) and isinstance(vector, Vector):
            if self.shape == vector.shape:
                if check_vector(self.values) == "Column":
                    newVector = []
                    for item1, item2 in zip(self.values, vector.values):
                        anotherVector = []
                        anotherVector.append(item1[0] * item2[0])
                        newVector.append(anotherVector)
                    return newVector
                elif check_vector(self.values) == "Row":
                    newVector = []
                    for item1, item2 in zip(self.values, vector.values):
                        newVector.append(item1 * item2)
                    return newVector
            else:
                print("only Vectors of same shape")
                sys.exit()
        print("only Vectors")

    def T(self):
        if isinstance(self, Vector):
            if check_vector(self.values) == "Row":
                newValue = []
                for item in self.values:
                    anotherValue = []
                    anotherValue.append(item)
                    newValue.append(anotherValue)
                return newValue
            elif check_vector(self.values) == "Column":
                newValue = []
                for item in self.values:
                    newValue.append(item[0])
                return newValue
        else:
            print("Only Vectors")
            sys.exit()
