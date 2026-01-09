from Run_Main import run_main_original, run_main_testing, run_main_unit_testing
from Input_Commands_and_Commanders import *
import sys
sys.path.append("../The_Great_Diplomacy_Program/GUI")
from Functions_GUI import run_gui
#run_main_testing()
game_objects = run_main_unit_testing(input_data_8, "8")

gui = run_gui(game_objects)