board = {
'top-l':'',
'top-m':'',
'top-r':'',
'mid-l':'',
'mid-m':'',
'mid-r':'',
'bot-l':'',
'bot-m':'',
'bot-r':'',
}
turn = True

def display():
	print(board['top-l']     + ' | ' + board['top-m'] + ' | ' + board['top-r'] )
	print('-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-')
	print(board['mid-l']     + ' | '  + board['mid-m'] + ' | ' + board['mid-r'] )
	print('-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-'+'-')
	print(board['bot-l']     + ' | ' + board['bot-m'] + ' | ' + board['bot-r'] )


def get_input():
	global turn
	if (turn):
		turn = False
		print('Player one turn')
		print('Choose your position as (top|mid|bot)-(l|m|r)')
		one = input('Get value\n')
		update_board(one,'1')
	
	else:
		turn = True
		print('Player two turn')
		print('Choose your position as (top|mid|bot)-(l|m|r)')
		two = input('Get value\n')
		update_board(two,'2')

def check_winner():
	for key in list(board.keys()):
		

def update_board(position,player):
	if player == '1':
		board[position] = 'X'
	elif player == '2':
		board[position] = 'O'


while True:
	get_input()	
		
	
	display()





