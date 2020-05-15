import random

result = []

head_streak = 0
tail_streak = 0

head_streak_index = []
tail_streak_index = []

for i in range(10000):
	result.append(random.choice(['H','T']))

for index, value in enumerate(result):	
	try:
		if (result[index] == result[index+1] == result[index+2] == result[index+3] == result[index+4] == result[index+5]  and result[index] == 'H'): 
			head_streak = head_streak + 1
			head_streak_index = [index,index+1,index+2,index+3,index+4,index+5]
			print(head_streak_index)
			print(result[index:index+6])
		elif (result[index] == result[index+1] == result[index+2] == result[index+3] == result[index+4] == result[index+5] and result[index] == 'T'): 
			tail_streak = tail_streak + 1
			tail_streak_index = [index,index+1,index+2,index+3,index+4,index+5]
			print(tail_streak_index)
			print(result[index:index+6])
		else:
			pass

	except IndexError:
		pass
	
print('Head Streak: '+ str(head_streak))
print('Tail Streak: '+ str(tail_streak))

print('H: '+ str(result.count('H')))
print('T: '+ str(result.count('T')))



#print(result)


	
