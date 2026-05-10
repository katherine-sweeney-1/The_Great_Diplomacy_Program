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

run_tgdp(input_data_8, "8", "1901", False)