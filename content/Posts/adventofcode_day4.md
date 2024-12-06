Title: Advent of Code: Day 4
Date: 2018-11-11
Tags: Python, Advent of Code, AoC 2017
Summary: My solutions to the the fourth day's problems.  Well, that's a bit easier

## Part One
> A passphrase consists of a series of words (lowercase letters) separated by spaces.
> To ensure security, a valid passphrase must contain no duplicate words.

> For example:

> * `aa bb cc dd ee` is valid.

> * `aa bb cc dd aa` is not valid - the word `aa` appears more than once.

> * `aa bb cc dd aaa` is valid - `aa` and `aaa` count as different words.

> The system's full passphrase list is available as your puzzle input.

> How many passphrases are valid?

### Interpretation, Planning, and Discussion

I'm sorry, what?!
This is significantly easier than Day 3, to the point where it wouldn't be beyond the realm of possiblity to solve this as a one-liner.

To solve this, we need to open and parse the file and then determine if something shows up more than once.
We can store each passphrase as a list and then compare its length to the length of a set made from that list-- if they're equal, every item in the list shows up once.
If the length of the set is shorter, there was at least one duplicate.

### Solution 

The code for this is short enough that I can post all of it before breaking it down and talking about it.

```python
i = 0
with open('input.txt') as f:
    for line in f.readlines():
        pw = line.strip().split(' ')
        if len(pw) == len(set(pw)):
            i += 1

print('Part One:{}'.format(i))
```
* `i` is just the counter of valid passphrases
* `with`, the context manager, takes care of opening and closing the file.
If there's any error raised by the code in the context manager, it handles closing the file before reraising the error so that files aren't left in a bad state of being opened when they aren't actively being used.
* The `for line in f.readlines()` just goes line by line, resulting in each line being the variable `line` that we can use later.
* For each line, we make it into a list, `pw`, that is the string split on white spaces.
`'a b c'` would become the list `['a', 'b', 'c']`.
* If the length of the list is the same as the a set of that list, each item in the list is unique, meaning that the passphrase is valid.

At the end, the resulting count is printed out. 

#### Algorithmic Runtime

If $P$ is the number of passphrases and $L$ is their length, this solution is $O(PL)$ since we operate on each passphrase once and do an $O(L)$ operation on it (turning the list into a set).
Getting the length of a list or a set is free. 

Memory usage is just $O(L)$ since the variable `pw` is overwritten for every different passphrase.

## Part Two
> Now, a valid passphrase must contain no two words that are anagrams of each other-- that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

> For example:

> * `abcde fghij` is a valid passphrase.

> * `abcde xyz ecdab` is not valid - the letters from the third word can be rearranged to form the first word.

> * `a ab abc abd abf abj` is a valid passphrase, because all letters need to be used when forming another word.

> * `iiii oiii ooii oooi oooo` is valid.

> * `oiii ioii iioi iiio` is not valid - any of these words can be rearranged to form any other word.

> Under this new system policy, how many passphrases are valid?

### Interpretation, Planning, and Discussion

Ok, this is nice and similar to the previous one, thankfully.

This will just require a simple modification to the logic in the first-- the anagram detection.
A nice way to tell if two words are anagrams of each other without rearranging the letters in $L!$ different ways is to sort the letters and then compare the two words.
If the letters are sorted to be the same, then they are an anagram.

For instance, `c b a` and `c a b` are both sorted to be `a b c`, meaning that they are anagrams.
We don't need to try all $3!$ permutations of the letters to determine that. 

### Solution 

The code for Part 2 is just about as long as Part 1 with some passphrase sorting going on.

```python
i = 0
with open('input.txt') as f:
    for line in f.readlines():
        pw = [''.join(sorted(list(w))) for w in line.strip().split(' ')]
        if len(pw) == len(set(pw)):
            i += 1

print('Part Two:{}'.format(i))
```

The only line different here is the fourth.
Here, we go word by word, turning it first into a list of letters, sorting it, and then reassembling it back into a word-- `''.join(sorted(list(w)))`.
Now, each passphrase is a list of sorted letters whose set can be compared to the list just as before.

#### Algorithmic Runtime

This one, understandably, is a bit slower than the first.
For $P$ passphrases each of length $L$, this will take $O(PL\log{L})$ since it takes $L\log{L}$ time to sort a list of length $L$ and we're doing it $P$ times.
Turning a list into a set takes $L$ time, but that's overshadowed by the $L\log{L}$ cost, so $L + L\log{L} = L\log{L}$.
That's just one of the weird parts about algorithmic runtime complexity analysis.

Memory usage is the same as the first part, $O(L)$.

----

My solutions for the Advent of Code problems are available on [GitLab](https://gitlab.com/byarmis/AdventOfCode) and [GitHub](https://github.com/byarmis/AdventOfCode).

