#In this exercise, we will know about the different Variable names
#123abc = 100   # This is invalid variable name as variable will not start with number, it should be alphanumeric
abc123 = 100  #alphanumeric variable name
_puneet = 92
_abc = 100
pi = 3.14
name = "Puneet Sharma"
isMale = True

# print(type(123abc)) - will not print as variable name is invalid

# Variable Type
print(type(abc123))  # <class 'int'>
print(type(_abc))    # <class 'int'>
print(type(_puneet)) # <class 'int'>
print(type(pi))      # <class 'float'>
print(type(name))    # <class 'str'>
print(type(isMale))  # <class 'bool'>

#Complex numbers data type i.e also defined as iota means root of -1
complex_number = 2+3j
print(complex_number)
print(complex_number.real)
print(complex_number.imag)
print(type(complex_number))
