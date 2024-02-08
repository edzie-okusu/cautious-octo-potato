from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class Block(Turtle):
    """ Doc string for Block in the breakout game. The block has attribute of all_blocks, which is a list containing all the blocks created. It has an initial y cordinate of 200 and x cordinate of 360"""
    def __init__(self):
        super().__init__()
        self.all_blocks = []
        self.x = -360
        self.y = 200

    def create_block(self):
        """ The create_block() function creates a new block for the breakout game. It uses the 'square' turtle, has a shapesize of 1(for the stretch_wid and  the stretch_len) """
        new_block = Turtle('square')
        new_block.shapesize(stretch_wid=1, stretch_len=1)
        new_block.penup()
        new_block.color(random.choice(COLORS))
        new_block.goto(self.x, self.y)
        self.x += 40
        if self.x > 340:
            self.x = -360
            self.y -= 40
        self.all_blocks.append(new_block)
