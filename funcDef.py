# def hello_func():
#     # use 'pass' to save an empty function
#     return 'Hello Function!'


# hello_func()
# print(hello_func().upper())


# def hello_name(greeting='Howdy', name='Toki'):
#     return f'{greeting}, {name}'


# print(hello_name('Hello', 'Blue'))
# print(hello_name())


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# list
games = ['chess', 'twister', 'frisbee']
# tuple
pets = ('Toki', 'Eno', 'Blue')
# dictionary
info = {"phone": '555-123-4567', "email": 'jam@stardust.com'}
student_info(*games, **info)
