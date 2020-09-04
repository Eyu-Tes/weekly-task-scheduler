from django import template

register = template.Library()


@register.filter(name='add_classes')
def add_classes(value, arg):
    """
    Add provided classes to form field
    :param value: form field
    :param arg: string of classes seperated by ' '
    :return: edited field
    """

    print('----------------------Inside custom_tags.py--------------------')
    print(value)
    print()
    print(type(value))
    print(value.field)
    print(type(value.field))
    print(value.field.widget)
    print(type(value.field.widget))
    print(value.field.widget.attrs)
    print(type(value.field.widget.attrs))
    print(arg)
    print(type(arg))
    print('---------------------------------------------------------------')

    css_classes = value.field.widget.attrs.get('class', '')

    # check if class is set or empty and split its content to list (or init list)
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []

    # prepare new classes to list
    args = arg.split(' ')
    for a in args:
        if a not in css_classes:
            css_classes.append(a)

    # join back to single string
    return value.as_widget(attrs={'class': ' '.join(css_classes)})

    # or
    # value.field.widget.attrs.update({'class': ' '.join(css_classes)})
    # return value


@register.filter(name='haha')
def append(value, arg):
    print(f'{value} ----- {type(value)}')
    print(f'{arg} ----- {type(arg)}')
    temp = value + arg
    return temp
