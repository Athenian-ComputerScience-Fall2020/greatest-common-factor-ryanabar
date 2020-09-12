# Greatest common factor

## Problem Description
In this assignment, you will make a function to determine the greatest commo factor between two numbers. There are many ways to do this. The important thing is that yur function returns the "GCF".


## Example
```
X = 4
y = 6

gcf = 2
```

## Suggested Approach (this is only one way - feel free to choose another way!)
1) The GCF is the largest number that divides both input numbers evenly. Consider using the % operator.
2) Use nested loops. The outer loop can be used to find a factor of the first number and a nested loop inside that can be used to check if it is a factor of the second.
3) Consider using "break" and "continue" to control the flow in your loops.
4) Be sure to return the gcf.

## Hints
* Use the section under `if __name__ == '__main__': ` to change arguments and check your work.
* There is a print statement there already. Feel free to change the numbers. You can also copy and paste more of them (and change those numbers) to check multiple combinations at once.
* When you are happy with your code, comment the print(s) out and use the `input()` statements below them to prompt the user for values.
* Add code to [my_code.py](./my_code.py) to make it do the desired thing.
* Run your code with: `python my_code.py` or the run button
* Run your tests with: `pytest`

