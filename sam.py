Web VPython 3.2

from vpython import *
running = False
a=0
scene = canvas(title='Swinging Atwood Machine (SAM)', align='left', width=600, height=400)
scene.append_to_caption("\t")
startButton = button(bind=bouncing, text="    Start      ", background=vec(0.7, 0.9, 0.95))
#scene.append_to_caption("\t")
pauseButton = button(bind=bouncing, text="       Pause        ", background=vec(0.7, 0.9, 0.95))
#scene.append_to_caption("\t")
resetButton = button(bind=bouncing, text="       Reset        ", background=vec(0.7, 0.9, 0.95))
speedButton = button(bind=bouncing, text="      Speed Up       ", background=vec(0.7, 0.9, 0.95))
enableButton = button(bind=bouncing, text="     Enable Trail     ", background=vec(0.7, 0.9, 0.95))
scene.append_to_caption("\n\n")
scene.append_to_caption("\t")
enableButton = button(bind=bouncing, text="     Preset 1       ", background=vec(0.7, 0.9, 0.95))
enableButton = button(bind=bouncing, text="     Preset 2      ", background=vec(0.7, 0.9, 0.95))
enableButton = button(bind=bouncing, text="     Preset 3      ", background=vec(0.7, 0.9, 0.95))
scene.append_to_caption("\n\n")

#swinging mass slider
scene.append_to_caption("\t<b>Mass of Swinging Ball</b>\n")
scene.append_to_caption("\n\t")
mass1 = sphere(pos=vector(-10, -5, 0), color=color.blue, radius=1, make_trail=False)
mass1label = label(pos=mass1.pos, text="1 kg", box=False)
wtext(text="1.0 kg  ")
mass1slider = slider(min=1.0, max=10.0, value=1, length=300, bind=updatemass1)
wtext(text="  10.0 kg")

def updatemass1(slider):
    new_mass = slider.value
    mass1label.text = f"{new_mass:.1f} kg"
    
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
    
scene.append_to_caption("\n\n")

#pivots
pivot1 = sphere(pos=vector(-5, 5,0), radius=0.1, color=color.white)
pivot2 = sphere(pos=vector(7, 5, 0), radius=0.1, color=color.white)
curve(pos=[pivot2.pos, pivot1.pos], color=color.yellow)

#length of swinging part of string
scene.append_to_caption("\t<b>Length of Swinging part of string</b>\n")
scene.append_to_caption("\n\t")
string1 = curve(pos=[mass1.pos, pivot1.pos], color=color.yellow)
wtext(text="1.0 cm  ")
string1slider = slider(min=1.0, max=10.0, value=1, length=300, bind=updatestring1)
wtext(text="  10.0 cm")

def updatestring1(slider):
    new_length = slider.value
    #find new position of string based on starting angle
    top = pivot1.pos
    bottom = vector(-5, 5 - new_length, 0)
    string1.clear()
    string1.append(pos=top)
    string1.append(pos=bottom)
    mass1.pos = bottom

scene.append_to_caption("\n\n")

#length of not swinging part of string
scene.append_to_caption("\t<b>Length of not Swinging part of string</b>\n")
scene.append_to_caption("\n\t")
string2 = curve(pos=[mass2.pos, pivot2.pos], color=color.yellow)
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






def bouncing(butt):
    global running
    
    running = not running

# ------------ When the start button is clicked  -------------

    if running:
        butt.text = "Click to stop and reset"
        print("Calculating period ...")
        N=0
        extrema.clear()
        old_vel = initVel
        butt.background = color.green
        ip.disabled = True
        
# ------------- When the stop button is clicked
 
    else:
        butt.text = "Click to start"
        
        global N
        if N < 2: 
            print("Insufficient running time.")
        butt.background = color.red
        ball.vel = initVel
        ip.disabled = False

while True:
    rate(20)
    mass1label.pos = mass1.pos
    mass2label.pos = mass2.pos
