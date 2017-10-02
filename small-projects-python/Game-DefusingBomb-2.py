#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2/27/17

@author: davecohen

Title: GAME - DEFUSING THE BOMB

[2016-11-21] Challenge #293 [Easy] Defusing the bomb

Description
To disarm the bomb you have to cut some wires. These wires are either white, black, purple, red, green or orange.
The rules for disarming are simple:
full list: white, black, red, green, orange, purple
If you cut a white cable you can't cut white or black cable.
    you can cut: red, green, orange, purple
If you cut a red cable you have to cut a green one
If you cut a black cable you can't cut a white, green or orange one
    you can cut: red, black, purple
If you cut a orange cable  you can't cut orange, white, green, purple.
    you should cut a red or black one
If you cut a green one you have to cut a orange or white one
    you can't cut green, red, black, purple
If you cut a purple cable you can't cut a purple, green, orange or white cable
    you can cut: black, red

There can be multiple wires with the same colour and these instructions are for one wire at a time. Once you cut a wire you can forget about the previous ones.

Formal Inputs & Outputs
Input description

You will recieve a sequence of wires that where cut in that order and you have to determine if the person was succesfull in disarming the bomb or that it blew up.
Input 1
white
red
green
white

Input 2
white
orange
green
white

Output description
Wheter or not the bomb exploded
Output 1
"Bomb defused"
Output 2
"Boom"

Notes/Hints
A state machine will help this make easy
"""
#changes to make: user input? strings: 'wr' etc instead of tuples.
wire_in1 = ['w', 'r', 'g', 'w']
wire_in2 = ['w', 'o', 'g', 'w']
goodlist = ['wr','wg','wo','wp','rg','br','bb','bp','or','ob','go','gw','pb','pr']
inp0 = wire_in2 #<-change the input here! (on the right side of the = sign)
inp_pairs = []
#create pairs from input
for n,wire in enumerate(inp0):
    if n == len(inp0)-1 : continue
    else:
        #print((wire,inp0[n+1])) #debug
        pair = wire+inp0[n+1]
        inp_pairs.append(pair)
print('inp_pairs:',inp_pairs)
print('...checking if bomb will explode...')
for pair in inp_pairs:
    if pair in goodlist: status = True
    else: 
        status = False
        break
if status == True:
    print('Bomb defused - you saved the day!!')
else:
    print('BOOM! EVERYONE IS DEAD!')
'''OUTPUT for wire_in1 = ['w', 'r', 'g', 'w']:
<DEBUG> inp_pairs: [('w', 'r'), ('r', 'g'), ('g', 'w')]
Bomb defused - you saved the day!

OUTPUT for wire_in2 = ['w', 'o', 'g', 'w']:
<DEBUG> inp_pairs: [('w', 'o'), ('o', 'g'), ('g', 'w')]
BOOM! EVERYONE IS DEAD!
'''