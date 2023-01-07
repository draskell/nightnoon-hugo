---
title: "Bass Permutations Exercise"
date: 2023-01-06T20:10:37-08:00
draft: false
tags:
- music
categories:
- music
---

This is a left hand four finger exercise to train all of the left hand inter-finger permutations. The idea is to assign a finger to each fret and go through each of the 24 possible permutations. Start slowly then build up the speed, but keep it rhythmic, see how fast you can go. The trick to going faster is mastering slower speeds though.

It's a pretty great warm up because it gets all of the fingers involved.

## Background

I found practicing musical shapes (like the major scale in a single position) trains your brain to execute specific sequences between fingers. If you do a chromatic exercise like this you can strengthen the neural pathways other than those found in the scales.

It's not the most musical exercise, but it can be fun to try to think of melodies that use each permutation as you play through them.

## The Basic Exercise

Pick a fret which doesn't require too much pinky strength to start off with, I like the 7th fret. That's the fret for your index finger. Each finger will be assigned to a fret, so the index is on the 7th, the middle is on the 8th, ring on 9th, and pinky on 10th.

Assign a number to each finger: index is 1, middle is 2, ring is 3, and pinky is 4. The permutations are as follows:

```
1: 1-2-3-4
2: 1-2-4-3
3: 1-3-2-4
4: 1-3-4-2
5: 1-4-2-3
6: 1-4-3-2
7: 2-1-3-4
8: 2-1-4-3
9: 2-3-1-4
10: 2-3-4-1
11: 2-4-1-3
12: 2-4-3-1
13: 3-1-2-4
14: 3-1-4-2
15: 3-2-1-4
16: 3-2-4-1
17: 3-4-1-2
18: 3-4-2-1
19: 4-1-2-3
20: 4-1-3-2
21: 4-2-1-3
22: 4-2-3-1
23: 4-3-1-2
24: 4-3-2-1
```

So the first permutation is simply playing one finger on each fret counting up from 7th with the index, 8th with the middle, 9th with the ring, and 10th with the pinky.

The right hand isn't the focus of the exercise, just alternate fingers, or pick up-down if you're into that kind of thing.

In order to not read the permutations as you go it helps to think about it systematically. First, start on the first finger (1), then play the next one you haven't played (2) etc. When you get to the second permutation you reverse the final two. Next you play the 1-3 starting with the other two notes in ascending order. Then the 1-3 start with the other notes in descending order. Now the 1-4 start with the other notes 2-3 in ascending order, then 1-4 start with the other notes descending 3-2. 

Now you've played all of the options starting with 1, start with 2 then the lowest unplayed, so 2-1 with the other two in ascending 3-4 etc etc.

## Multi-string Option

Move up a string with each permutation. First permutation (1-2-3-4) on the E string, next (1-2-4-3) on the A string etc.

## Bonus: Python Script for Permutations

This is a simple Python script to find the permutations. 

```
#!/usr/bin/env python3
# make_permutations.py

from itertools import permutations

if __name__ == "__main__":
    for p in list(permutations([1,2,3,4])):
        print(p)
```

Puts out the permutations:

```
$ python make_permutations.py
(1, 2, 3, 4)
(1, 2, 4, 3)
(1, 3, 2, 4)
(1, 3, 4, 2)
(1, 4, 2, 3)
(1, 4, 3, 2)
(2, 1, 3, 4)
(2, 1, 4, 3)
(2, 3, 1, 4)
(2, 3, 4, 1)
(2, 4, 1, 3)
(2, 4, 3, 1)
(3, 1, 2, 4)
(3, 1, 4, 2)
(3, 2, 1, 4)
(3, 2, 4, 1)
(3, 4, 1, 2)
(3, 4, 2, 1)
(4, 1, 2, 3)
(4, 1, 3, 2)
(4, 2, 1, 3)
(4, 2, 3, 1)
(4, 3, 1, 2)
(4, 3, 2, 1)
```

It could be interesting to add more fingers which would require a position change on the neck. Sky's the limit!