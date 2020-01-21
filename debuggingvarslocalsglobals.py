#If you call vars() within a function, then it returns a dictionary of all local variables including global varaibles.  However, if you declare a varaible inside a function global, then it doesn't show up.
#If you call vars() or Locals() outside a function, then it returns thesame results as calling globals() which returns a dictionary of global variables.

x = 100
def foo3(y):	
	z = 300
	asecret = 400
	print("vars",vars())
foo3(2000) #print vars {'asecret': 400, 'z': 300, 'y': 2000}
for key, value in sorted(vars().items()):
	print("{0} = {1}".format(key, value))
	'''
	__annotations__ = {}
	__builtins__ = <module 'builtins' (built-in)>
	__cached__ = None
	__doc__ = None
	__file__ = quickpractice.py
	__loader__ = <_frozen_importlib_external.SourceFileLoader object at 0x7f25f729e080>
	__name__ = __main__
	__package__ = None
	__spec__ = None
	foo3 = <function foo3 at 0x7f25f72c1e18>
	x = 100
	'''
print(globals())
'''
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7ff39aa4c080>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'quickpractice.py', '__cached__': None, 'x': 100, 'foo3': <function foo3 at 0x7ff39aa6fe18>, 'key': 'x', 'value': 100}
'''
for key, value in globals().items():
	print(key, value)
'''
__name__ __main__
__doc__ None
__package__ None
__loader__ <_frozen_importlib_external.SourceFileLoader object at 0x7ff39aa4c080>
__spec__ None
__annotations__ {}
__builtins__ <module 'builtins' (built-in)>
__file__ quickpractice.py
__cached__ None
x 100
foo3 <function foo3 at 0x7ff39aa6fe18>
key foo3
value foo3
'''
x = 100
def foo(y):
	z = 300
	asecret = 400
	print("vars",vars())
	print("locals",locals())
foo(2000) #print vars {'asecret': 400, 'z': 300, 'y': 2000}\n locals {'asecret': 400, 'z': 300, 'y': 2000}

x = 100
def foo2(y):
	global z
	z = 300
	asecret = 400
	print("vars",vars())
	print("locals",locals())
foo2(2000) #print vars {'asecret': 400, 'y': 2000}\n locals {'asecret': 400, 'y': 2000}
