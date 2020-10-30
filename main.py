from random import choice

names = {
	0:"Rock",
	1:"Paper",
	2:"Scissors"
}

def game():
	bot_play = choice([0,1,2])
	valid_play = False
	while valid_play == False:
		player_play = input("[0: " + names[0] + "] [1: " + names[1] + "] [2: " + names[2]+"]:\n")
		if (player_play == "0" or player_play == "1" or player_play == "2"):
			valid_play = True
			player_play = int(player_play)
	print("Player played " + names[player_play] + " and the bot played " + names[bot_play])
	result = check(player_play, bot_play)
	if result == -1:
		print("Bot Wins!")
	elif result == 1:
		print("Player Wins!")
	else:
		print("It's a tie")


def check(x, y):
	if x==y:
		return 0
	if (x-y)%3 == 1:
		return 1
	else:
		return -1

if __name__ == "__main__":
	game()
