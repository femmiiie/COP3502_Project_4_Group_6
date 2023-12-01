from board import Board

#replaces old state checking for simplicity
state = "menu"
possible_states = ["menu", "game", "win", "loss"]

#Mostly Obsoleted, Still Here For Consistency
running = True

#Determines Whether To Render Menu Or Game
in_menu = True

#Determines Whether Win/Lose Screen Should Be Displayed
game_finished = False

#Determines Which Of The Win/Lose Screens to Display
correct_solution = False

#Global Board Object
#Set To Empty Board Type When No Game Is Active
board = Board