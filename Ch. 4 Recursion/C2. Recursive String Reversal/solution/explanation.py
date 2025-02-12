def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

# When we call 
reverse_string("cat")

# First call:
s = "cat"
len(s) = 3 # not zero, so continue
s[1:] = "at" # gets all characters after index 0
s[0] = "c"   # gets first character
# calls reverse_string("at") + "c"

# Second call:
s = "at"
len(s) = 2 # not zero, so continue
s[1:] = "t" # gets all characters after index 0
s[0] = "a"  # gets first character
# calls reverse_string("t") + "a"

# Third call:
s = "t"
len(s) = 1 # not zero, so continue
s[1:] = "" # gets all characters after index 0
s[0] = "t" # gets first character
# calls reverse_string("") + "t"

# Fourth call:
s = ""
len(s) = 0 # is zero!
# returns ""

# Now the calls unwind, adding characters in reverse:

"" + "t" = "t"
"t" + "a" = "ta"
"ta" + "c" = "tac"

# The resulting string isn’t stored in a variable - it’s built up through the return values of each recursive call on the call stack. Let me show you with a modification that helps visualize this:

def reverse_string(s):
    print(f"Called with string: {s}")
    if len(s) == 0:
        print("Hit base case, returning empty string")
        return s
    result = reverse_string(s[1:]) + s[0]
    print(f"Building result: {result}")
    return result

# Let's try with "hi"
print(reverse_string("hi"))

# This would output something like:

# Called with string: hi
# Called with string: i
# Called with string: 
# Hit base case, returning empty string
# Building result: i
# Building result: ih
# ih

# Each recursive call’s return value is temporarily held in the call stack (computer’s memory) until all the calls complete. Think of it like a stack of papers:

# First call waits for reverse_string("i") + "h"
# Second call waits for reverse_string("") + "i"
# Third call returns ""
# Second call can now complete "" + "i" = "i"
# First call can now complete "i" + "h" = "ih"