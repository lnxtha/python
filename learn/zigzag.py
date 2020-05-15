z = '*****'
flag = True
i = 0
j = 0
import time
import sys

while True:
	try:

		if (j == 5):
			flag = False
		elif (j==0):
			flag = True

		if (flag):
			z = z+ ' '
			#print(flag)
			print(z[::-1])
			j = j+1
			#print('space count: '+str(z.count(' ')))
			#print(str(i)+ ': from top' )
			time.sleep(0.15)
			
		else:
			l = len(z)-1
			z = z[:l]
			#print(flag)
			j = j-1			
			print(z[::-1])
			#print('space count: '+str(z.count(' ')))
			#print(str(j)+ ': from bottom' )
			time.sleep(0.15)	



	except KeyboardInterrupt:
		print('This program should now end !!...')
		sys.exit()
				

	
			
				
	
