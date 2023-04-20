#Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in the x,y range
def even_odd_numbers(x:int,y:int):
    odd=[i for i in range(int(x), int(y)+1) if i % 2 != 0]
    even=[i for i in range(int(x), int(y)+1) if i % 2 == 0]
    print(f'''          odd numbers is {odd}
          even numbers is {even}''')
    


