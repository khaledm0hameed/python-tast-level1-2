#Create a function that takes x,y and prints all the number that can be divide by y from x to 100
def print_divisible_numbers(x: int, y: int):
    for i in range(x, 101):
        if i % y == 0:
            print(i)
