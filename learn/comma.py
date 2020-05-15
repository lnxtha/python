def fn(alist):
	final_string = ''
	if len(alist) < 2:
		print('Values less than 2')		
		return alist
	else:
		for i in alist:
			
			if (i == alist[-2]):
				final_string = final_string + i
				#print('1') 
			elif (i == alist[-1]):
				final_string = final_string + ' and ' + i
				#print('2')			
			else:
				final_string = final_string + i + ','
				#print('3')			
	return final_string


#ls = ['a','b','c','e','f','g','h','i','j','k','l']
lst = ['a']
print(fn(lst))
