"""
Convoy affected outcomes

    Game 1

        1903 Spring: GE02

        1905 Fall: RU07

        1907 Spring: RU08

    Game 2

        1902 Fall: RU04

        1903 Spring: GE02

    Game 3

        1903 Fall: GE02

        1908 Fall: RU04

    Game 4

        1901 Fall: RU04
    
    Game 7

        1901 Fall: AU02
    
    Game 8

        1905 Spring: FR01

        1905 Fall: IT01

        1905 Fall: IT02

        1912 Spring: TU07

        1914 Spring: UK08

        1914 Spring: TU09 => convoy cut support


Invalid Move Affected Outcomes

    Game 1

        1905 Spring: RU02

        1906 Spring: RU02

        1908 Spring: RU11
    
    Game 2

        1901 Spring: RU03

        1902 Fall: TU01

        1903 Fall: GE02

        1905 Spring: IT04

    Game 3

        1902 Spring: IT04

        1904 Spring: AU02

        1904 Fall: AU02

        1905 Spring: IT02

        1905 Spring: IT07

        1906 Fall: FR01

        1907 Fall: FR01

        1907 Fall: IT04

        1909 Spring: IT04

        1910 Fall: IT09

        1910 Fall: IT10

    Game 4

        1902 Fall: TU01

        1903 Spring: GE01

        1904 Spring: UK06

        1904 Fall: UK01

        1904 Fall: FR03

    Game 5

        1901 Fall: AU01

        1902 Fall: FR05

        1903 Spring: FR01

        1904 Spring: RU03

        1904 Fall: TU01

        1904 Fall: TU02

    Game 6

        1903 Fall: UK04

        1903 Fall: UK05

        1903 Fall: UK06

        1903 Fall: GE05
    
        1904 Fall: FR04

        1908 Fall: GE10

    Game 7

        1903 Spring: IT04

        1903 Fall: IT04

        1906 Spring: GE03

        1907 Spring: IT05

        1913 Fall: AU03

    Game 8

        1903 Fall: IT01

        1905 Spring: IT02

        1905 Fall: IT03

        1905 Fall: IT04

        1906 Spring: TU06

        1906 Fall: TU04

        1907 Fall: FR10

        1908 Fall: TU01

        1909 Fall: FR12

        1910 Spring: UK04

        1910 Fall: TU07

        1914 Fall: TU08

        1915 Spring: FR05

        1916 Spring: UK04

"""




"""

Convoys

    Game 1

        1903 Spring:    RU04 (army convoyed)    => succeed
                        RU01 (fleet convoying)  => succeed
                        UK01 (fleet support)    => succeed
                        Note: destination is unoccupied, has higher strength than other attack on destination

        1904 Fall:      UK04 (army convoyed)    => succeed
                        FR03 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1905 Fall:      UK01 (army convoyed)    => fails; attack strength not greater than defend strength
                        UK05 (fleet convoying)  => succeed
                        UK06 (army support)     => fails; support is disrupted by attack on unit, supporting unit is displaced
                        Note: Destination is occupied, unit on destination supports an attack on the convoy's supporting unit
    
        1906 Fall:      FR08 (army convoying)   => succeed
                        FR05 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1907 Spring:    RU07 (army convoyed)    => succeed
                        UK02 (fleet convoying)  => succeed
                        RU04 (army support)     => succeed
                        RU01 (army support)     => succeed
                        Note: destination is occupied, destination unit successfully attacks another territory, no other attacks on destination

        1907 Fall:      TU05 (army convoyed)    => succeed
                        TU01 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination

    Game 2

        1901 Fall:      UK03 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1902 Spring:    UK03 (army convoyed)    => fails; attack strength not greater than defend strength
                        UK04 (fleet convoying)  => succeed
                        Note: destination is occupied, unit on destination has a failed attack 

        1902 Fall:      UK02 (army convoyed)    => fails; attack strength not greater than defend strength
                        UK03 (fleet convoying)  => succeed
                        Note: destination is occupied, unit on destination has a failed attack

        1902 Fall:      TU03 (army convoyed)    => fails; attack strength not greater than defend strength
                        TU02 (fleet convoying)  => succeed
                        Note: destination is unoccupied, attack bounces with another attack

        1903 Spring:    UK03 (army convoyed)    => fails; attack strength not greater than defend strength
                        UK05 (fleet convoying)  => succeed
                        UK02 (fleet support)    => fails; support is disrupted and unit is displaced
                        Note: destination is occupied and holding with no additional support strengths

        1903 Fall:      FR05 (army convoyed)    => fails; attack strength not greater
                        FR03 (fleet convoying)  => succeed
                        Note: destination is unoccupied, another attack on destination with higher strength wins

        1904 Fall:      UK04 (army convoyed)    => succeed
                        UK07 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1906 Fall:      UK03 (fleet convoying)  => succeed
                        UK01 (fleet convoying)  => succeed
                        UK05 (fleet support)    => succeed
                        Note: destination is unoccupied, no other attacks on destination

    Game 3

        1902 Spring:    UK03 (army convoyed)    => succeed
                        UK02 (fleet convoying)  => succeed
                        Note: destination is unoccupied

        Fall 1903:      UK01 (army convoyed)    => fails; attack strength not greater
                        UK04 (fleet convoying)  => succeed
                        Note: destination is unoccupied, attack bounces with another attack

        1904 Fall:      TU04 (army convoyed)    => fails; attack strength not greater
                        TU02 (fleet convoying)  => succeed
                        Note: destination is occupied by TU unit that has a failed attack

        1907 Spring:    RU07 (army convoyed)    => succeed
                        RU06 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1908 Fall:      IT02 (army convoyed)    => succeed
                        IT04 (fleet convoying)  => succeed
                        IT11 (fleet support)    => succeed
                        Note: destination is occupied, attack strength exceeds hold strength
        
        1910 Spring:    IT13 (army convoyed)    => succeed
                        IT09 (fleet convoying)  => succeed
                        IT05 (fleet support)    => succeed
                        Note: destination is unoccupied, no other attacks on destination 

    Game 4

        1901 Fall:      UK01 (army convoyed)    => succeed
                        UK03 (fleet convoying)  => succeed
                        UK02 (fleet support)    => succeed
                        Note: destination is unoccupied, there is another attack on destination, attack strength exceeds other attack strength

        1905 Spring:    UK04 (army convoyed)    => fails; invalid move path
                        UK02 (fleet convoying)  => succeed
                        UK05 (fleet convoying)  => succeed
                        UK03 (fleet support)    => succeed
                        Note: UK02 convoys army to a sea and not a coast; it is still a legal move

    Game 5

        1901 Fall:      RU02 (army convoyed)    => succeed
                        RU01 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1902 Spring:    RU04 (army convoyed)    => succeed
                        RU01 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1902 Fall:      UK03 (army convoyed)    => succeed
                        UK02 (fleet convoying)  => succeed
                        UK01 (fleet support)    => succeed
                        Note: destination is occupied, unit on destination successfully attacks another territory, no other attacks on destination 

    Game 6

        1903 Fall:      GE04 (army convoyed)    => succeed
                        GE01 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1907 Spring:    TU01 (army convoyed)    => succeed
                        TU05 (fleet convoying)  => succeed
                        TU07 (fleet support)    => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1907 Spring:    TU04 (army convoyed)    => succeed
                        TU02 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1908 Spring:    TU03 (army convoyed)    => succeed
                        TU04 (fleet convoying)  => succeed
                        TU05 (fleet convoying)  => succeed
                        TU12 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

    Game 7

        1901 Fall:      UK03 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1901 Fall:      IT01 (army convoyed)    => fails; attack strength not greater, another unit attacks destination
                        IT02 (fleet convoying)  => succeed
                        Note: destination is unoccupied, attack bounces with another attack

        1902 Fall:      IT01 (army convoyed)    => succeed
                        IT02 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1904 Spring:    IT01 (army convoyed)    => succeed
                        IT02 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 
        
        1911 Spring:    IT02 (army convoyed)    => succeed
                        IT03 (fleet convoying)  => succeed
                        IT05 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination
                    
        1913 Spring:    IT05 (army convoyed)    => succeed
                        IT03 (fleet convoying)  => succeed
                        Note: destination is unoccupied, no other attacks on destination 

        1913 Fall:      IT03 (army convoyed)    => fails; attack strength not greater than defend strength
                        IT02 (fleet convoying)  => succeed
                        IT08 (fleet convoying)  => succeed
                        Note: destination is occupied by IT unit with failed attack, another unit attacks destination with same strength

    Game 8

        1901 Fall:      UK02 (fleet convoying)  => succeed
                        UK03 (army convoyed)    => succeed
                        Note; destination is unoccupied, no other attacks on destination

        1903 Spring:    UK04 (fleet convoying)  => succeed
                        UK03 (army convoyed)    => succeed
                        UK02 (fleet support)    => succeed
                        Note: destination is occupied, destination unit does not attack, destination unit is displaced

        1905 Spring:    UK03 (fleet convoying)  => succeed
                        UK07 (army convoyed)    => fail; attack strength not greater than defend strength
                        Note: destination is occupied by FR01, FR01 does not attack and is not displaced
                        
        1905 Fall:      UK01 (fleet convoying)  => succeed
                        UK02 (fleet convoying)  => succeed
                        UK04 (army convoyed)    => fail; attack strength not greater than defend strength
                        UK06 (fleet support)    => fail, disrupted
                        Note: destination is occupied by IT01, IT01 does not attack and is not displaced

        1905 Fall:      UK03 (fleet convoying)  => fail
                        UK07 (army convoyed)    =>  invalid move path
                        Note: UK03 is dislodged by an attack with strength 2   
             
        1907 Spring:    UK01 (fleet convoying)  => succeed
                        FR05 (army convoyed)    => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1907 Spring:    UK03 (fleet convoying)  => succeed
                        FR04 (fleet convoying)  => succeed
                        UK07 (army convoyed)    => succeed    
                        Note: destination is unoccupied, no other attacks on destination

        1907 Fall:      UK01 (fleet convoying)  => succeed
                        FR03 (army convoyed)    => succeed
                        UK07 (fleet support)    => succeed
                        Note: destination is occupied and unit on destination has a failed attack, unit on destination disbands

        1908 Fall:      TU04 (fleet convoying)  => succeed
                        TU03 (army convoyed)    => fail; attack strength not greater than defend strength
                        Note: destination is occupied by TU10, TU10 has a failed attack 
                        
        1909 Spring:    UK02 (fleet convoying)  => succeed
                        UK03 (army convoyed)    => fails; invalid move path
                        Note: army has different move path than fleet

        1909 Spring:    TU04 (fleet convoying)  => succeed
                        TU03 (army convoyed)    => succeed
                        Note: destination is occupied, destination unit successfully attacks another territory         

        1909 Fall:      UK01 (fleet convoying)  => succeed
                        UK02 (army convoyed)    => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1910 Spring:    UK01 (fleet convoying)  => succeed
                        UK03 (army convoyed)    => succeed
                        Note: destination is unoccupied, no other attacks on destiantion 
        
        1910 Spring:    TU04 (fleet convoying)  => succeed
                        TU03 (army convoyed)    => succeed
                        Note: destination is occupied, destination unit successfully attacks another territory

        1911 Fall:      UK01 (fleet convoying)  => succeed
                        UK05 (army convoyed)    => succeed 
                        Note: destination is unoccupied, no other attacks on destination

        1911 Fall:      UK08 (fleet convoying)  => succeed
                        UK04 (army convoyed)    => succeed
                        Note: destination is unoccupied, no other attacks on destinaton

        1912 Spring:    UK01 (fleet convoying)  => succeed
                        UK10 (army convoyed)    => succeed
                        FR07 (army support)     => succeed
                        Note: destination is unoccupied, attack strength exceeds other attack strength

        1912 Spring:    TU03 (fleet convoying)  => succeeds
                        TU01 (army convoyed)    => fails; attack strength not greater than defend strength
                        Note: destination is occupied, TU unit on destination has failed attack

        1912 Fall:      TU03 (fleet convoying)  => succeed
                        TU02 (army convoyed)    => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1914 Spring:    UK05 (fleet convoying)  => succeed
                        UK02 (army convoyed)    => fails; attack strength not greater than defend strength
                        Note: destination is occupied and convoy has no support for attack 

        1914 Spring:    UK07 (fleet convoying)  => succeed
                        UK03 (army convoyed)    => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1914 Fall:      TU02 (fleet convoying)  => succeed
                        TU01 (army convoyed)    => succeed
                        Note: destination is unoccupied, no other attacks on destination

        1915 Spring:    UK01 (fleet convoying)  => succeed
                        UK02 (army convoyed)    => succeed
                        Note: destination is occupied by UK06, UK06 has a successful attack, no other attacks on destination 




"""