# [2015-2-23] Challenge #203 [Easy] The Start of Something Big
# http://redd.it/2ww3pl

# Description

# All great things start with something small. Sometimes people don't even realise what goes into making a 'small' thing[1] .
# A popular story is linked above about a group of graphics programmers who create a rendering engine in some amount of time. After some time HR came to see what the programmers had accomplished. They responded by showing a black triangle on a tv.
# HR was less than impressed (understandle for a non techie) but it goes to show the natural evolution of a program. What they didn't realise is that the programmers have created their base engine and can now easily add and extend on top of it.
# Maybe you can follow similar steps?

# Challenge

# On your screen, display a square.
# You may use any libraries available to you.
# The square may be of any size and of any colour.

import turtle

turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(4):
    turtle.forward(300)
    turtle.left(90)
turtle.end_fill()
turtle.mainloop()
