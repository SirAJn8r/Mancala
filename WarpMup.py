import math

try:
    a = float(input("Type Things: "))
    print(math.sqrt(a))
except ValueError:
    print("Python doesn't know what i is. Sorry.")
except TypeError:
    print("That is not a number. Sorry.")
except OverflowError:
    print("You broke the brain capacity of the universe. Sorry.")
except Exception:
    print("Not a normal error. You really messed up this time. Sorry.")
    