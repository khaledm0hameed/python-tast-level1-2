#Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can be divided on x,y
def divisible_numbers(x:int, y:int):
    divisible_nums = [i for i in range(1, 101) if i % x == 0 and i % y == 0]
    return divisible_nums
