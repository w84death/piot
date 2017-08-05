# LvL0 - Telnet Multiplayer Shooter

# Prototype

![prototype of LvL0](http://i.imgur.com/s2JRCMz.png)

# Gameplay

- each player controls one tank
- tank have 3 Hit Points
- player controls tank by text commands
    - fi/fire *at* (empty == last target)
    - mv/move *to* (empty == forward)
    - at/to:
        - up
        - ri/right
        - do/down
        - le/left
    - sh/shield
    - sl/sleep *turns*
- shield hives prottection against bullets. It works form the time activated to the first interaction: hit/move/fire
- after 3 hits tank is eliminated and the player ands it's play with the hightscore
- highscore is calculated by formula: kills * 1000 + moves * 0.1 + fires * 0.2
- terrain
    - clear
    - wall
    - water
- tanks can run only on clear terrain
- walls can be destroyed by firing at them
- maps is always 80x24 characters
- tank represent one character
- player can give a list of commands (one after another)
- all tanks will run commands at the same time, each second
- no command for given second is interpreted as sleep


@ - tank
* - bullet path
~ - water (can not move)
. - clear (can move)
# - wall (can be destroyed)
+ - heals 1HP (up to 3)

Sample map:
```
................................~~~~...
######........@...................~~~~.
#....#....................#####.....~~~
#.+..#....................#.+.#......~~
###*##....................#...#.......~
...*......#.#.............#####.......~
...*.....##.######....................~
...*.....#....+..#....................~
...*.....#.......#....................~
...@.....#....+..#....................~
.........#########..........~~~......~~
.........................~~~~~~~~..~~~.
...................#.#.~~~.....~~~~~~..
...####.........~~~#.#~~ ..............
......#.......~~~..#.#.....#####.......
......#.....~~~............#...#.......
......#....~~..............#.+.#....,..
...####...~~~.........@....#####.......
.........~~............................
.........~~............................
```  
