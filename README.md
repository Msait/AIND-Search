##Prerequires:
Version of python: 2.7
##Commands:
To run Agents use:
**Depth First Search**
```bash
$ python pacman.py -l tinyMaze -p SearchAgent
$ python pacman.py -l mediumMaze -p SearchAgent
$ python pacman.py -l bigMaze -z .5 -p SearchAgent
```
**Breadth First Search**
```bash
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=bfs
```
**Uniform Search**
```bash
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs
```
**A-star**
```bash
$ python pacman.py -l tinyMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

Play pacman:
```bash
$ python pacman.py
```