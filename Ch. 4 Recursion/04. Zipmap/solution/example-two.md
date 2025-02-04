Here's a simple recursive function that builds a list of squared numbers in reverse order. It's similar to zipmap because it builds a data structure:

```py
def build_squares(n):
    if n == 0:
        return []
    res = build_squares(n - 1)  # get result from smaller problem
    res.append(n * n)           # add our piece to it
    return res                  # return modified structure

# Let's trace build_squares(3):

# Call 1: n = 3 (waiting)
res = build_squares(2)    # pauses here
# will append 9 later

    # Call 2: n = 2 (waiting)
    res = build_squares(1)    # pauses here
    # will append 4 later

        # Call 3: n = 1 (waiting)
        res = build_squares(0)    # pauses here
        # will append 1 later

            # Call 4: n = 0 (base case)
            return []    # returns to Call 3

        # Back to Call 3
        res = []        # got empty list
        res.append(1)   # adds 1
        return [1]      # returns to Call 2

    # Back to Call 2
    res = [1]          # got [1]
    res.append(4)      # adds 4
    return [1, 4]      # returns to Call 1

# Back to Call 1
res = [1, 4]          # got [1, 4]
res.append(9)         # adds 9
return [1, 4, 9]      # final result
```

Would you like to try predicting what build_squares(4) would produce? Try tracing through it like we did above!

```py
[1, 4, 9, 16]
```

Let's compare this to your zipmap function:

Both start with an empty structure ([] or {})
Both add one piece of data in each recursive step
Both build the final structure from bottom to top
The main pattern is:

Recurse down until you hit base case
Start with empty structure
Add one piece as you return up
Pass the modified structure back up
Now that you understand this pattern, can you think of why we needed the base case of `if len(keys) == 0 or len(values) == 0` in zipmap? Why do we need to check both lists?