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


    - paint bucket to change map color to match starting positions  

    - Submit moves on website

    - Submitting on website sends email to me

    - Have map for winter builds/tears

    - Show state of map without arrows for submitting moves 

    - Different pages for current game and submitting moves

        => Check with Mercy

        => Have a map without arrows for submitting moves 

    - ASK MERCY: submit moves on discord or just show maps on discord? Is there a way to automate move submission via discord?

    - Fix galecia coordinate? Game 8 Boh support to galecia has arrow finishing in bohemia

    - DONE: Color changes

        -  successful attacks be green
        
        - successful supports be blue

        - orange for invalid move
    
    - DONE: Retreat Options for non-coastal fleet situations (i.e. the majority of the situations)

    - DONE: fix Galecia coordinate => changed setting for Drawings_GUI

"""

#run_tgdp(input_data_sample, "9", "1903", False)
run_tgdp(input_data_8, "8", "1901", False)

"""

MAP ISSUE - invalid supports show up as failed holds instead of failed supports

"""