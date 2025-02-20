def css_styles(initial_styles):
    styles = initial_styles.copy()

    def add_style(selector, property, value):
        if selector not in styles:
            styles[selector] = {}
        styles[selector][property] = value
        return styles

    return add_style