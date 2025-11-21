#IC 1st turt starter

import turtle as turt

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turt.forward(length)
            draw_branch(length/3)
            turt.backward(length)
            turt.right(60)

fturt = turt.Turtle(),turt.shape("turtle"),turt.speed(0)
