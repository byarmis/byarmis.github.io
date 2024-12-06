Title: Advent of Code: Day 5
Date: 2018-11-19
Tags: Python, Advent of Code, AoC 2017
Summary: My solutions to the the fifth day's problems.  Fun with lambdas

## Part One
> You are given message consisting of the offsets for jumps.
Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one.
Start at the first instruction in the list.
The goal is to follow the jumps until one leads outside the list.

> After each jump, the offset of that instruction increases by 1.
So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

> For example, consider the following list of jump offsets:

> $$ \left[
         \begin{array}{c}
             0 \\
             3 \\
             0 \\
             1 \\
             -3
         \end{array} 
     \right]
  $$

> Positive jumps ("forward") move downward; negative jumps move upward.
The following steps would be taken before an exit is found:

> 1. `(0) 3  0  1  -3`  - before we have taken any steps.
> 2. `(1) 3  0  1  -3`  - jump with offset `0` (that is, don't jump at all).
The instruction is then incremented to `1`.
> 3. `2 (3) 0  1  -3`  - step forward because of the instruction we just modified.
The first instruction is incremented again, now to `2`.
> 4. `2  4  0  1 (-3)` - jump all the way to the end; leave a `4` behind.
> 5. `2 (4) 0  1  -2`  - go back to where we just were; increment `-3` to `-2`.
> 6. `2  5  0  1  -2`  - jump `4` steps forward, escaping the maze.

> In this example, the exit is reached in 5 steps.

> How many steps does it take to reach the exit?

### Interpretation, Planning, and Discussion

Algorithmically, this solution is fairly straightforward-- we just implement the rules of the problem.

We can take advantage of some different parts of Python to keep this clean and looking nice.
There were some slight modifications made to the solution to the first part after the second was revealed, but they were fairly minor.

### Solution 

The code for this solution is also small enough to show all of it and discuss it line-by-line:

```python
def jumps_to_exit(j, f):
    i = 0
    c = 0

    while 0 <= i < len(j):
        to_jump = j[i]
        j[i] += f(j[i])

        i += to_jump
        c += 1

    return c
```

* `jumps_to_exit` will be our function that takes in an input list and a function (I'll talk more about that later)
* `i` is initialized to be our index in the list and `c` is the jumps taken to exit the list
* `while 0 <= i < len(j)`: while our pointer hasn't gone over either end of the list, we keep running the algorithm in the body of the loop.
* `to_jump` is the offset that we're going to add to our current one
* `j[i] += f(j[i])`: this is where there's some fun!
We use the function that's the second argument to the function to calculate our jump value.
For part one, this is just a function that returns the value `1`.
We don't need to take up a whole lot of space with this function and can use Python's `lambda`, or anonymous, functions to define them in-line.
In this case, for part one, it's simply `part_one = lambda x: 1`.
It can be called like a normal function with one argument, but this one always returns `1`.
* `i += to_jump`: here, we add the amount that we should jump to our current index's value
* Lastly, we increment our jump counter by 1 (`c += 1`) and return it if we've broken out of the loop off either end of the list.

Something to note: we're modifying the list in-place.
If we want to call this function multiple times with the same input list, we have to make sure we're passing it a copy and not the original one.

#### Algorithmic Runtime

Because of the rule that adds one to the value before we jump, this _isn't_ $O(\infty)$ worst-case since we are guaranteed to run over _an_ end eventually.

I _think_ that the runtime of this is $O(Nm)$ where $N$ is the number of elements in the list and $m$ is the minimum absolute value in the list.
If we have a long list but the first value is equal to or greater than the list's length, then we just have to do one operation and we're done.
Similarly, if we have a really long list and small values, we'll be making many jumps.

We don't use any additional data structures, so this uses $O(1)$ additional memory.

## Part Two
> Now, after each jump, if the offset was three or more, instead decrease it by 1.
Otherwise, increase it by 1 as before.

> Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as `2 3 2 3 -1`.

> How many steps does it now take to reach the exit?

### Interpretation, Planning, and Discussion

Awesome!
Since our previous function took in a function as the second argument to calculate the amount we should jump, we just need to change the function that we're passing in.

### Solution 

This modification is even shorter!

```python
part_two = lambda x: -1 if x >= 3 else 1
```

Seriously, that's it.
We call the function the same as before, but instead of calling `jumps_to_exit(list_in[:], part_one)`, we call it with `part_two`.

The `list_in[:]` syntax makes a copy of the list.
I normally see list slicing used like `list_in[1:]` to skip the first element or `list_in[:-1]` to skip the last.
It's a slightly odd use of the slicing syntax, effectively saying "give me `list_in` starting at the beginning and ending at the end."

#### Algorithmic Runtime

This one's the same as before since the amount we increment by isn't a factor in the runtime.

----

My solutions for the Advent of Code problems are available on [GitLab](https://gitlab.com/byarmis/AdventOfCode) and [GitHub](https://github.com/byarmis/AdventOfCode).

