Title: Advent of Code: Introduction and Day 1
Date: 2018-02-05
Tags: Python, Advent of Code, AoC 2017
Summary: Intros and my solutions to the first day's problems


## Introduction

### What

This series of blog posts are my attempt at solving all of the [Advent of Code](http://adventofcode.com/) posts, starting at 2017 and then working on the previous years.
The Advent of Code consists of puzzles and problems, one each day for the month of December.
Yes, I know it's February.

After the problems are posted at midnight each day, the first hundred people who solve get points; starting at 100 points for the first person who solves it and decreasing down to 1 point for the hundredth person who solves it.
The way that a solution is arrived at is not specified-- it can be in any programming language or not any programming language at all.
I've been told that some people just print out their input and work through it by hand with a pencil and other people [decide to go an even more difficult direction](https://www.reddit.com/r/adventofcode/comments/7jicl9/2017_day_13_part_1factorio_anyone_here_play/).

Each day has two parts-- the first being simpler and / or easier than the second.  The second part may ask you something about the first part ("how many times did you \_\_\_ ?") or modify it slightly or not so slightly ("instead of calculating \_\_\_ like \_\_\_, instead, calculate it like \_\_\_").
Solving the first part results in one star and the second part results in an addtional one.
Solving both parts isn't required and solving the days in order isn't required either-- I decided to do both, however.

### How

The ideal solution for a given problem is an interesting mix of run-time as well as implementation time.
The algorithmically fastest solution that takes too long to write will lose to the slower solution that can be written then run in fewer lines of code.
This can lead to interesting solutions that might consist of illegible code that can be written quickly or maybe even no code at all.
Minutes of thinking about the problem to come up with an answer in your head may beat the best algorithm any day-- after all, you only get points if you're one of the first hundred people to solve a given problem.

I started working on the problems back in December, but by no means kept up with the pace of the problems (as evidenced by me publishing this blog post in February).
I also didn't start on the first problem on December 1, but more like the 14th.
I _did_ start on the problems in December, in my defense!

I decided to take a different approach to the problems-- instead of the quickest to code or the best algorithm, I went for what I thought was the "best".
Possibly the fastest, but hopefully the cleanest or most-readable.
If nothing else, aiming to be cleaner and more readable than the fastest and faster than the cleanest!

All of my solutions for the Advent of Code problems are available on [GitLab](https://gitlab.com/byarmis/AdventOfCode) and [GitHub](https://github.com/byarmis/AdventOfCode).
Feel free to take a look!

----

## Day 1

### Part One

> The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list.
> The list is circular, so the digit after the last digit is the first digit in the list.

> For example:

> * `1122` produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
> * `1111` produces 4 because each digit (all 1) matches the next.
> * `1234` produces 0 because no digit matches the next.
> * `91212129` produces 9 because the only digit that matches the next one is the last digit, 9.

> What is the solution to your captcha?

#### Interpretation, Planning, and Discussion

Ok, so this problem consists of a series of digits, 0 through 9.
It looks like we're going to want to iterate through the input once and only once-- thinking of algrotihmic complexity, we can probably do this in $O(N)$ (where $N$ is the length of the input string).
At least, if we can't, we'll have to think about it a bit and justify it to ourselves.

There's a slight twist here in that the list is circular; the last digit will have to be compared to the first.
As far as data structures for this goes, we're going to need something that stores values in order (so we can't use a set) and if we can access the first or last value in constant time, that'd be better.
Fortunately, we can just use an array (or a string) and iterate over it.

#### Solution

Let's make a function that takes in a number (or a string) and returns our calculated captcha.
This day's problem is simple enough that we just need the one function and not a whole lot else.
We're going to return `out` and we need to initialize it to `0`-- simple enough.
This function can accept either an integer (to make testing easier) or a string (which is what reading a file would return) so we need to cast what we get to a string.
If we're passed a string, `str(i)` won't do anything.

```python
def inverse_captcha_p1(i):
    out = 0
    i = str(i)
```
Python's `zip` function takes iterables and returns the first of all of the iterables, the second of all of the iterables, and so on until we're all the way through the shortest one ([the itertools module has an `izip_longest`](https://docs.python.org/3/library/itertools.html#itertools.zip_longest) function that keeps going to the longest, instead of the shortest).
We're going to pass it our string twice with the second one being our whole string but skipping the first value.
This way, we look at the first value and the second, then the second value and the thrid, and so on.

If they're the same, we need to add the value of either of them to our output counter.
We're iterating over a string, so `first` is a string-- the `int` function casts that string to an integer, allowing us to do math with it (`1 + 1` equals `2`, but `'1' + '1'` is `'11'`).

```python
    for first, second in zip(i, i[1:]):
        if first == second:
            out += int(first)
```

Lastly, the input is circular so now we need to compare the last to the first before returning our sum.

```python
    if i[-1] == i[0]:
        out += int(i[0])
    return out

```

Good news!
We iterated over our list once-ish.
One of the weird things about algorithmic complexity calculations is that pesky things like numbers kinda merge together so now one is effectively the same thing as two.

### Part Two

> Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. that is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
> Fortunately, your list has an even number of elements.

> For example:

> * `1212` produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
> * `1221` produces 0, because every comparison is between a 1 and a 2.
> * `123425` produces 4, because both 2s match each other, but no other digit has a match.
> * `123123` produces 12.
> * `12131415` produces 4.

> What is the solution to your new captcha?

#### Interpretation, Planning, and Discussion

Ok, so this is pretty similar to the first part.
Instead of comparing one with the next, we have to be halway around (so instead of `i` and `i + 1`, we compare `i` and `i + len(N) / 2`) for just half of the array and then we can double our result at the end.
If a number in the first half has a twin, we'll run into it on the second half of the array so we can double the initial value and not even worry about the second half.

#### Solution

Our initialization is pretty much the same as before, except we also want to make sure that there's an even number of elements.
The problem does specify that the length of the input is even, but adding the check doesn't hurt. 

```python
def inverse_captcha_p2(i):
    out = 0
    i = str(i)
    assert len(i) % 2 == 0, 'Length of input must be even'
```

The looping is similar again, but this time, instead of the second argument in our `zip` being the list offset by one, it's now the second half of the list.
Because `len(i)` is even, `len(i) / 2 == len(i) // 2` so they _should_ be equivalent.
_But_ in Python 3, division will always result in a float (`2.0`) instead of an integer (`2`).
List slicing requires integer indexes so we use the floor divide (`//`) instead.

```python
    for first, second in zip(i, i[len(i) // 2 : ]):
        if first == second:
            out += int(first)
```

Finally, we return double what we calculated.

```python
    return out * 2
```

Part two, like the first part, runs in $O(N)$ (linear) time.

----

My solutions for the Advent of Code problems are available on [GitHub](https://github.com/byarmis/AdventOfCode).

