"""

@ Bhaskara Rao Karri,
Date : 06/07/2020.
"""
# Import the required Modules on here.
import warnings

# Create a Testclass on here.  
class Test():
    pass

# Create a Test1class on here.  
class Test1():
    pass
# Define the functions with required arguments for Exception and checking the conditions that functions returns some value.  
def raise_function(var1):
    if var1 == 100:
        raise Exception(" Not a valid number")
    elif var1 == (u'\u4e2d\u6587'):
        raise Exception(" Not a valid number") 
    else:
        return True

# Define the functions with required arguments for warinings and checking the conditions that functions returns some value.  
def isZero(i):
    if i != 0:
        print("OK")
    else:
        warnings.warn("the input is 0!") 
    return i

# Define the add function  with required arguments on here and returns  Some value on here.
def add(variable):
    return sum(variable)

# Define the add function with required arguments on here and returns  Some value on here.
def lenght_function(variable):
    return len(variable)

# Define the grtaer_function function with required arguments and checking the conditions on here and returns  Some value on here.
def grtaer_function(variable1,variable2):
    if variable1 > variable2:
        return variable1

# Define the less_function function with required arguments and checking the conditions on here and returns  Some value on here.
def less_function(variable1,variable2):
    if variable1 < variable2:
        return variable1

# Define the collection_function function with required arguments and checking the conditions on here and returns  Some value on here.
def collection_function(variable):
    list1 =[]
    [list1.append(x) for x in variable] 
    if type(variable) == list:
        return list1
    elif type(variable) == tuple:
        return tuple(list1)
    elif type(variable) == str:
        return (''.join(list1))
    else:
        return set(list1)

# Define the float_equal function with required arguments on here and returns  Some value on here.
def float_equal(variable):
    return round(variable,7)

# Define the dict_function with required arguments and checking the conditions on here and returns  Some value on here.
def dict_function(variable1):
    if type(variable1) == dict :
         return variable1

# Define the count_function with required arguments on here and returns  Some value on here.
def count_function(var1,var2):
    return var1 + var2

# Define the membership_in_function with required arguments and checking the conditions on here and returns  Some value on here.
def membership_in_function(value1,value2):
    if value1 in value2:
        return value1
    
# Define the membership_notin_function with required arguments and checking the conditions on here and returns  Some value on here.
def membership_notin_function(value1,value2):
    if value1 not in value2:
        return value1
    
# Define the count_equall_function with required arguments and perform some operations on here and returns  Some value on here.
def count_equall_function(variable1):
    list1 = []
    [list1.append(x) for x in variable1]
    return list1