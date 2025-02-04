```py
Solution explanation
```py
# Let's trace zipmap(["a", "b"], [1, 2])

# Call 1 (waiting for res)
res = zipmap(["b"], [2])     # Call 1 pauses here
# res[keys[0]] = values[0] will be: res["a"] = 1

    # Call 2 (waiting for res)
    res = zipmap([], [])     # Call 2 pauses here
    # res[keys[0]] = values[0] will be: res["b"] = 2

        # Call 3 (base case)
        return {}    # Returns to Call 2

    # Back to Call 2
    res = {}        # Got result from Call 3
    res["b"] = 2    # Adds entry
    return res      # Returns {"b": 2} to Call 1

# Back to Call 1
res = {"b": 2}      # Got result from Call 2
res["a"] = 1        # Adds entry
return res          # Final result: {"a": 1, "b": 2}
```
Each call waits for its recursive call to complete before adding its own key-value pair. Think of it like a stack of plates - you add plates (make calls) from top to bottom, but you remove them (resolve calls) from bottom to top!