print("Hello World!")

# print(self, *args, sep=' ', end='\n', file=None):
# self - Ignore as of now as (oops) concept
# * args - defines that you can add unlimited numbers of comma separated arguments.
# sep=' ' as this defines space b/w arguments but you can any other symbol instead of space
# Note : sep can never be at the beginning of the line for output
# end='\n' is the new line but if you write (end="*") with any characters in the double quote then no new line is there

print("Puneet", "belongs", "to", "Punjab")
print("Puneet", "belongs", "to", "Punjab", "and", "has DOB", 1995)
print("Puneet", "belongs", "to", "Punjab", "and", "has DOB", 1995, True, 1.234)
print("Puneet", "belongs", "to", "Punjab", "and", "has DOB", 1995, True, 1.234, sep='$')
print("Puneet", "belongs", "to", "Punjab", "and", "has DOB", 1995, True, 1.234, sep='$',
      end="_")  # if we use (end='\n') then new line will print in the console
print("Puneet", "belongs", "to", "Punjab", "and", "has DOB", 1995, True, 1.234)

# IndentationError: Unexpected Error (It comes when you add space at the start of the line and you can automatically correct it by using reformat code)
print("Puneet", "belongs", "to", "Punjab", "and", "has DOB", 1995, True, 1.234)
