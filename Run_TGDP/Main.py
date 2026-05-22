from Run_Main import run_tgdp
from Input_Commands_and_Commanders import *
import flask
import sys
sys.path.append("../The_Great_Diplomacy_Program/TGDP_Website")

"""

Arguments:

    1. Input data file

    2. Game number

    3. Starting year

    4. Boolean => save images (True), run GUI (False)

"""

"""

To Do

    - Show units that retreat on map

    - Show units that diband on map

    - paint bucket to change map color to match starting positions  

    - Submit moves on website

    - Submitting on website sends email to me

    - Show state of map without arrows for submitting moves

    - Different pages for current game and submitting moves

        => Check with Mercy

        => Have a map without arrows for submitting moves 

    - Eventually: make objects continuous with input? Need to look how backstabbr does this

    - DONE: Color changes

        -  successful attacks be green
        
        - successful supports be blue

        - orange for invalid move
    
    - DONE: Retreat Options for non-coastal fleet situations (i.e. the majority of the situations)

    - DONE: fix Galecia coordinate => changed setting for Drawings_GUI

    - DONE: invalid supports show up as failed supports

    - DONE: Have map for winter builds/tears

"""

#run_tgdp(input_data_sample, "9", "1903", False)
run_tgdp(input_data_8, "8", "1901", False)
