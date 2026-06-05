Web VPython 3.2

running = False
a=0

l1 = 5
theta = 0

scene = canvas(title='Swinging Atwood Machine (SAM)', align='left', width=600, height=400)
scene.append_to_caption("\t")
startButton = button(bind=start, text="    Start      ", background=vec(0.7, 0.9, 0.95))
#scene.append_to_caption("\t")
pauseButton = button(bind=start, text="       Pause        ", background=vec(0.7, 0.9, 0.95))
#scene.append_to_caption("\t")
resetButton = button(bind=reset, text="       Reset        ", background=vec(0.7, 0.9, 0.95))
speedButton = button(bind=start, text="      Speed Up       ", background=vec(0.7, 0.9, 0.95))
enableButton = button(bind=start, text="     Enable Trail     ", background=vec(0.7, 0.9, 0.95))
scene.append_to_caption("\n\n")
scene.append_to_caption("\t")
enableButton = button(bind=start, text="     Preset 1       ", background=vec(0.7, 0.9, 0.95))
enableButton = button(bind=start, text="     Preset 2      ", background=vec(0.7, 0.9, 0.95))
enableButton = button(bind=start, text="     Preset 3      ", background=vec(0.7, 0.9, 0.95))
scene.append_to_caption("\n\n")

#swinging mass slider
scene.append_to_caption("\t<b>Mass of Swinging Ball</b>\n")
scene.append_to_caption("\n\t")
mass1 = sphere(pos=vector(-5, -5, 0), color=color.blue, radius=1, make_trail=False)
mass1label = label(pos=mass1.pos, text="1 kg", box=False)
wtext(text="1.0 kg  ")
mass1slider = slider(min=1.0, max=10.0, value=1, length=300, bind=updatemass1)
wtext(text="  10.0 kg")

def updatemass1(slider):
    new_mass = slider.value
    mass1label.text = f"{new_mass:.1f} kg"
    mass1.radius = pow(new_mass, 1/3)
    
scene.append_to_caption("\n\n")
    
#not swinging mass slider
scene.append_to_caption("\t<b>Mass of Ball</b>\n")
scene.append_to_caption("\n\t")
mass2 = sphere(pos=vector(7, -5, 0), color=color.red, radius=1, make_trail=False)
mass2label = label(pos=mass2.pos, text="1 kg", box=False)
wtext(text="1.0 kg  ")
mass2slider = slider(min=1.0, max=10.0, value=1, length=300, bind=updatemass2)
wtext(text="  10.0 kg")

def updatemass2(slider):
    new_mass = slider.value
    mass2label.text = f"{new_mass:.1f} kg"
    mass2.radius = pow(new_mass, 1/3)
    
scene.append_to_caption("\n\n")

#pivots
pivot1 = sphere(pos=vector(-5, 5,0), radius=0.3, color=color.white)
pivot2 = sphere(pos=vector(7, 5, 0), radius=0.3, color=color.white)
curve(pos=[pivot2.pos, pivot1.pos], color=vec(0.7, 0.9, 0.95))

#length of swinging part of string
scene.append_to_caption("\t<b>Length of Swinging part of string</b>\n")
scene.append_to_caption("\n\t")
string1 = curve(pos=[mass1.pos, pivot1.pos], color=vec(0.7, 0.9, 0.95))
wtext(text="1.0 cm  ")
string1slider = slider(min=1.0, max=10.0, value=1, length=300, bind=updatestring1)
wtext(text="  10.0 cm")



def updatestring1(slider):
    new_length = slider.value
    global l1
    l1 = new_length
    #find new position of string based on starting angle
    top = pivot1.pos
    bottom = vector(-5-l1 * sin(theta), 5-l1 * cos(theta),0)
    string1.clear()
    string1.append(pos=top)
    string1.append(pos=bottom)
    mass1.pos = bottom
    mass1label.pos = mass1.pos

scene.append_to_caption("\n\n")

#length of not swinging part of string
scene.append_to_caption("\t<b>Length of not Swinging part of string</b>\n")
scene.append_to_caption("\n\t")
string2 = curve(pos=[mass2.pos, pivot2.pos], color=vec(0.7, 0.9, 0.95))
wtext(text="1.0 cm  ")
string2slider = slider(min=1.0, max=10.0, value=1, length=300, bind=updatestring2)
wtext(text="  10.0 cm")

def updatestring2(slider):
    new_length = slider.value
    #find new position of string based on starting angle
    top = pivot2.pos
    bottom = vector(7, 5 - new_length, 0)
    string2.clear()
    string2.append(pos=top)
    string2.append(pos=bottom)
    mass2.pos = bottom
    mass2label.pos = mass2.pos
    
scene.append_to_caption("\n\n")

#starting angle
scene.append_to_caption("\t<b>Starting Angle</b>\n")
scene.append_to_caption("\n\t")
wtext(text="0°  ")
angleslider = slider(min=0, max= pi/2, value=0, length=300, bind=updateangle)
wtext(text="  90°")

def updateangle(slider):
    new_angle = slider.value
    global theta
    theta = new_angle
    mass1.pos=vector(-5-l1 * sin(new_angle), 5-l1 * cos(new_angle),0)
    global string1
    string1.clear()
    string1 = curve(pos=[mass1.pos, pivot1.pos], color=vec(0.7, 0.9, 0.95))
    mass1label.pos = mass1.pos
    
scene.append_to_caption("\n\n")
    
#mass of pivots
scene.append_to_caption("\t<b>Mass of pivots</b>\n")
scene.append_to_caption("\n\t")
pmass1label = label(pos=pivot1.pos, text="0 kg", yoffset=15, box=False)
pmass2label = label(pos=pivot2.pos, text="0 kg", yoffset=15, box=False)
wtext(text="0 kg  ")
pmassslider = slider(min=0, max=10.0, value=0, length=300, bind=updatepmass)
wtext(text="  10.0 kg")

def updatepmass(slider):
    new_mass = slider.value
    pmass1label.text = f"{new_mass:.1f} kg"
    pmass2label.text = f"{new_mass:.1f} kg"

scene.append_to_caption("\n\n")


#radius of pivots
scene.append_to_caption("\t<b>Radius of pivots</b>\n")
scene.append_to_caption("\n\t")
pradius1label = label(pos=pivot1.pos, text="0 cm", xoffset=30, yoffset=15, box=False)
pradius2label = label(pos=pivot2.pos, text="0 cm", xoffset=30, yoffset=15, box=False)
wtext(text="0 cm  ")
pradiusslider = slider(min=0, max=10.0, value=0, length=300, bind=updatepradius)
wtext(text="  10.0 cm")

def updatepradius(slider):
    new_radius = slider.value
    pradius1label.text = f"{new_radius:.1f} cm "
    pradius2label.text = f"{new_radius:.1f} cm "







def start(button):
    global running
    running = True
    
def pause(button):
    global running
    running = False
    
def reset(button): 
    extrema.clear()

# ------------ When the start button is clicked  -------------

    if running:
        butt.background = color.green
        
# ------------- When the stop button is clicked
 
    else:
        butt.text = "Click to start"
        
        global N
        if N < 2: 
            print("Insufficient running time.")
        butt.background = color.red
        ball.vel = initVel
        ip.disabled = False

while running:
    rate(20)
    mass1label.pos = mass1.pos
    mass2label.pos = mass2.pos
