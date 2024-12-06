Title: Advent of Code: Day 6
Date: 2020-03-15
Tags: Python, Advent of Code, AoC 2017
Summary: My solutions to the sixth day's problems

## Part One

> There are sixteen memory banks; each memory bank can hold any number of blocks.
The goal of the reallocation routine is to balance the blocks between the memory banks.

> The reallocation routine operates in cycles.
In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks.
To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks.
It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

> The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen before.

> For example, imagine a scenario with only four memory banks:

> 1. The banks start with `0`, `2`, `7`, and `0` blocks. The third bank has the most blocks, so it is chosen for redistribution.

> 2. Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the 7 blocks are spread out over the memory banks.
The fourth, first, and second banks get two blocks each, and the third bank gets one back. The final result looks like this: `2 4 1 2`.

> 3. Next, the second bank is chosen because it contains the most blocks (four).
Because there are four memory banks, each gets one block. The result is: `3 1 2 3`.

> 4. Now, there is a tie between the first and fourth memory banks, both of which have three blocks.
The first bank wins the tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: `0 2 3 4`.

> 5. The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: `1 3 4 1`.

> 6. The third bank is chosen, and the same thing happens: `2 4 1 2`.

> At this point, we've reached a state we've seen before: `2 4 1 2` was already seen. The infinite loop is detected after the fifth block redistribution cycle, and so the answer in this example is 5.

> Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?

### Interpretation, Planning, and Discussion

Ok, this doesn't seem terribly insurmountable.
It sounds like we'll want to write a function to do the memory reallocation and then call it multiple times, keeping track of how many times we've called it.
We'll also have to keep track of everything we've seen so that we know when to stop.

### Solution

First, let's make the function to reallocate memory!
It will have to get the first maximum as well as its location.
If we look at the documentation for Python's [`max` function](https://docs.python.org/3/library/functions.html#max), it says that:

> If multiple items are maximal, the function returns the first one encountered.

This is great as we won't have to do anything special.

Similarly, looking at the [`.index` method for lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), it tells us that it will:

> Return zero-based index in the list of the first item whose value is equal to x.

We don't have to do anything special here either!

```python
def reallocate_mem(bank):
    # Get idx of first max
    amt = max(bank)
    idx = bank.index(amt)
```

Now, we set our bank's index to zero and allocate memory.
```python
    bank[idx] = 0

    # While we have memory, run through, allocating
    while amt > 0:
        idx += 1
        idx %= len(bank) # Wrap around

        bank[idx] += 1
        amt -= 1
```

The `%=` operator is similar to `+=`, but with the modulo operator (`%`) instead of addition.
When we take the `index MOD length`, it will make sure that `0 <= index < len(bank)` will always remain true.
That part does our wraparound logic.

Now, we need to call that function and stop when we've seen an allocation before.

```python
def reallocate_cycle_count(bank):
    seen_configs = set()
    count = 0

    while tuple(bank) not in seen_configs:
        seen_configs.add(tuple(bank))
        reallocate_mem(bank)
        count += 1

    return count
```

We need to check if `tuple(bank)` has been seen instead of just `bank` since lists in Python are not hashable and cannot be put in a set.
Tuples are not mutable and thus they can be hashed.
This can be accomplished in `O(N)` time where `N` is the length of our bank instead of `O(M)` time where `M` is the number of banks that we've seen.

Other than that, this function is fairly straight-forward!

#### Algorithmic Runtime

For allocation, I believe that part is `O(N)` where `N` is the length of the bank.
As stated above, checking if we've seen a configuration before is also `O(N)`.
I'm not actually sure what the worst-case upper bound is for how many times we need to reallocate memory before we see a duplicate.
It might be `O(NO)` where `O` is the maximum value in our memory bank?

In that case, our runtime would be `O(N^2 * O)` and our memory would be something similar since we are adding `O(N)` memory for each iteration.

## Part Two

> Now, we would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

> In the example above, `2 4 1 2` is seen again after four cycles, and so the answer in that example would be 4.

> How many cycles are in the infinite loop that arises from the configuration in your puzzle input?

### Interpretation, Planning, and Discussion

This is even more straightforward!
We take the output from the previous function and feed it back in to itself.
Even better, we can modify just one line in our function and get what we need.

### Solution 

I decided to use the [`namedtuple` class](https://docs.python.org/3/library/collections.html#collections.namedtuple) in order to keep track of our return values.
This is like a tuple, but we can access its members using attribute lookup as well as indexing.

```python
from collections import namedtuple

...

    return namedtuple('result', 'count final_val')(count, bank)
```

Now, our answer for Part One is `reallocate_cycle_count(our_input).count` and our answer for Part Two is `reallocate_cycle_count(reallocate_cycle_count(our_input).final_val).count`


#### Algorithmic Runtime

The algorithmic runtime and memory usage for Part Two should be similar to that of Part One.


----

My solutions for the Advent of Code problems are available on [GitHub](https://github.com/byarmis/AdventOfCode).

