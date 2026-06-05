Web VPython 3.2

running = False
speed_multiplier = 1
trail = False
g = 9.81
m1 = 1.0 #swinging mass
m2 = 1.0  #non swining mass
mpivot = 0.0   
rpivot = 0.0   
l1 = 5.0       
l2 = 5.0       
L = 10.0 #total rope length
rd = 0.0       
theta = 0.0    
omega = 0.0
dt = 0.001

def start(button):
    global running
    running = True

def pause(button):
    global running
    running = False

def reset(button): 
    global running, l1, L, theta, rd, omega
    running = False
    l1 = string1slider.value
    L = l1 + string2slider.value
    theta = angleslider.value
    rd = 0.0
    omega = 0.0
    
    if trail:
        mass1.clear_trail()
    update_visuals()

def speed_up(button):
    global speed_multiplier
    if speed_multiplier == 1:
        speed_multiplier = 10
        button.text = "   Normal Speed   "
    else:
        speed_multiplier = 1
        button.text = "     Speed Up     "

def toggle_trail(button):
    global trail
    trail = not trail
    mass1.make_trail = trail
    if trail:
        button.text = "   Disable Trail  "
    else:
        button.text = "   Enable Trail   "
        mass1.clear_trail()

def preset1(button):
    mass1slider.value = 1.0
    updatemass1(mass1slider)
    mass2slider.value = 1.555
    updatemass2(mass2slider)
    string1slider.value = 4.0
    updatestring1(string1slider)
    string2slider.value = 2.0
    updatestring2(string2slider)
    angleslider.value = pi/2
    updateangle(angleslider)
    reset(None)

def preset2(button):
    mass1slider.value = 1
    updatemass1(mass1slider)
    mass2slider.value = 6
    updatemass2(mass2slider)
    string1slider.value = 2.0
    updatestring1(string1slider)
    string2slider.value = 4.0
    updatestring2(string2slider)
    angleslider.value = pi/2
    updateangle(angleslider)
    reset(None)

def preset3(button):
    mass1slider.value = 1.0
    updatemass1(mass1slider)
    mass2slider.value = 1.665
    updatemass2(mass2slider)
    string1slider.value = 5.0
    updatestring1(string1slider)
    string2slider.value = 5.0
    updatestring2(string2slider)
    angleslider.value = pi/2
    updateangle(angleslider)
    reset(None)

def updatemass1(slider):
    global m1
    m1 = slider.value
    mass1label.text = f"{m1:.4f} kg"
    mass1.radius = pow(m1, 1/3)

def updatemass2(slider):
    global m2
    m2 = slider.value
    mass2label.text = f"{m2:.4f} kg"
    mass2.radius = pow(m2, 1/3)

def updatestring1(slider):
    global l1, L
    if not running:
        l1 = slider.value
        L = l1 + string2slider.value
        update_visuals()

def updatestring2(slider):
    global L
    if not running:
        L = string1slider.value + slider.value
        update_visuals()

def updateangle(slider):
    global theta
    if not running:
        theta = slider.value
        update_visuals()

def updatepmass(slider):
    global mpivot
    mpivot = slider.value
    pmass1label.text = f"{mpivot:.3f} kg"
    pmass2label.text = f"{mpivot:.3f} kg"

def updatepradius(slider):
    global rpivot
    rpivot = slider.value
    pradius1label.text = f"{rpivot:.3f} cm "
    pradius2label.text = f"{rpivot:.3f} cm "
    pivot1.radius = max(0.3, rpivot / 10.0)
    pivot2.radius = max(0.3, rpivot / 10.0)

scene = canvas(title='Swinging Atwood Machine (SAM)', align='left', width=600, height=400)
scene.append_to_caption("\t")
startButton = button(bind=start, text="    Start      ", background=vec(0.7, 0.9, 0.95))
pauseButton = button(bind=pause, text="       Pause        ", background=vec(0.7, 0.9, 0.95))
resetButton = button(bind=reset, text="       Reset        ", background=vec(0.7, 0.9, 0.95))
speedButton = button(bind=speed_up, text="      Speed Up       ", background=vec(0.7, 0.9, 0.95))
enableButton = button(bind=toggle_trail, text="     Enable Trail     ", background=vec(0.7, 0.9, 0.95))
scene.append_to_caption("\n\n")
scene.append_to_caption("\t")
preset1Button = button(bind=preset1, text="     Preset 1       ", background=vec(0.7, 0.9, 0.95))
preset2Button = button(bind=preset2, text="     Preset 2      ", background=vec(0.7, 0.9, 0.95))
preset3Button = button(bind=preset3, text="     Preset 3      ", background=vec(0.7, 0.9, 0.95))
scene.append_to_caption("\n\n")

scene.append_to_caption("\t<b>Mass of Swinging Ball</b>\n")
scene.append_to_caption("\n\t")
wtext(text="1.0 kg  ")
mass1slider = slider(min=1.0, max=10.0, value=1.0, length=300, bind=updatemass1)
wtext(text="  10.0 kg")
scene.append_to_caption("\n\n")
    
scene.append_to_caption("\t<b>Mass of Ball</b>\n")
scene.append_to_caption("\n\t")
wtext(text="1.0 kg  ")
mass2slider = slider(min=1.0, max=10.0, value=1.0, length=300, bind=updatemass2)
wtext(text="  10.0 kg")
scene.append_to_caption("\n\n")

scene.append_to_caption("\t<b>Length of Swinging part of string</b>\n")
scene.append_to_caption("\n\t")
wtext(text="1.0 cm  ")
string1slider = slider(min=1.0, max=10.0, value=5.0, length=300, bind=updatestring1)
wtext(text="  10.0 cm")
scene.append_to_caption("\n\n")

scene.append_to_caption("\t<b>Length of not Swinging part of string</b>\n")
scene.append_to_caption("\n\t")
wtext(text="1.0 cm  ")
string2slider = slider(min=1.0, max=10.0, value=5.0, length=300, bind=updatestring2)
wtext(text="  10.0 cm")
scene.append_to_caption("\n\n")

scene.append_to_caption("\t<b>Starting Angle</b>\n")
scene.append_to_caption("\n\t")
wtext(text="0°  ")
angleslider = slider(min=0, max=pi/2, value=0.5, length=300, bind=updateangle)
wtext(text="  90°")
scene.append_to_caption("\n\n")
    
scene.append_to_caption("\t<b>Mass of pivots</b>\n")
scene.append_to_caption("\n\t")
wtext(text="0 kg  ")
pmassslider = slider(min=0, max=10.0, value=0, length=300, bind=updatepmass)
wtext(text="  10.0 kg")
scene.append_to_caption("\n\n")

scene.append_to_caption("\t<b>Radius of pivots</b>\n")
scene.append_to_caption("\n\t")
wtext(text="0 cm  ")
pradiusslider = slider(min=0, max=10.0, value=0, length=300, bind=updatepradius)
wtext(text="  10.0 cm")
scene.append_to_caption("\n\n")

pivot1 = sphere(pos=vector(-5, 5, 0), radius=0.3, color=color.white)
pivot2 = sphere(pos=vector(7, 5, 0), radius=0.3, color=color.white)
bridge_string = curve(pos=[pivot2.pos, pivot1.pos], color=vec(0.7, 0.9, 0.95))

mass1 = sphere(pos=vector(-5, 0, 0), color=color.blue, radius=1, make_trail=False)
mass1label = label(pos=mass1.pos, text="1.0 kg", box=False)

mass2 = sphere(pos=vector(7, 0, 0), color=color.red, radius=1, make_trail=False)
mass2label = label(pos=mass2.pos, text="1.0 kg", box=False)

string1 = curve(color=vec(0.7, 0.9, 0.95))
string2 = curve(color=vec(0.7, 0.9, 0.95))

pmass1label = label(pos=pivot1.pos, text="0.0 kg", yoffset=15, box=False)
pmass2label = label(pos=pivot2.pos, text="0.0 kg", yoffset=15, box=False)

pradius1label = label(pos=pivot1.pos, text="0.0 cm", xoffset=30, yoffset=15, box=False)
pradius2label = label(pos=pivot2.pos, text="0.0 cm", xoffset=30, yoffset=15, box=False)

def update_visuals():
    bottom1 = pivot1.pos + vector(-l1 * sin(theta), -l1 * cos(theta), 0)
    mass1.pos = bottom1
    mass1label.pos = mass1.pos
    
    string1.clear()
    string1.append(pos=pivot1.pos)
    string1.append(pos=bottom1)
    
    bottom2 = pivot2.pos + vector(0, -(L - l1), 0)
    mass2.pos = bottom2
    mass2label.pos = mass2.pos
    
    string2.clear()
    string2.append(pos=pivot2.pos)
    string2.append(pos=bottom2)

reset(None)

while True:
    rate(500)
    
    if not running:
        mass1label.pos = mass1.pos
        mass2label.pos = mass2.pos
        continue

    for e in range(speed_multiplier):
        effective_mass_denominator = m1 + m2 + mpivot
        
        rdd = (
            m1 * l1 * (omega ** 2) 
            - g * (m2 - m1 * cos(theta))
        ) / effective_mass_denominator

        thetaddot = (
            -g * sin(theta) 
            - 2 * rd * omega
        ) / l1

        rd += rdd * dt
        omega += thetaddot * dt

        l1 += rd * dt
        theta += omega * dt

        if l1 < 0.1:
            l1 = 0.1
            rd = 0
        if l1 > L - 0.1:
            l1 = L - 0.1
            rd = 0

    update_visuals()
