# MMSim

A simulator of the flood fill algorithm for a MicroMouse. It starts by showing the "optimal" Dijkstra's algorithm solution. Then it runs flood fill multiple times between the source and target in the search for the shortest path. There's a bunch of different mazes in the mazes/ folder stored as .txt files. To run one try this:

```
python3 simrh.py mazes/00japan.txt
```

simrh.py simulates a mouse which has sensors on its front, left, and right. simang.py is more like the mouse we use in the DeCal, which has angled sensors and one on the front. To simulate that mouse, use:

```
python3 simang.py mazes/00japan.txt
```