Title: Advent of Code: Day 3 Part Two
Date: 2018-11-10
Tags: Python, Advent of Code, AoC 2017
Summary: My solutions to the second part of the third day's problems.  This could stand to be a little more related.

## Part Two

> The value 1 is stored in square 1.
> Then, in the same allocation order as above, the sum of the values in all adjacent squares is stored, including diagonals.

> So, the first few squares' values are chosen as follows:

> * Square 1 starts with the value 1.
> * Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
> * Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
> * Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
> * Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

> Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

$$
\begin{matrix}
147 & 142 & 133 & 122 & 59 \\
304 &   5 &   4 &   2 & 57 \\
330 &  10 &   1 &   1 & 54 \\
351 &  11 &  23 &  25 & 26 \\
362 & 747 & 806 & \rightarrow &   \dots
\end{matrix}
$$

> What is the first value written that is larger than your puzzle input?

### Interpretation, Planning, and Discussion

Wow, man, that's unfortunate.
Normally, the second part of the problems add on to what was made before.
Here, it seems like the only thing that's reused is, at best, the building out part of things, but even then, Part 2 is built out very differently compared to Part 1.

Our previous data structure is no longer really helpful at all.
Previously, we simplified the matrix by explicitly not caring about what was on either side of the cell, just which direction it should go.
Now, we _need_ to know what's to a cell's left / right, top / bottom, and its diagonals.
Forntunately, there's no walking back through that we need to worry about, just build until the value we insert is above a certain number.

We could possibly use a [Pandas](https://pandas.pydata.org/) DataFrame to represent a matrix, but there's a lot of overhead there that we don't need.
Regardless of performance, I want to solve all of the Advent of Code problems using just the Python standard library.
Also, I think what I came up with may be more performant!

In this case, a matrix can be represented by a dictionary where the keys are a tuple with the X and Y values of a point.
They have to be measured against something that doesn't move-- the origin in this case is the first cell.
One benefit of a dictionary is that keys can be added and accessed in constant time so we don't have to worry about the speed of lookups affecting the run time.

The grid is built out in a sprial and we'll have to keep track of the maximum value since that's our stopping point.

### Solution 

Let's start this solution with a class to represent a point.
This will make doing math later a bit easier since we'll be able to add a point to a point and get a point back.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return 'Point({x}, {y})'.format(x=self.x, y=self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
```

* Its initializer (`__init__`) just takes two arguments, an X and a Y value, the point's offset from the origin.
* The `__add__` method is called when you add two objects together.
In this case, you can only add a `Point` to another `Point` which makes sense.
* The `__repr__` method is just what the class looks like when you print it.
Instead of just seeing `Point` and its address in memory, we can see the values contained in the class.
* The `__eq__` and `__hash__` methods allow us to use the class as keys in a dictionary.
In Python 2, you can have a `__hash__` method without also defining an `__eq__` method, which is a really bad idea.
There can be hash collisions where two different objects have the same hash values but are not the same.  This is why  both `__hash__` and `__eq__` are required in Python 3 (and _strongly_ suggested in Python 2).

For this part of the problem, I decided to implement the solution as a class instead of a function, so let's define it and its initialization method now!

```python
from collections import defaultdict
from itertools import product

class part_2:
    def __init__(self):
        self.DIRECTIONS = tuple(Point(p[0], p[1]) for p in product([-1,0,1], repeat=2) if p != (0,0))
        self.points = defaultdict(int)
        self.points[Point(0,0)] = 1
        self.point_stack = [1]
```

* `DIRECTIONS` is a `tuple` representing the 8 directions around a cell, excluding the cell itself.
* `product` is an `itertools` function that returns all the different possible combinations of the first argument that it's passed `repeat` number of times.
In this case, it's $(-1, -1)$, $(-1, 0)$, $(-1, 1)$, $(0, -1)$, and so on.
There _are_ only 8 different directions, but this is easier to type, less likely to result in mistakes, and easier to increase the number if we become interested in more directions at some point.
* `points` is the dictionary that represents the grid that we're going to build out.
It's initialized with the origin and its starting value.
A `defaultdict` is effectively the same as a dictionary with one useful addition-- if you try to access a key that doesn't exist, instead of raising a `KeyError`, `defaultdict` returns a value.
Since we passed in `int` when we initialized it, it returns the default value, 0 (the same as just calling `int()`).
* The `point_stack` is used to keep track of the highest value since we're going to build out the spiral a bit more than we strictly need to in order to keep the code a bit more readable.

We'll also need a function to add up everone around a point:

```python
def neighbor_sum(self, p):
    return sum(self.points[p+d] for d in self.DIRECTIONS)
```

This function is fairly straightforward-- it takes a point, goes through all the directions we've calculated, and adds up everying.
The benefit of using a `defaultdict` is that we don't have to catch any errors and can just sum up everything as though they all exist, even though most of them might not.
The benefit of defining our own `Point` class earlier also is shown here since we can add a point to a point and use that as the key in our dictionary.
We don't have to worry about doing tuple math down here since the logic that already takes care of that is in the `Point` class, where it should be.

Now, it's time for the real meaty function, I'll call `run`.

```python
def run(self, goal):
    r = 1
    
    while self.point_stack[-1] <= goal:
        self.point_stack = []
        # Add right
        for y in range(-r+1, r+1):
            ns = self.neighbor_sum(Point(r, y))
            self.points[Point(r, y)] = ns
            self.point_stack.append(ns)
```

`run` is called with one argument, the goal that we want to build up to and past.
`r` is the effective radius of the spiral.
We're going to build it out one layer at a time and `r` will track that layer.

The stopping condition for the loop is that we've added a value that's greater than the input and `point_stack` is used to keep track of that maximum value.
Each time we go through the loop, we can clear out the stack since we don't care about previous layers, just the one that's most recently built.

The spiral is first built by going up the right side (starting at 3 o'clock, if the grid were a clock).
`r` is the X value for all the points going up the right side and the only thing that varies is their Y values, going from one row off the bottom of the grid up to the top right corner.  
For the first iteration, `r` is 1 so this will go from 0 upu to and including 1.

`ns` is the sum of a point's neighbors and that's calculated using the function we defined earlier.
That's added to our dictionary as well as pushed onto the stack.

Now we just need to repeat for the top, left, and bottom!

```python
        # Add top, right to left
        for x in range(r, -r-1, -1):
            ns = self.neighbor_sum(Point(x, r))
            self.points[Point(x, r)] = ns
            self.point_stack.append(ns)

        # Add left, top to bottom
        for y in range(r, -r-1, -1):
            ns = self.neighbor_sum(Point(-r, y))
            self.points[Point(-r, y)] = ns
            self.point_stack.append(ns)

        # Add bottom
        for x in range(-r, r+1):
            ns = self.neighbor_sum(Point(x, -r))
            self.points[Point(x, -r)] = ns
            self.point_stack.append(ns)

        r += 1
```
Since the `neighbor_sum` function doesn't care if a point already has a value (since `DIRECTIONS` purposefully _doesn't_ include $(0,0)$), we don't have to worry about double-counting the corners.
The order that we add a point definitely does matter though, so we have to build the top and left opposite from how we're building the right and bottom, hence the `-1` argument to the `range` function indicating that instead of adding 1 each time, it should subtract 1.

We've now finished adding a whole layer to the spiral, so it's time to increment `r` and start our loop again.
The `while` loop checks if it should continue at the start of each loop so the stack will be full with the layer that we just built.

Lastly, now that the spiral is built, we have to get what the problem is actually looking for

```python
    while self.point_stack[-1] > goal:
        # Pop from the stack until we go less than the value we're looking for
        ret_val = self.point_stack.pop()

    return ret_val
```
While our stack has too many values, we should remove them and save the thing we removed to `ret_val`.
This gets overwritten until the loop finds the crossover point, where the goal is between two values-- the larger one is returned.

#### Algorithmic Runtime

This one's also a bit tricky since it's hard to estimate how many cells the grid would have based off of the input value.
Going function-by-function though, we should be able to get a good estimate, or at least one that's good enough to compare this algorithm to others.

The `neighbor_sum` function is constant time since no matter the size of the input, it looks at 8 and only 8 different values.
Each one of those is a constant time lookup because we used a dictionary.

Despite the four `for` loops, each one only hits a cell once so building out the sprial is $O(N)$ where $N$ is the number of cells in the spiral.
The various stack manipulations during the construction phase are also $O(N)$ since each cell is pushed onto the stack once.

Popping from the stack at the end is, worst-case, $O(\sqrt{N})$ since there are, at most, $\sqrt{N}$ items on the stack at the end.
There are $N$ items in the spiral, but the stack only has the last layer from the spiral.
If the length of a spiral's side is $S$, then there are $S^2$ cells in the matrix and $4S$ items in the stack (four sides in a layer).
Since $N$ is the number of cells in the matrix, $N = S^2$ so $O(\sqrt{N})$ items in the stack (the constant factor $4$ drops away).

Similarly, the memory used is $O(N)$ since each cell is stored in the matrix once.
There is some memory used by the stack, but again, its dwarfed by the matrix.

----

This isn't my first solution to this problem.

I originally started with a list of lists representing the matrix, but the code for that was terrible with large chunks copy-pasted and slightly modified to go along each side and special cases had to be made for corner pieces as well as pieces touching corner pieces.
The runtime complexity of it was also terrible since lists were prepended to multiple times, an $O(N)$ operation in and of itself since the whole list has to be shifted around to add an item to the beginning of it.

----

My solutions for the Advent of Code problems are available on [GitLab](https://gitlab.com/byarmis/AdventOfCode) and [GitHub](https://github.com/byarmis/AdventOfCode).
