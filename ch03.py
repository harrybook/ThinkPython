def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day")

# repeat_lyrics()

def right_justify(str, size):
    print((size - len(str))*" " + str)

# right_justify("allen", 70)

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_spam():
    print("spam")

# do_twice(print,"spam")

def print_twice(str):
    do_twice(print, str)

# print_twice("spam")


# do_twice(print_twice, "spam")

def do_four(f, str):
    do_twice(f, str)
    do_twice(f,str)

do_four(print,"spam")