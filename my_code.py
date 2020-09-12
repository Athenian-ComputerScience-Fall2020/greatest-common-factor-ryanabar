# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# https://www.w3schools.com/python/python_operators.asp
# I used the one above to learn what the % operator does (This assingment became a lot easier after I learned that this exists :)
# https://www.mathsisfun.com/definitions/modulo-operation.html
# I used the one above to actually learn what modulo is because I have never used it before

def find_gcf(x,y):   # Do not change function name!
    # User code goes here
    if x > y:
        number = y
    else:
        number = x
    for i in range(1, number + 1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i
    return gcf




if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    x = int(input("Enter a  number: "))
    y = int(input("Enter another number: "))
    print(find_gcf(x,y))


    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

