class People:
    def __init__(self, name, sex, age):
        self._name = name
        self._sex = sex
        self._age = age

    def __hash__(self):
        return hash((self._name ,self._sex, self._age))

    def __eq__(self, other):
        return (self._name, self._sex, self._age) == (other._name, other._sex, other._age)

    def __ne__(self, other):
        return not (self == other)

if __name__ == '__main__':
    James = People('James', 'M', 28)
    Tom = People('Tom', 'M', 22)
    print(James != Tom)
