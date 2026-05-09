_____________________________________________________________________________________________________



Create image locally of moves on map, save the image with the arrows et al, upload that image to website


Different ways to look at map => side by side view 
- not tricky
- create standard view (one image) and comparison view map (two images)
- next turn => image on right goes to image on left

Have a page that adds all images to file. Can append most recent turn's image to the end of the page



_____________________________________________________________________________________________________

Commander Class

    Completed

        => Create commander objects (1)

        => Add unit objects to commander's members (4a)

        => Add node objects to commander's dots_owned (4c)

        => Add node objects to commander's dots (4d)

        => add node objects to commander's hsc (4e)

    To Do

        => Add commander.orders to give all of a commander's commands for a turn?


Node

    Completed

        => Create node object (2a)

        => Create special case coastal node object subclass with parent and sibling node functions (2b)

        => Node object has unit object for "is_occ" if a unit object occupies the node (5a)

        => is occupied for node subclass so if one of subclass family nodes is occupied then 
        all three in the family are occupied (5b)

        => Node dictionary and coastal node dictionary are combined (2c)

        => Node object has dot status (2d)
        
        => Node object has home supply center status (2e)
    

UNIT CLASS

    Completed

        => Create unit objects (3a)

        => Assign location as a node object to unit object (3b)

        => Assign commander to unit object (3c)

        => Create unit dictionary (4b)

    To Do

        => Add unit.command function? 


COMMAND CLASS

    Completed

        => Create command objects (6a)

        => Assign commander object to command object (6b)

        => Assign location, origin, and destination as node objects to command object (6c)
    
        => Assign unit object to command object (6d)


FILTERING MOVES

    Completed

        => Unit must exist

        => Unit for command must belong to correct human

        => Fleets must move to coast or seas

        => Armies must move to coast or inland

        => Location and destination must be neighbors (need to do origin and destination)

        => Location and destination must be neighbors and origin and destination must be neighbors


Processing Moves

    Completed

        => Determine outcomes of orders

        => Continue to debug


Post Outcome

    Completed
    
        => Determine if a unit is displaced

        => Determine retreat options (holding off on disband for now)

        => Update units with new locations

        => Update nodes with new occupy status

        => turn count





Notes on Rules

    units can trade places with a convoy

    support can be given without consent and cannot be refused

    Cannot let fleets move from Stp-SC to Stp-NC
    fleets can move from Bul-EC to Bul-SC and Spa-SC to Spa-NC

    Diagram 13 in rulebook is the tricky one to implement
        -   if an attack from origin 1 dislodges unit X, and unit X and unit Y attack origin 1, then 
            unit Y gains origin 1 
        -   This is instead of it being a stalemate between unit X and unit Y
        -   Issue: an attack is invalid if another attack succeeds' on the unit's origin
        -   this is where recursion happened last time

    Take note of diagram 17


SQL

UPDATE table_name SET Origin="xyz", Destintaition = "abc" WHERE UNIT_ID = "AU01";

add command ID for command objects? Right now it uses units for ID's

python debugger json
cmd line debugger

nodes[node].is_occ shows the occupied status for the first turn 

____________________________________________________________________________________________



Eventually Include

    - retreats => check if this actually works

    - builds/tears

    - Continuity of game so it runs as one game and not isolated moves

    - I think the filter owners is not implemented in the program 

