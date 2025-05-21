from turtle import *

# Set background color to match Instagram's dark theme
bgcolor('#262626')

# Function to simulate gradient effect
def change_color(gradient_step):
    colors = ['#833AB4', '#E1306C', '#FCAF45']  # Purple to pink to orange
    pencolor(colors[gradient_step % len(colors)])

width(23)

penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
    change_color(i)  # Cycle through gradient colors
    forward(250)
    circle(34,90)

# Inner circle
penup()
goto(85,30)
pendown()
pencolor('#FCAF45')  # Orange tone from Instagram's gradient
circle(80,360)

# Small dot
penup()
goto(110,130)
pendown()
pencolor('#833AB4')  # Purple tone from Instagram's gradient
circle(7,360)

done()