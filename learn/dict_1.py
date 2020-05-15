# To count how many times each character appear in this string

message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 

counter = {}

for character in message:
	counter.setdefault(character, 0)
	counter[character] = counter[character] + 1	#incrementor

for key,value in  sorted(count.items()):
	print(key,value)
