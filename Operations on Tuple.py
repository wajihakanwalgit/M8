
my_tuple = ()
print(my_tuple)


my_tuple = (10, 20, 30)
print(my_tuple)

my_tuple = (42, "World", 7.5)
print(my_tuple)

my_tuple = ("cat", [1, 2, 3], (9, 8, 7))
print(my_tuple)


my_tuple = ('c','o','d','i','n','g')
print(my_tuple[0])   
print(my_tuple[5])   

n_tuple = ("dog", [11, 22, 33], (100, 200, 300))


print(n_tuple[0][2])       
print(n_tuple[1][2])      


print("Sliced :", my_tuple[1:4])


for letter in (my_tuple):
    print("Hi", letter)
