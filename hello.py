# https://www.youtube.com/watch?v=k9TUPpGqYTo&t=349s&frags=pl%2Cwn
message = "Hello World"
# Slicing
# print(message[:5])
# print(message[6:])
# print(message.lower())
# print(message.count('l'))
# print(message.find('World'))  # returns starting position
# helloEno = message.replace('World', 'Eno')
# message = message.replace('World', 'Eno')
# print(helloEno)
# print(message)

greeting = 'Hello'
name = 'Blue'

# message = greeting + ", " + name
# message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
print(dir(name))  # shows all methods available to a string
print(help(str.lower))
