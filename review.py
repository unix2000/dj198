#!/usr/bin/env python35
#python 3 review
data = ['acme', 50, 91.1, (2012,12,21)]
#必须下划线
_, shares, price, _ = data

record = ('liner', 'liner.xie@qq.com', '773-999-878', '878-678-999')
name, email, *phone_numbers = record
print(phone_numbers) #['773-999-878', '878-678-999'] 跟ruby类似

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args, sep="/"):
	return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

def f(ham: str, eggs: str = 'eggs') -> str:
	print("Annotations:", f.__annotations__)
	print("Arguments:", ham, eggs)
	return ham + ' and ' + eggs
f('spam')

#Scopes and Namespaces Example
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
	
	def __del__(self):
		pass

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


