from multiprocessing.managers import convert_to_error

print("Puneet" + 32)    # TypeError: can only concatenate str (not "int") to str

# In Python - No concept of Concatenation

# If you want to print, you need to convert all variables into str (String)
print("Puneet" + str(32))
