class Parrot:


    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


rio = Parrot("Rio", 5)
mango = Parrot("Mango", 8)


print("Rio is a {}".format(rio.species))
print("Mango is also a {}".format(mango.species))


print("{} is {} years old".format(rio.name, rio.age))
print("{} is {} years old".format(mango.name, mango.age))
