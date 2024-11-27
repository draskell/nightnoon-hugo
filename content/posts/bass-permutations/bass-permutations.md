---
title: "Bass Permutations Exercise"
date: 2023-01-06T20:10:37-08:00
draft: false
tags:
- music
categories:
- music
---

This left hand four finger exercise will lead you through every four finger pattern (permutation). The idea is to assign a each finger to a fret (ie the index finger on the 7th fret) and go through each of the 24 possible permutations. Start slowly then build up the speed, but keep it rhythmic, see how fast you can go. The trick to going faster is mastering slower speeds first.

I like this exercise as a warm up because it gets all of the fingers involved. I do this on the bass, but it works on any stringed instrument.

## The Idea

Practicing musical shapes (like the major scale in a single position) is a great idea, but it trains your brain to execute specific sequences between fingers. If you do a chromatic exercise like this you can strengthen the neural pathways other than those found in the standard scales.

It's not exactly a musical exercise, but it can be fun to try to think of melodies you know which use each permutation in the melody as you play through them.

## The Basic Exercise

Pick a fret which doesn't require too much pinky strength to start off with, I like the 7th fret. That fret gets assigned to your index finger. Each finger will be assigned to a fret, so if the index is on the 7th, the middle is on the 8th, ring on 9th, and pinky on 10th.

I'm going to use a number to represent each finger for simplicity: index is 1, middle is 2, ring is 3, and pinky is 4. This can also be thought of as the fret number where the 7th fret is "1", 8th is "2", etc. It doesn't matter where on the neck you play.

![Numbered Fingers](/numbered_fingers.png)

The permutations are as follows:

```
1:  1-2-3-4, index-middle-ring-pinky (natural ascending order)
2:  1-2-4-3, index-middle-PINKKY-RING (switch the last two)
3:  1-3-2-4, index-RING-middle-pinky
4:  1-3-4-2, etc
5:  1-4-2-3
6:  1-4-3-2
7:  2-1-3-4
8:  2-1-4-3
9:  2-3-1-4
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

The right hand isn't the focus of the exercise, just alternate fingers, or pick up-down-up-down if you're into the pick thing.

In order to not read the permutations as you go it helps to think about it systematically. Start with the lowest number that you haven't played all the options then move to the next finger and do the same. From the beginning start on the first finger (1), then play the next one you haven't played (2) etc. When you get to the second permutation you have already played the third finger (1-2-3-4), so play the 4th (1-2-4-3), reversing the final two. 

Next you play the 1-3 starting starting pair because you've already covered both 1-2 starts. The final two positions will start in ascending order, so 1-3-2-4. 

## Multi-string Options

In order to reduce the cognitive load of figuring out the next permutation while playing it I found a useful option was to play the same permutation on each of the 4 strings. So start with 1-2-3-4 on the E string, then A string, then D string, and finally G string before going back to the E string for 1-2-4-3 etc.

Alteratively, a harder option once you have familiarity with the permutations is to move up a string with each permutation. First permutation (1-2-3-4) on the E string, next (1-2-4-3) on the A string etc.

## Add Some Rhythm

Play with a metronome. Play one measure of quarter notes, one measure of eighths, one measure of quarter note triplets, and one measure of sixteenth notes. Then do the same backward:

1/4 notes -> 8th notes -> 1/4 triplets -> 16th notes -> 16th -> 1/4 triplet -> 8th -> 1/4 -> repeat from the beginning.

The trick here is to do this over the permutations. One permutation per measure, so first measure is a quarter note on fret 1, quarter on 2, quarter on 3, and a quarter on 4. Second measure is two 8ths on fret 1, two 8ths on fret 2, two 8ths on fret 4, and two 8ths on fret 3. 

Play slow (40 BPM) and record yourself to see how accurate you can be. Listen back to the recording to hear an honest (an in my case humbling) reproduction of your timing. Alternatively, play fast and see if you can make it through without any obvious mistakes.

Mastering this exercise with rhythm at a pace like 120 BPM could take a really long time, but it's a great way to check in and warm your fingers up. I've been doing it for years and I rarely get it perfect.

## Bonus: Python Script for Permutations

This is a simple Python script to find the permutations. 

``` Python
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

It could be interesting to add more positions on the neck. Sky's the limit!