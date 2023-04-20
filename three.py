#Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
def multiplication_table(x, y):
    for i in range(x, y+1):
        print(f"Multiplication table of {i}:")
        for j in range(1, 13):
            print(f"{i} x {j} = {i*j}")
        print()
multiplication_table(1,2)