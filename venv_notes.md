Steps for Venv (transfer information to Zet)

    0. Create venv

        - Command: python -m venv venv_name (.venv is standard practice)

        - Do this one time to create the virtual environment

        - Is the .venv directory a script?

    1. Activate the environment 

        - Command: source .venv/bin/activate (assuming .venv is the directory's name)

        - This assumes I'm using bash/zsh; I'm using bash

        - Activation command depends on shell and operating system

        - I use bash; may be different for non-bash/zsh shells 

        - Learn shells

    2. Confirm activation works

        - Command: which python

        - make sure python points to the environment


    3. Execute python code in command

        - Command: python -c "import sys; print(sys.executable)

        - "In command" can be one or more statements separated by new lines

        - "python -c" runs a single python command; e.g. python -c "import numpy as np"

        - The above command imports sys and prints sys.executable

        




Sources: 

    - Documentation: https://docs.python.org/3/library/venv.html

    - Tutorial: https://mimo.org/tutorials/python/how-to-activate-a-virtual-environment-in-python

    - Reference: https://www.w3schools.com/python/python_virtualenv.asp



Other CS things to learn:

    - shells

    - kernels