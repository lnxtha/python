eggs = 'global'

def spam():    
	global eggs
	eggs = 'spam local'
	print(eggs)    # prints 'spam local'
def bacon():
	eggs = 'bacon local'
	print(eggs)    # prints 'bacon local' 
	spam()
	print(eggs)    # prints 'bacon local'


bacon()
print(eggs)
