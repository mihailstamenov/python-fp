Let's trace through a small example to see how your code works. Let's use this simplified directory structure:

```python
{
    "Documents": {
        "notes.txt": None,
        "School": {
            "homework.pdf": None
        }
    }
}
```

Let's trace the steps:

1. First call to `list_files`:
    
    - `current_filepath` is ""
    - `path` becomes "Documents"
    - `filepath` = "" + "/Documents"
    - Since value is a dictionary, makes recursive call
2. Second level:
    
    - `current_filepath` is "/Documents"
    - First iteration:
        - `path` is "notes.txt"
        - `filepath` = "/Documents/notes.txt"
        - Value is None, so appends to list
    - Second iteration:
        - `path` is "School"
        - `filepath` = "/Documents/School"
        - Value is dictionary, makes recursive call
3. Third level:
    
    - `current_filepath` is "/Documents/School"
    - `path` is "homework.pdf"
    - `filepath` = "/Documents/School/homework.pdf"
    - Value is None, so appends to list

Final result would be:

```python
[
    "/Documents/notes.txt",
    "/Documents/School/homework.pdf"
]
```