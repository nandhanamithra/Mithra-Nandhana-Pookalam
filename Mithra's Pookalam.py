# 🌸 Hello! I’m Mithra, and this is my final submission for Code a Pookalam 2025 🌸
# 🌺 Requirements: Python + turtle + math (no extra libraries needed)
# 🌷 Note: tracer() used for faster drawing (disable it with '#' to see animations)
# 🌼 Sit back, relax, run the code, and watch a digital Pookalam bloom 🪷

import turtle, math    

#functions
def small_circles_around(pen, big_radius, small_radius=10, count=36, color="black", offset_deg=0):
    halfstep = math.radians(offset_deg)
    for i in range(count):
        angle = 2 * math.pi * i / count + halfstep
        x = big_radius * math.cos(angle)
        y = big_radius * math.sin(angle)
        pen.penup()
        pen.goto(x, y - small_radius)
        pen.setheading(0)
        pen.pendown()
        pen.color(color)
        pen.fillcolor(color)
        pen.begin_fill()
        pen.circle(small_radius)
        pen.end_fill()

def petal(pen, size=200, color="black"):    
    pen.color(color)
    pen.fillcolor(color)    
    pen.begin_fill()    
    for i in range(2):    
        pen.circle(size, 100)    
        pen.left(90)    
    pen.end_fill()    

def teardrop_shape(p, size=30, color="black"):    
    p.color(color)
    p.fillcolor(color)    
    p.begin_fill()    
    p.right(90)    
    p.circle(size, 180)    
    p.circle(size * 2, 180)    
    p.left(180)    
    p.circle(-size, 180)    
    p.left(90)    
    p.end_fill()    

def teardrops_inside_circle(p, x, y, big_radius, count=10, size=20, color="black"):    
    for i in range(count):    
        ang = 360 / count * i    
        p.penup()    
        p.goto(x, y)    
        p.setheading(ang)    
        p.forward(big_radius - size)    
        p.pendown()    
        teardrop_shape(p, size=size, color=color)    
    p.penup(); p.goto(0,0); p.setheading(0)    

def triangles_around_circle(pen, radius=150, count=12, size=80, color="black"):
    angle_step = 360 / count
    for i in range(count):
        angle = angle_step * i
        pen.penup()
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        pen.goto(x, y)
        pen.setheading(angle)
        pen.pendown()
        pen.color(color)
        pen.fillcolor(color)
        pen.begin_fill()
        pen.right(90)
        for i in range(3):
            pen.forward(size)
            pen.left(120)
        pen.end_fill()

def draw_flower(x, y, petal_color="white", center_color="yellow"):
    pen.up()
    pen.goto(x, y)
    pen.setheading(0)
    pen.down()

    for i in range(8):  
        pen.color(petal_color)
        pen.fillcolor(petal_color)
        pen.begin_fill()
        pen.circle(15, 60)
        pen.left(120)
        pen.circle(15, 60)
        pen.left(120)
        pen.end_fill()
        pen.left(45)

    pen.up()
    pen.goto(x, y-5)
    pen.setheading(0)
    pen.down()
    pen.color(center_color)
    pen.fillcolor(center_color)
    pen.begin_fill()
    pen.circle(6)
    pen.end_fill()

#🐢
pen = turtle.Turtle()    
pen.speed(0)    
pen.hideturtle()
turtle.colormode(255)    
turtle.tracer(0,0) #comment '#' to enable animations
turtle.bgcolor((85, 107, 47))    

#brown base
#dark
pen.penup(); pen.goto(0, -345); pen.pendown()    
pen.color((60, 40, 20)); pen.fillcolor((60, 40, 20))    
pen.begin_fill(); pen.circle(345); pen.end_fill()
#light
pen.penup(); pen.goto(0, -340); pen.pendown()    
pen.color((101, 67, 33)); pen.fillcolor((101, 67, 33))    
pen.begin_fill(); pen.circle(340); pen.end_fill()

#purple flowers (5)
small_circles_around(pen, 215, small_radius=120, count=5, color=(48,25,52)) 

#colored 
colors = [(220, 20, 60), (255, 255, 255), (255, 140, 0), (128, 0, 128), (255, 215, 0)]    
smcolors=[(178, 34, 34),(245, 245, 245),(204, 85, 0),(75, 0, 130),(204, 173, 0)]
lighter_smcolors= [(255, 182, 193),(255, 250, 240),(255, 200, 150),(221, 160, 221),(255, 239, 170)]

petal_colors1 = [(255, 200, 150), (218, 170, 255),(244, 196, 48),(255, 182, 193),(255, 255, 240)]
centre_colors1 = [(160, 82, 45),(255, 215, 0),(160, 82, 45),(255, 215, 0),(160, 82, 45)]

petal_colors2 = [(255, 140, 80),(186, 85, 211),(255, 223, 100),(153, 102, 204),(250, 240, 230)]
centre_colors2 = [(101, 67, 33),(255, 191, 0),(101, 67, 33),(255, 191, 0),(101, 67, 33)]

num_circles = 5
radius = 210
circle_size = 110

for i in range(num_circles):
    angle = 2 * math.pi * i / num_circles
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    pen.penup()
    pen.goto(x, y - circle_size)
    pen.setheading(0)
    pen.pendown()
    pen.color(colors[i % len(colors)])
    pen.fillcolor(colors[i % len(colors)])
    pen.begin_fill()
    pen.circle(circle_size)
    pen.end_fill()
    
    #flower ring
    inner_ring_radius = circle_size * 0.4
    petals_count = 12
    angle_step = 2 * math.pi / petals_count

    for j in range(petals_count):
        theta = j * angle_step
        fx = x + inner_ring_radius * math.cos(theta)
        fy = y + inner_ring_radius * math.sin(theta)
        draw_flower(fx, fy, petal_color=petal_colors1[i % len(petal_colors1)], center_color=centre_colors1[i % len(centre_colors1)])
    inner_ring_radius = circle_size * 0.85 
    petals_count = 12
    angle_step = 2 * math.pi / petals_count

    for j in range(petals_count):
        theta = j * angle_step
        fx = x + inner_ring_radius * math.cos(theta)
        fy = y + inner_ring_radius * math.sin(theta)
        draw_flower(fx, fy, petal_color=petal_colors2[i % len(petal_colors2)], center_color=centre_colors2[i % len(centre_colors2)])    
    
    #small circles
    r = 65
    count = 20
    small_radius = 6
    for j in range(count):
        theta = 2 * math.pi * j / count
        sx = x + r * math.cos(theta)
        sy = y + r * math.sin(theta)

        pen.penup()
        pen.goto(sx, sy - small_radius)
        pen.setheading(0)
        pen.pendown()
        pen.color(lighter_smcolors[i % len(lighter_smcolors)])
        pen.fillcolor(lighter_smcolors[i % len(lighter_smcolors)])
        pen.begin_fill()
        pen.circle(small_radius)
        pen.end_fill()
        
        #big circles
        ring_radius = circle_size
        small_radius = 6
        small_count = 20
        for j in range(small_count):
            theta = 2 * math.pi * j / small_count
            sx = x + ring_radius * math.cos(theta)
            sy = y + ring_radius * math.sin(theta)

            pen.penup()
            pen.goto(sx, sy - small_radius)
            pen.setheading(0)
            pen.pendown()
            pen.color(smcolors[i % len(smcolors)])
            pen.fillcolor(smcolors[i % len(smcolors)])
            pen.begin_fill()
            pen.circle(small_radius)
            pen.end_fill()
            
#triangles(leaf)
triangles_around_circle(pen, radius=200, count=20, size=60, color=(90, 140, 28)) 
triangles_around_circle(pen, radius=195, count=20, size=55, color=(25, 85, 15))

#magenta flowers and flowers  
count = 5
magenta_radius = 180
circle_size =90

for i in range(count):
    angle = 2 * math.pi * i / count + math.radians(36)
    x = magenta_radius * math.cos(angle)
    y = magenta_radius* math.sin(angle)

    pen.penup()
    pen.goto(x, y - circle_size)
    pen.setheading(0)
    pen.pendown()
    pen.color((73,36,51))
    pen.fillcolor((73,36,51))
    pen.begin_fill()
    pen.circle(circle_size)
    pen.end_fill()

count = 5
magenta_radius= 175
circle_size = 85

for i in range(count):
    angle = 2 * math.pi * i / count + math.radians(36)
    x = magenta_radius * math.cos(angle)
    y = magenta_radius* math.sin(angle)

    pen.penup()
    pen.goto(x, y - circle_size)
    pen.setheading(0)
    pen.pendown()
    pen.color((110, 0, 50))
    pen.fillcolor((226,28,112))
    pen.begin_fill()
    pen.circle(circle_size)
    pen.end_fill()
   
    inner_ring_radius = 60
    petals_count = 10
    angle_step = 360 / petals_count

    for j in range(petals_count):
        theta = math.radians(j * angle_step)
        fx = x + inner_ring_radius * math.cos(theta)
        fy = y + inner_ring_radius * math.sin(theta)
        draw_flower(fx, fy, petal_color="white", center_color="yellow")
 
    inner_ring_radius = 5
    petals_count = 1
    angle_step = 360 / petals_count

    for j in range(petals_count):
        theta = math.radians(j * angle_step)
        fx = x + inner_ring_radius * math.cos(theta)
        fy = y + inner_ring_radius * math.sin(theta)
        draw_flower(fx, fy, petal_color="white", center_color="yellow")

#pink flowers + pea flowers
small_circles_around(pen, 140, small_radius=75, count=5, color=(199, 21, 133)) 
small_circles_around(pen, 140, small_radius=70, count=5, color=(219, 112, 147))

count = 5    
for i in range(count):    
    angle = 2 * math.pi * i / count    
    x = 140 * math.cos(angle)    
    y = 140 * math.sin(angle)    
    teardrops_inside_circle(pen, x, y, big_radius=60, count=12, size=10, color=(0, 61, 128))   
    teardrops_inside_circle(pen, x, y, big_radius=60, count=12, size=9, color=(153, 204, 255))  
    teardrops_inside_circle(pen, x, y, big_radius=60, count=12, size=8, color=(0, 102, 204))  
    teardrops_inside_circle(pen, x, y, big_radius=60, count=12, size=6, color=(0, 76, 153))
    teardrops_inside_circle(pen, x, y, big_radius=60, count=12, size=4, color=(0, 46, 102)) 
    teardrops_inside_circle(pen, x, y, big_radius=55, count=12, size=4, color=(120, 120, 200))       
     
    #flower ring inside this circle
    inner_ring_radius = circle_size * 0.4
    petals_count =9
    angle_step = 2 * math.pi / petals_count

    for j in range(petals_count):
        theta = j * angle_step
        fx = x + inner_ring_radius * math.cos(theta)
        fy = y + inner_ring_radius * math.sin(theta)
        draw_flower(fx, fy, petal_color='yellow', center_color='white') 

# red flowers    
pen.penup(); pen.goto(0,-140 ); pen.pendown()    
pen.color((153, 0, 51)); pen.fillcolor((153, 0, 51))    
pen.begin_fill(); pen.circle(140); pen.end_fill()
pen.penup(); pen.goto(0,-135 ); pen.pendown()    
pen.color((153, 0, 51)); pen.fillcolor((178, 0, 34))    
pen.begin_fill(); pen.circle(135); pen.end_fill()

# yellow flower 
small_circles_around(pen, 110, small_radius=50, count=5, color=(230, 190, 40)) 


#flower ring inside the circle
circle_radius = 110  
small_radius = 45
count = 5            
for i in range(count):
    angle = 2 * math.pi * i / count
    cx = circle_radius * math.cos(angle)
    cy = circle_radius * math.sin(angle)

    
    pen.penup()
    pen.goto(cx, cy - small_radius)
    pen.pendown()
    pen.color((255, 223, 85))
    pen.fillcolor((255, 223, 85))
    pen.begin_fill()
    pen.circle(small_radius)
    pen.end_fill()

    pen.color((255, 20, 147))
    draw_flower(cx, cy, petal_color="pink", center_color="white")


#colourful petals  
colorslight=[(255, 178, 102),(255, 220, 100),(255, 102, 128),(255, 153, 204),(221, 160, 221),(186, 85, 211)]
colorsdark=[(204, 85, 0),(204, 128, 0),(139, 0, 0),(199, 21, 133),(148, 0, 211),(75, 0, 130)]
colors = [(255, 140, 0),(255, 180, 0),(220, 20, 60),(255, 0, 127),(186, 85, 211),(128, 0, 128)]
num_petals = 24    
angle = 360 / num_petals    

for i in range(num_petals):    
    pen.penup(); pen.goto(0, 0)    
    pen.setheading(angle * i)    
    pen.forward(80)    
    pen.pendown()   
    pen.color(colorsdark[i % len(colorsdark)])
    petal(pen, size=45, color=colors[i % len(colors)])    
    petal(pen, size=40, color=colorslight[i % len(colorslight)])  
        

#white flowers
small_circles_around(pen, 100, small_radius=20, count=13, color=(245, 245, 220))    
small_circles_around(pen, 95, small_radius=20, count=13, color=(255, 248, 240))   
small_circles_around(pen, 90, small_radius=20, count=13, color=(255, 255, 255))   
 
#flowers 
circle_radius = 90   
small_radius = 20     
count = 13         

for i in range(count):
    angle = 2 * math.pi * i / count
    cx = circle_radius * math.cos(angle)
    cy = circle_radius * math.sin(angle)

    
    pen.penup()
    pen.goto(cx, cy - small_radius)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(small_radius)
    pen.end_fill()

    pen.color((255, 20, 147))
    draw_flower(cx, cy, petal_color="pink", center_color="white")


#circles   
#  yellow flowers
pen.penup(); pen.goto(0, -80); pen.pendown()
pen.color((153, 122, 0)); pen.fillcolor((255, 215, 0))
pen.begin_fill(); pen.circle(80); pen.end_fill()
small_circles_around(pen, 80, small_radius=12, count=18, color=(204, 173, 0))
small_circles_around(pen, 80, small_radius=10, count=18, color=(255, 215, 0))
small_circles_around(pen, 80, small_radius=8, count=18, color=(255, 239, 150))

#hues of red
pen.penup(); pen.goto(0, -70); pen.pendown()
pen.color((153, 51, 0)); pen.fillcolor((255, 69, 0))
pen.begin_fill(); pen.circle(70); pen.end_fill()
small_circles_around(pen, 70, small_radius=10, count=16, color=(204, 85, 0))
small_circles_around(pen, 70, small_radius=8, count=16, color=(255, 69, 0))
small_circles_around(pen, 70, small_radius=6, count=16, color=(255, 178, 102))


pen.penup(); pen.goto(0, -60); pen.pendown()
pen.color((128, 0, 0)); pen.fillcolor((255, 69, 0))
pen.begin_fill(); pen.circle(60); pen.end_fill()
small_circles_around(pen, 60, small_radius=8, count=17, color=(178, 34, 34))
small_circles_around(pen, 60, small_radius=6, count=17, color=(255, 69, 0))
small_circles_around(pen, 60, small_radius=4, count=17, color=(255, 120, 90))


pen.penup(); pen.goto(0, -50); pen.pendown()
pen.color((128, 0, 64)); pen.fillcolor((255, 0, 127))
pen.begin_fill(); pen.circle(50); pen.end_fill()
small_circles_around(pen, 50, small_radius=7, count=18, color=(199, 21, 133))
small_circles_around(pen, 50, small_radius=7.5, count=18, color=(255, 0, 127))
small_circles_around(pen, 50, small_radius=6, count=18, color=(255, 153, 204))


pen.penup(); pen.goto(0, -40); pen.pendown()
pen.color((220, 20, 60)); pen.fillcolor((220, 20, 60))
pen.begin_fill(); pen.circle(40); pen.end_fill()
small_circles_around(pen, 40, small_radius=7, count=17, color=(139, 0, 0))
small_circles_around(pen, 40, small_radius=6, count=17, color=(220, 20, 60))
small_circles_around(pen, 40, small_radius=5, count=17, color=(255, 102, 128))


pen.penup(); pen.goto(0, -30); pen.pendown()
pen.color((128, 0, 64)); pen.fillcolor((255, 0, 127))
pen.begin_fill(); pen.circle(30); pen.end_fill()
small_circles_around(pen, 30, small_radius=6, count=15, color=(199, 21, 133))
small_circles_around(pen, 30, small_radius=5, count=15, color=(255, 0, 127))
small_circles_around(pen, 30, small_radius=4, count=15, color=(255, 153, 204))
 
#tulsi
pen.penup(); pen.goto(0, -20); pen.pendown()
pen.color((51, 0, 77)); pen.fillcolor((128, 0, 128))
pen.begin_fill(); pen.circle(20); pen.end_fill()
small_circles_around(pen, 20, small_radius=5, count=10, color=(75, 0, 130))
small_circles_around(pen, 20, small_radius=4, count=10, color=(128, 0, 128))
small_circles_around(pen, 20, small_radius=3, count=10, color=(186, 85, 211))

r = 12    
while r > 0:    
    pen.color((51, 0, 77))
    small_circles_around(pen, r, small_radius=4, count=5, color=(75, 0, 130))    
    r -= 4    

#thumba
pen.penup(); pen.goto(0, -8); pen.pendown()    
pen.color((192, 192, 192)); pen.fillcolor((253, 245, 230))    
pen.begin_fill(); pen.circle(8); pen.end_fill()    

r = 4   
while r > 0:   
    small_circles_around(pen, r, small_radius=2, count=3, color=(255, 250, 250))    
    r -= 4


turtle.update()
turtle.done()
