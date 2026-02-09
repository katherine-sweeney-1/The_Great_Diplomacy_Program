from Run_Main import run_main_process_moves
from Input_Commands_and_Commanders import *
import sys
sys.path.append("../The_Great_Diplomacy_Program/GUI")
from Functions_GUI import run_gui

game_objects = run_main_process_moves(input_data_8b, "8")
gui = run_gui(game_objects)