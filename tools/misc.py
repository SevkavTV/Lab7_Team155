from random import choice, randint

from ulam_numbers import *
from happy_numbers import happy_numbers
from prime_numbers import *

def random_grid(grid_width: int, 
                number: int, 
                ulams: bool, 
                happy: bool, 
                prime: bool) -> (list, list):
    """
    Returns a list of lists of grid_width with random numbers
    in ratio depending on booleans ulam, happ
    Exmaple:
    >> random_grid(4, 100, True, False, False)
       [ [1, 22, 69, 53],
         [3, 13, 66, 38],
         [16, 18, 26, 4],
         [48, 10, 20, 7] ]

    """
    grid = []
    correct_list = []
    # all_num_list = [el for el in range(number)]
    
    if ulams: 
        for elem in ulam_numbers(number):
            if elem not in correct_list:
                correct_list.append(elem)
    if prime:
        for elem in prime_numbers(number):
            if elem not in correct_list:
                correct_list.append(elem)
    if happy:
        for elem in happy_numbers(number):
            if elem not in correct_list:
                correct_list.append(elem)

    incorrect_list = [num for num in range(number) if num not in correct_list]

    while len(grid) < (grid_width ** 2):
        coef = randint(1, 3)

        if coef == 1:
            grid.append(choice(correct_list))

        else:
            grid.append(choice(incorrect_list))

    return grid, correct_list


def printer(width, grid):
    """
    Printer
    """
    for num in range(int(width ** 2)):
        if (num + 1) % width != 0 or (num == 0):
            print("|{}|".format(grid[num]), end="\t")
        else:
            print("|{}|".format(grid[num]), end="\n\n")

        
def gamestart():

    print("----" * 15)
    ulams = input("Do you want to play with ulam_numbers? (Yes/No) \n")
    if ulams.strip().lower() == "yes":
        ulams = True
    else:
        ulams = False

    print("----" * 15)
    happy = input("Do you want to play with happy_numbers? (Yes/No) \n")
    if happy.strip().lower() == "yes":
        happy = True
    else:
        happy = False

    print("----" * 15)
    prime = input("Do you want to play with prime_numbers? (Yes/No) \n")
    if prime.strip().lower() == "yes":
        prime = True
    else:
        prime = False
    
    if not prime and not happy and not ulams:
        print("----" * 15)
        print("You have to choose at least one game mode!")
        print("----" * 15)
        answer = input("Do you want to play the game again? (Yes/No) \n")
        if answer.strip().lower() == "yes":
            gamestart()
        else:
            exit()

    print("----" * 15)
    width = int(input("Which board size you want? (4-8) \n"))
    
    return width, 100, ulams, happy, prime


if __name__ == "__main__":
    cheers = ["You are the best!", "Great job my man!", "OMG, you did it!!!", "Fabulous"]
    grid_param = gamestart()
    grid, corrects = random_grid(*grid_param)

    message = "Find: "
    if grid_param[2]:
        message += "(ulam_numbers) "
    if grid_param[3]:
        message += "(happy_numbers) "
    if grid_param[4]:
        message += "(prime_numbers) "
    
    grid_corrects = [num for num in corrects if num in grid]

    while len(grid_corrects) > 0:

        print("----" * 15)
        print(message)
        print()
        printer(len(grid)**(0.5), grid)
        print("----" * 15)
        answer = int(input("Pick a number \n"))
        if answer in grid_corrects:
            for pos, value in enumerate(grid):
                if value == answer:
                    grid[pos] = "++"
            grid_corrects.remove(answer)
            print()
            print(choice(cheers))
            print()
        else:
            print("----" * 15)
            print("\nGAME OVER\n")
            print("Numbers left: {}\n".format(grid_corrects))
            print("----" * 15)
            exit()

    print("----" * 15)
    print("\nYOU WON THE GAME!!!\n")
    print("----" * 15)

# corrects list is bigger than the grid and I need to extract all grid corrects before i start the loop




    


        


