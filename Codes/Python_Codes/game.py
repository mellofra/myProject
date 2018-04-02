#!/usr/bin/python

from turtle import *
import sys

title("Draw what you want! By: Nicolas Mello Franca")

res = sys.argv[1]

if(res == "quadrado"):
	color("Red")
	pensize("5")
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(100)

	done()

if(res == "triangulo"):
	color("Green")
	pensize("5")
	forward(100)
	left(120)
	forward(100)
	left(120)
	forward(100)

	done()

if(res == "circulo"):
	color("Grey")
	pensize(5)
	circle(50)

	done()
