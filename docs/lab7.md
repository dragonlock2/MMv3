# Lab 7: Maze Solving Primitives (WIP)

The simplest implementation is to just have `forward`, `turn_left`, `turn_right`, and `turn_around` functions. Turning should be pretty easy, but implementing `forward` is trickier as it needs to wall follow, account for lack of walls to reference, and correct for distance errors. Here's some considerations.

- There are 8 possible cases on wall presence for `forward` bc there are 4 walls in consideration when moving forward one cell.
- If we suddenly see an opening on the left or right (or sudden appearance of a wall) we can correct our internal distance measurement.
- We want to maintain 0° with respect to wall on left and right which means an error for each side. If we see openings on the left and right, the errors will point in opposite directions and we should drive straight using just encoders.
- If we start without a wall on one side, we should wall follow using just the other side. May be a concern if that side suddenly lacks a wall so perhaps just drive straight using encoders.
- Should take the minimum of the efforts to correct for both wall angle errors to account for suddenly seeing an opening on one side.
