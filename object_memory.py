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

        1914 Spring: TU09


Invalid Move Affected Outcomes

    Game 2

        1903 Fall: GE02

        1905 Spring: IT04

    Game 3

        1902 Spring: IT04

        1907 Fall: IT04

        1910 Fall: IT09

        1910 Fall: IT10

    Game 4

        1903 Spring: GE01

        1904 Fall: UK01

        1904 Fall: FR03

    Game 5

        1901 Fall: AU01

        1903 Spring: FR01

        1904 Spring: RU03

        1904 Fall: TU01

    Game 6

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

        Fall 1903: IT01

        1905 Fall: IT03

        1905 Fall: IT04

        1909 Fall: FR12

        1910 Spring: UK04

        1914 Fall: TU08

        1915 Spring: FR05

        1916 Spring: UK04

"""




"""

Convoys


    Game 8

        1901 Fall:      UK03 (army convoyed)    => succeed
                        UK02 (fleet convoying)  => succeed

        1903 Spring:    UK04 (army convoyed)    => succeed
                        UK03 (fleet convoying)  => succeed

        1905 Spring:    UK07 (army convoyed)    => fail; attack strength not greater than defend strength, destination is occupied by FR01
                        UK03 (fleet convoying)  => succeed

        1905 Fall:      UK04 (army convoyed)    => fail; attack strength not greater than defend strength, destination is occupied by IT01
                        UK01 (fleet convoying)  => succeed
                        UK02 (fleet convoying)  => succeed
                        UK06 (fleet support)    => fail, disrupted

        1905 Fall:      UK07 (army convoyed)    =>  invalid move path   
                        UK03 (fleet convoying)  => fail; unit is displaced
             
        1907 Spring:    FR05 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed

        1907 Spring:    UK07 (army convoyed)    => succeed
                        UK03 (fleet convoying)  => succeed    
                        FR04 (fleet convoying)  => succeed

        1907 Fall:      FR03 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed
                        UK07 (fleet support)    => succeed
                        Note: destination is occupied and unit on destination has a failed attack, unit on destination disbands

        1908 Fall:      TU03 (army convoyed)    => fail; attack strength not greater than defend strength, another TU unit occupies destination
                        TU04 (fleet convoying)  => succeed
                        
        1909 Spring:    UK03 (army convoyed)    => succeed
                        UK02 (fleet convoying)  => fail; invalid move path, different move path than fleet convoying

        1909 Spring:    TU03 (army convoyed)    => succeed
                        TU04 (fleet convoying)  => succeed

        1909 Fall:      UK02 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed

        1910 Spring:    UK03 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed
        
        1910 Spring:    TU03 (army convoyed)    => succeed
                        TU04 (fleet convoying)  => succeed

        1911 Fall:      UK05 (army convoyed)    => succeed 
                        UK01 (fleet convoying)  => succeed

        1911 Fall:      UK04 (army convoyed)    => succeed
                        UK08 (fleet convoying)  => succeed

        1912 Spring:    UK10 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed
                        FR07 (army support)     => succeed
                        Note: destination is unoccupied, another unit tries to attack destination

        1912 Spring:    TU01 (army convoyed)    => fails; attack strength not greater than defend strength, another TU unit occupied destination
                        TU03 (fleet convoying)  => succeeds

        1912 Fall:      TU02 (army convoyed)    => succeed
                        TU03 (fleet convoying)  => succeed

        1914 Spring:    UK02 (army convoyed)    => fails; attack strength not greater than defend strength, destination is occupied and convoy has no support
                        UK05 (fleet convoying)  => succeed

        1914 Spring:    UK03 (army convoyed)    => succeed
                        UK07 (fleet convoying)  => succeed

        1914 Fall:      TU01 (army convoyed)    => succeed
                        TU02 (fleet convoying)  => succeed

        1915 Spring:    UK02 (army convoyed)    => succeed
                        UK01 (fleet convoying)  => succeed




"""