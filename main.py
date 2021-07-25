import random
import matplotlib.pyplot as plt

def monty_hall(ndoors, kopen, switch=True, show_selections=False):
	assert(ndoors - kopen > 0 and kopen >= 0)
	if ndoors-kopen == 1: return True
	"""
	Randomly choose a door between 1 and ndoors
	"""
	door_chose = random.randint(1, ndoors)
	"""
	Randomly choose a winning door with car between 1 and ndoors
	"""
	door_win = random.randint(1, ndoors)

	if switch: # If switch is True open k doors

		# doors which can be opened
		doors = [door for door in range(1, ndoors+1) if door not in (door_chose, door_win)]

		# List of the doors opened randomly
		revealed_doors = random.sample(doors, kopen)

		# The doors which are left to be opened
		left_doors = [door for door in range(1, ndoors+1) if door not in (*revealed_doors, door_chose)]
		# print(left_doors)
		
		# Again choose a random door other than the first one
		prev_selection = door_chose
		door_chose = random.choice(left_doors)


	if show_selections:
		if switch: print(f"You chose door: {prev_selection} and switched to door: {door_chose} Car was behind : {door_win}")
		else: print(f"You chose door: {prev_selection} Car was behind : {door_win}")

	return door_chose == door_win

def run_simulation(n, ndoors, kopen, switch=True):
	wins = 0
	loss = 0
	win_percentage = []
	for i in range(n):
		res = monty_hall(ndoors, kopen, switch)
		if res: wins += 1
		else: loss += 1
		win_percentage.append(wins/(wins + loss))
	return wins, loss, win_percentage

def main():
	N = 15000
	DOORS = 3
	OPEN_NUM = 1
	SWITCH = True


	wins, loss, win_percentage = run_simulation(n=N, ndoors=DOORS, kopen=OPEN_NUM, switch=SWITCH)

	plt.figure(figsize=(12.2,4.5))
	plt.plot(range(1, N + 1), win_percentage,
				label = f'Win ratio after {N} trials: {win_percentage[-1]:0.2f}')

	plt.fill_between( range(1, N+1), win_percentage, alpha = 0.7)

	plt.xlabel('Number of Trials')
	plt.ylabel('Win Ratio')

	plt.legend(title = f"{DOORS} doors with {OPEN_NUM} revealed; switch : {SWITCH}")
	plt.show()

if __name__ == '__main__':
	main()