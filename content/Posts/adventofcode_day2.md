Title: Advent of Code: Day 2
Date: 2018-02-11
Tags: Python, Advent of Code, AoC 2017
Summary: My solutions to the second day's problems

## Part One
> The spreadsheet consists of rows of apparently-random numbers.
> To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum.
> For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

> For example, given the following spreadsheet:

> `5 1 9 5`

> `7 5 3`

> `2 4 6 8`

> * The first row's largest and smallest values are 9 and 1, and their difference is 8.
> * The second row's largest and smallest values are 7 and 3, and their difference is 4.
> * The third row's difference is 6.

> In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

> What is the checksum for the spreadsheet in your puzzle input?

### Interpretation, Planning, and Discussion

So this one too is rather straightforward.
A file is read in line-by-line so works nicely that we are concerned with the minimum and maximum of a row.
We can go row by row, summing the min and max for each row.

We should be able to do this in $O(N)$ where N is the number of elements in our sheet.

### Solution

We have to do some preprocessing to change the read in strings to integers, but once we do that, we can get the solution with a simple one-liner:

```python
def checksum(sheet):
    return sum(max(row)-min(row) for row in sheet)
```

As predicted, this runs in $O(N)$ time-- both `min` and `max` run in linear time and if you do a bounded number of linear operations (like exactly two), the total time is also linear.

## Part Two

> The goal is now to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number.
> Find those numbers on each line, divide them, and add up each line's result.

> For example, given the following spreadsheet:

> `5 9 2 8`

> `9 4 7 3`

> `3 8 6 5`

> * In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
> * In the second row, the two numbers are 9 and 3; the result is 3.
> * In the third row, the result is 2.

> In this example, the sum of the results would be 4 + 3 + 2 = 9.

> What is the sum of each row's result in your puzzle input?

### Interpretation, Planning, and Discussion

Well then, this just got a bit more interesting!
Our data structure will definitely remain the same since we're still interested in the data broken up row by row.
For each row, however, we have to do something significantly different.

Python's [`itertools`](https://docs.python.org/3/library/itertools.html) module is one of my favorite and it is full of useful functions (that return iterators).
Because `itertools` returns generators, they are very memory efficient as long as they're not all stored (`list(<a generator>)` is no longer a generator).

The `combinations` function in `itertools` picks a configurable number of items from an iterable and returns all possible combinations of those.
For instance, `combinations('ABCD', 2)` --> `AB AC AD BC BD CD`.
Note that `BA` is considered the same as `BA` and therefore won't be returned as well.

Since we don't know anything about a row since it's not sorted, knowing the min / max won't help us, and filtering out even or odd values won't help us (3 divides 6 and 3 divides 9), we're probably going to have to test every combination (with `combinations`!).

This is going to be quite a bit more expensive than linear time-- the equation for the binomial coefficient (n choose k) is:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

Here, $n$ is the number of items in the row and $k$ is pegged to two.
As $n$ increases, the result increases by $n!$.
This is the best that I could come up with, unfortunately.

### Solution 

This new function takes a list of lists as its only argument.
We initialize our output variable (`O`) to zero and add to it as we go

```python
def checksum_2(sheet):
    O = 0
    for row in sheet:
```

We need to iterate through our possible `combinations` in each row.
We're given two values, `x` and `y`, and we should make sure that one is always predicably greater than the other.
We take the max and min of our values, giving us `X` and `Y`.

```python
        for x, y in itertools.combinations(row, 2):
            X = max(x,y)
            Y = min(x,y)
```

Finally, we need to see if the smaller value (`Y`) evenly divides the larger one (`X`).
If the floor diivsion of the numbers (`//`) is the same as the regular division (`/`), then we know `Y` evenly divides `X`.
We add that to our running sum and we can break out of our combination iteration since the problem tells us that here's only one number that evenly divides another.
This won't save us time in the algorithmic complexity sense (in the worst-case, we'll still have to go through every possible combination), but it will save us time in the average and best cases.

```python
            if X / Y == X // Y:
                O += X / Y
                break

    return O
```
After we go through all of the rows, we return our sum.  

Since we do factorial-time work, the complexity of Part Two is $O(N!)$ where $N$ is the number of items in the input spreadsheet.
Fortunately, our input is small enough to allow this to run in a reasonable amount of time (seconds).

----

My solutions for the Advent of Code problems are available on [GitHub](https://github.com/byarmis/AdventOfCode).
