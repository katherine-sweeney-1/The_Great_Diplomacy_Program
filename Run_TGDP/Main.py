from Run_Main import run_tgdp
from Input_Commands_and_Commanders import *
import flask
import sys
sys.path.append("../The_Great_Diplomacy_Program/TGDP_Website")

#run_tgdp(input_data_sample, "9", "1903", False)
run_tgdp(input_data_6, "6", "1901", False)

"""

Arguments:

    1. Input data file

    2. Game number

    3. Starting year

    4. Boolean => save images (True), run GUI (False)

"""

"""

To Do

    - Fix winter turns: they need to be the destinations of fall turn successful attacks

    - paint bucket to change map color to match starting positions  

    - Submit moves on website

    - Submitting on website sends email to me

    - Show state of map without arrows for submitting moves at last turn

    - Show SQL table for moves on website

    - Different pages for current game and submitting moves

        => Check with Mercy

        => Have a map without arrows for submitting moves 

    - Eventually: make objects continuous with input? Need to look how backstabbr does this

    - DONE: Color changes

        - Successful attacks be green
        
        - Successful supports be blue

        - Orange for invalid move
    
    - DONE: Retreat Options for non-coastal fleet situations (i.e. the majority of the situations)

    - DONE: Fix Galecia coordinate => changed setting for Drawings_GUI

    - DONE: Invalid supports show up as failed supports

    - DONE: Have map for winter builds/tears

    - DONE: Show retreats on map

    - DONE: Show disbands

    - DONE: Add command.succeed to treeview

"""
