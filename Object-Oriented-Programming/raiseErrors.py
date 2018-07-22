
# A class of list -> Only even numbers can be added to "EvenOnly" list.
class EvenOnly(list):
    def append(self,integer):
        if not isintance(integer,int):
            raise TypeError("Only integers can be added")

        if integer % 2:
            raise ValueError("Only even numbers can be added")

        super().append(integer)



# errors
def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never excute")
    return "I won't be returned"




def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100/anumber

    except ZeroDivisionError:
        return "Enter a number other than zero"

    except TypeError:
        return "Enter a numerical value"

    except ValueError:
        print("No,No,not 13!")



try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)


