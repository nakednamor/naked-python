# methods are created using the def keyword and brackets
def first_method ():
    print("I'm the first method")

# methods are called as expected
first_method()

# methods can have arguments
def parameter_method(param1, param2, param3):
    print("passed param1: " + param1)
    print("passed param2: " + param2)
    print("passed param3: " + param3)

parameter_method("a", "b", "c")

# you can call a method using parammeter names
parameter_method(param1 = 'a', param2 = 'b', param3 = 'c')

# if you use parameter names, the order doesn't matter
parameter_method(param3 = 'c', param1 = 'a', param2 = 'b')

# methods can have default values
def method_with_defaults(param1, param2, param3 = "default param3"):
    print("passed param1: " + param1)
    print("passed param2: " + param2)
    print("passed param3: " + param3)

# default values are not applied if a value for the argument is passed
method_with_defaults("x", "y", "z")
method_with_defaults(param3="z", param2="y", param1="x")

# when you don't pass the parameter which is defined as default
# argument, the default value will be used
method_with_defaults(param2="y", param1="x")

# you can achieve the same with using parameter names - but than the
# argument with the default value has to be defined last
method_with_defaults("x", "y")

# you can have multiple default values
def everything_has_some_defaults(param1="default 1", param2="default 2",
    param3 = "default 3"):
    print("passed param1: " + param1)
    print("passed param2: " + param2)
    print("passed param3: " + param3)

everything_has_some_defaults()

# methods can return a value
def give_something_back(input):
    print("this is the input: " + input)
    return "some output"

output = give_something_back("some method input")
print("the method returns: " + output)


# when you you pass a list to a function, the function will alter the 
# original list ... if you don't want your list to be changed, you need
# to pass a copy of the list
original_list = ['a', 'b', 'c', 'd', 'e']
print(original_list)

def some_method_which_alters_the_argument(some_list):
    some_list.pop()

some_method_which_alters_the_argument(original_list)
print(original_list)


# you can define functions which take a not defined amount of arguments:
def do_stuff(*stuffs):
	print(len(stuffs))
	for stuff in stuffs:
		print stuff

do_stuff('a')
do_stuff('a', 'b')
