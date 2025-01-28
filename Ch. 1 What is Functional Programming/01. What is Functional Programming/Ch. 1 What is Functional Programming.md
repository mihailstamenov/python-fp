# What Is Functional Programming?

Functional programming is a style (or "paradigm" if you're pretentious) of programming where we compose functions instead of mutating state (updating the value of variables).

- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming) is more about declaring _what_ you want to happen, rather than _how_ you want it to happen.
- [Imperative](https://en.wikipedia.org/wiki/Imperative_programming) (or procedural) programming declares both the _what_ and the _how_.

**Example of imperative code:**

```py
car = create_car()
car.add_gas(10)
car.clean_windows()
```

**Example of functional code:**

```py
return clean_windows(add_gas(create_car()))
```

The important distinction is that in the functional example, we never change the value of the `car` variable, we just compose functions that return new values, with the outermost function, `clean_windows` in this case, returning the final result.

## Doc2Doc

In this course, we're working on "Doc2Doc", a command line tool for converting documents from one format to another. If you're familiar with [Pandoc](https://pandoc.org/), the idea is similar.

## Assignment

Complete the `stylize_title` function. It should take a single string as input, and return a single string as output. The returned string should have both the title centered and a border added.

- Use the provided functions `center_title` and `add_border`.
- Center the title _before_ adding the border.
- Do not create any variables.
- Use only 1 line of code in the function body.