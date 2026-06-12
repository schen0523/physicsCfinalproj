Web VPython 3.2

running = False
speed_multiplier = 1
trail = False
labels = True
g = 9.81
m1 = 1.0       # swinging mass
m2 = 1.0       # non swinging mass
mpivot = 0.0   # mass of each pulley
rpivot = 0.0   # radius of each pulley
l1 = 5.0       # r (distance from pulley to swinging mass)
l2 = 5.0       
L = 10.0       # total rope length
rd = 0.0       # r dot (radial velocity)
theta = 0.0    # theta
omega = 0.0 
dt = 0.001

multi_mode = False
last_changed = "theta" 
simulations = []
step_counter = 0        

BLUE = vec(0.7, 0.9, 0.95)
RED = vec(0.95, 0.7, 0.7)

def toggle_run(button):
    global running
    running = not running
    if running:
        button.text = "Pause".center(24)
        button.background = RED
        set_controls_disabled(True)
    else:
        button.text = "Start".center(24)
        button.background = BLUE
        set_controls_disabled(False)

def set_controls_disabled(setting):
    mass1slider.disabled = setting
    mass2slider.disabled = setting
    string1slider.disabled = setting
    string2slider.disabled = setting
    angleslider.disabled = setting
    pmassslider.disabled = setting
    pradiusslider.disabled = setting
    preset1Button.disabled = setting
    preset2Button.disabled = setting
    preset3Button.disabled = setting

def reset(button): 
    global running, l1, L, theta, rd, omega, gPhase, rPhase
    running = False
    runButton.text = "Start".center(24)
    runButton.background = BLUE
    set_controls_disabled(False)
    l1 = string1slider.value
    L = l1 + string2slider.value
    theta = angleslider.value
    rd = 0.0
    omega = 0.0
    
    gPhase.delete()
    rPhase.delete()
    gPhase = gcurve(color=color.blue, graph=gPhasePlot)
    rPhase = gcurve(color=color.red, graph=rPhasePlot)
    
    if trail:
        mass1.clear_trail()
    
    if multi_mode:
        setup_multi()
    else:
        update_visuals()

def speed_up(button):
    global speed_multiplier
    if speed_multiplier == 1:
        speed_multiplier = 10
        button.text = "Normal Speed".center(24)
        button.background = RED
    else:
        speed_multiplier = 1
        button.text = "Speed Up".center(24)
        button.background = BLUE

def toggle_trail(button):
    global trail
    trail = not trail
    mass1.make_trail = trail
    if multi_mode:
        for sim in simulations:
            sim['mass1'].make_trail = trail
            if not trail:
                sim['mass1'].clear_trail()
    if trail:
        button.text = "Disable Trail".center(24)
        button.background = RED
    else:
        button.text = "Enable Trail".center(24)
        button.background = BLUE
        mass1.clear_trail()
        
def toggle_label(button):
    global labels
    labels = not labels
    
    if labels:
        button.text = "Disable Labels".center(24)
        button.background = RED
    else:
        button.text = "Enable Labels".center(24)
        button.background = BLUE
        
    mass1label.visible = labels
    mass2label.visible = labels
    pmass1label.visible = labels
    pmass2label.visible = labels
    pradius1label.visible = labels
    pradius2label.visible = labels

def toggle_multi(button):
    global multi_mode, gPhase, rPhase
    multi_mode = not multi_mode
    if multi_mode:
        button.text = "Disable Multi-Mode".center(24)
        button.background = RED
        gPhase.delete()
        rPhase.delete()
        gPhase = gcurve(color=color.blue, graph=gPhasePlot)
        rPhase = gcurve(color=color.red, graph=rPhasePlot)
        setup_multi()
    else:
        button.text = "Enable Multi-Mode".center(24)
        button.background = BLUE
        clear_multi()
        reset(None)

def setup_multi():
    global simulations, running
    running = False
    runButton.text = "Start".center(24)
    runButton.background = BLUE
    set_controls_disabled(False)
    clear_multi()
    
    mass1.visible = False
    mass2.visible = False
    string1.visible = False
    string2.visible = False
    
    base_theta = angleslider.value
    base_m1 = mass1slider.value
    base_m2 = mass2slider.value
    base_l1 = string1slider.value
    base_l2 = string2slider.value
    base_mpivot = pmassslider.value
    base_rpivot = pradiusslider.value
    
    if labels:
        mass1label.visible = True
        mass2label.visible = True
        mass1label.text = f"{base_m1:.4f} kg"
        mass2label.text = f"{base_m2:.4f} kg"
    else:
        mass1label.visible = False
        mass2label.visible = False
    
    for i in range(25):
        offset = i - 12
        
        inst_theta = base_theta + offset * 0.01 if last_changed == "theta" else base_theta
        inst_m1 = max(0.1, base_m1 + offset * 0.02) if last_changed == "m1" else base_m1
        inst_m2 = max(0.1, base_m2 + offset * 0.02) if last_changed == "m2" else base_m2
        inst_l1 = max(0.2, base_l1 + offset * 0.05) if last_changed == "l1" else base_l1
        inst_l2 = max(0.2, base_l2 + offset * 0.05) if last_changed == "l2" else base_l2
        inst_mpivot = max(0.0, base_mpivot + offset * 0.02) if last_changed == "mpivot" else base_mpivot
        inst_rpivot = max(0.01, base_rpivot + offset * 0.02) if last_changed == "rpivot" else base_rpivot
        
        inst_L = inst_l1 + inst_l2
        
        bottom1 = pivot1.pos + vector(inst_l1 * sin(-inst_theta), -inst_l1 * cos(-inst_theta), 0)
        bottom2 = pivot2.pos + vector(0, -(inst_L - inst_l1), 0)
        
        hue = i / 25
        inst_color = color.hsv_to_rgb(vec(hue, 1, 1))
        
        s1 = curve(color=inst_color, radius=0.02)
        s2 = curve(color=inst_color, radius=0.02)
        
        m1_obj = sphere(pos=bottom1, color=inst_color, radius=pow(inst_m1, 1/3) * 0.3, make_trail=trail)
        m2_obj = sphere(pos=bottom2, color=inst_color, radius=pow(inst_m2, 1/3) * 0.3, make_trail=False)
        
        g_curve = gcurve(color=inst_color, graph=gPhasePlot)
        r_curve = gcurve(color=inst_color, graph=rPhasePlot)
        
        simulations.append({
            'm1': inst_m1, 'm2': inst_m2, 'l1': inst_l1, 'L': inst_L, 'theta': inst_theta,
            'mpivot': inst_mpivot, 'rpivot': inst_rpivot,
            'rd': 0.0, 'omega': 0.0, 'string1': s1, 'string2': s2,
            'mass1': m1_obj, 'mass2': m2_obj, 'gcurve': g_curve, 'rcurve': r_curve
        })
    update_multi_visuals()

def clear_multi():
    global simulations
    for sim in simulations:
        sim['string1'].clear()
        sim['string2'].clear()
        sim['mass1'].clear_trail()
        sim['mass1'].visible = False
        sim['mass2'].visible = False
        sim['gcurve'].delete()
        sim['rcurve'].delete()
    simulations = []
    
    mass1.visible = True
    mass2.visible = True
    string1.visible = True
    string2.visible = True
    if labels:
        mass1label.visible = True
        mass2label.visible = True
        mass1label.text = f"{m1:.4f} kg"
        mass2label.text = f"{m2:.4f} kg"

def update_multi_visuals():
    for i, sim in enumerate(simulations):
        current_l1 = sim['l1']
        current_theta = sim['theta']
        current_L = sim['L']
        
        bottom1 = pivot1.pos + vector(current_l1 * sin(-current_theta), -current_l1 * cos(-current_theta), 0)
        sim['mass1'].pos = bottom1
        sim['string1'].clear()
        sim['string1'].append(pos=pivot1.pos)
        sim['string1'].append(pos=bottom1)
        
        bottom2 = pivot2.pos + vector(0, -(current_L - current_l1), 0)
        sim['mass2'].pos = bottom2
        sim['string2'].clear()
        sim['string2'].append(pos=pivot2.pos)
        sim['string2'].append(pos=bottom2)
        
        if i == 12 and labels:
            mass1label.pos = bottom1
            mass2label.pos = bottom2

def preset1(button):
    mass1slider.value = 1.0; updatemass1(mass1slider)
    mass2slider.value = 1.555; updatemass2(mass2slider)
    string1slider.value = 5.0; updatestring1(string1slider)
    string2slider.value = 5.0; updatestring2(string2slider)
    angleslider.value = pi/2; updateangle(angleslider)
    reset(None)

def preset2(button):
    mass1slider.value = 1.0; updatemass1(mass1slider)
    mass2slider.value = 1.665; updatemass2(mass2slider)
    string1slider.value = 5.0; updatestring1(string1slider)
    string2slider.value = 5.0; updatestring2(string2slider)
    angleslider.value = pi/2; updateangle(angleslider)
    reset(None)
    
def preset3(button):
    mass1slider.value = 1; updatemass1(mass1slider)
    mass2slider.value = 6; updatemass2(mass2slider)
    string1slider.value = 5.0; updatestring1(string1slider)
    string2slider.value = 5.0; updatestring2(string2slider)
    angleslider.value = pi/2; updateangle(angleslider)
    reset(None)

def updatemass1(slider):
    global m1, last_changed
    m1 = slider.value
    last_changed = "m1"
    if labels and not multi_mode:
        mass1label.text = f"{m1:.4f} kg"
    mass1.radius = pow(m1, 1/3) * 0.5
    if multi_mode and not running: setup_multi()

def updatemass2(slider):
    global m2, last_changed
    m2 = slider.value
    last_changed = "m2"
    if labels and not multi_mode:
        mass2label.text = f"{m2:.4f} kg"
    mass2.radius = pow(m2, 1/3) * 0.5
    if multi_mode and not running: setup_multi()

def updatestring1(slider):
    global l1, L, last_changed
    l1 = slider.value
    last_changed = "l1"
    if not running:
        L = l1 + string2slider.value
        if multi_mode: setup_multi()
        else: update_visuals()

def updatestring2(slider):
    global L, last_changed
    last_changed = "l2"
    if not running:
        L = string1slider.value + slider.value
        if multi_mode: setup_multi()
        else: update_visuals()

def updateangle(slider):
    global theta, last_changed
    theta = slider.value
    last_changed = "theta"
    if not running:
        if multi_mode: setup_multi()
        else: update_visuals()

def updatepmass(slider):
    global mpivot, last_changed
    mpivot = slider.value
    last_changed = "mpivot"
    if labels:
        pmass1label.text = f"{mpivot:.3f} kg"
        pmass2label.text = f"{mpivot:.3f} kg"
    if multi_mode and not running: setup_multi()

def updatepradius(slider):
    global rpivot, last_changed
    rpivot = slider.value
    last_changed = "rpivot"
    if labels:
        pradius1label.text = f"{rpivot:.3f} cm "
        pradius2label.text = f"{rpivot:.3f} cm "
    pivot1.radius = max(0.3, rpivot / 10.0)
    pivot2.radius = max(0.3, rpivot / 10.0)
    if multi_mode and not running: setup_multi()

scene = canvas(title='Swinging Atwood Machine (SAM)', align='left', width=600, height=400)
scene.append_to_caption("\t")
x
runButton = button(bind=toggle_run, text="Start".center(24), background=BLUE)
resetButton = button(bind=reset, text="Reset".center(24), background=BLUE)
speedButton = button(bind=speed_up, text="Speed Up".center(24), background=BLUE)
trailButton = button(bind=toggle_trail, text="Enable Trail".center(24), background=BLUE)
labelButton = button(bind=toggle_label, text="Disable Labels".center(24), background=RED)
multiButton = button(bind=toggle_multi, text="Enable Multi-Mode".center(24), background=BLUE)

scene.append_to_caption("\n\n")
scene.append_to_caption("\t")
preset1Button = button(bind=preset1, text="Preset 1".center(24), background=BLUE)
preset2Button = button(bind=preset2, text="Preset 2".center(24), background=BLUE)
preset3Button = button(bind=preset3, text="Preset 3".center(24), background=BLUE)

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

mass1 = sphere(pos=vector(-5, 0, 0), color=color.blue, radius=0.5, make_trail=False)
mass1label = label(pos=mass1.pos, text="1.0 kg", box=False)

mass2 = sphere(pos=vector(7, 0, 0), color=color.red, radius=0.5, make_trail=False)
mass2label = label(pos=mass2.pos, text="1.0 kg", box=False)

string1 = curve(color=vec(0.7, 0.9, 0.95))
string2 = curve(color=vec(0.7, 0.9, 0.95))

pmass1label = label(pos=pivot1.pos, text="0.0 kg", yoffset=15, box=False)
pmass2label = label(pos=pivot2.pos, text="0.0 kg", yoffset=15, box=False)

pradius1label = label(pos=pivot1.pos, text="0.0 cm", xoffset=30, yoffset=15, box=False)
pradius2label = label(pos=pivot2.pos, text="0.0 cm", xoffset=30, yoffset=15, box=False)

gPhasePlot = graph(title="Angular Phase Space", xtitle="theta (rad)", ytitle="omega(rad/s)")
gPhase = gcurve(color=color.blue, graph=gPhasePlot) 

rPhasePlot = graph(title="Radial Phase Space", xtitle="r (cm)", ytitle="rdot (cm/s)")
rPhase = gcurve(color=color.red, graph=rPhasePlot) 

def update_visuals():
    bottom1 = pivot1.pos + vector(l1 * sin(-theta), -l1 * cos(-theta), 0)
    
    if trail and not running:
        mass1.make_trail = False
        mass1.pos = bottom1
        mass1.make_trail = True
        mass1.clear_trail()
    else:
        mass1.pos = bottom1
        
    string1.clear()
    string1.append(pos=pivot1.pos)
    string1.append(pos=bottom1)
    
    bottom2 = pivot2.pos + vector(0, -(L - l1), 0)
    mass2.pos = bottom2
    
    string2.clear()
    string2.append(pos=pivot2.pos)
    string2.append(pos=bottom2)
    
    if labels:
        mass1label.pos = mass1.pos
        mass2label.pos = mass2.pos

reset(None)

while True:
    running_rate = 500
    rate(running_rate)
    
    if not running:
        if not multi_mode:
            mass1label.pos = mass1.pos
            mass2label.pos = mass2.pos
        else:
            if labels and len(simulations) > 12:
                mass1label.pos = simulations[12]['mass1'].pos
                mass2label.pos = simulations[12]['mass2'].pos
        continue

    if mpivot > 0 and rpivot <= 0:
        pradiusslider.value = 0.5
        updatepradius(pradiusslider)

    base_L = string1slider.value + string2slider.value

    for e in range(speed_multiplier):
        step_counter += 1
        if multi_mode:
            for sim in simulations:
                m1_v = sim['m1']
                m2_v = sim['m2']
                l1_v = sim['l1']
                L_v = sim['L']
                theta_v = sim['theta']
                rd_v = sim['rd']
                omega_v = sim['omega']
                mp_v = sim['mpivot']
                rp_v = sim['rpivot']
                
                if mp_v > 0:
                    I_v = (1/2) * mp_v * (rp_v ** 2)
                    rdd = (m1_v * l1_v * omega_v + g * (m1_v * cos(theta_v) - m2_v)) / (m1_v + m2_v + ((2 * I_v) / (rp_v ** 2)))
                    thetadd = (-g * sin(theta_v) - 2 * rd_v * omega_v) / l1_v
                else:
                    rdd = (m1_v * l1_v * (omega_v ** 2) + m1_v * g * cos(theta_v) - m2_v * g) / (m1_v + m2_v)
                    thetadd = (-g * sin(theta_v) - 2 * rd_v * omega_v) / l1_v

                rd_v += rdd * dt
                omega_v += thetadd * dt
                l1_v += rd_v * dt
                theta_v += omega_v * dt

                if l1_v < 0.1:
                    l1_v = 0.1
                    rd_v = 0
                if l1_v > L_v - 0.1:
                    l1_v = L_v - 0.1
                    rd_v = 0

                sim['l1'] = l1_v
                sim['theta'] = theta_v
                sim['rd'] = rd_v
                sim['omega'] = omega_v

                if step_counter % 20 == 0:
                    sim['gcurve'].plot(theta_v, omega_v)
                    sim['rcurve'].plot(l1_v, rd_v)
        else:
            if mpivot > 0:
                I = (1/2) * mpivot * (rpivot ** 2)
                rdd = (m1 * l1 * omega + g * (m1 * cos(theta) - m2)) / (m1 + m2 + ((2 * I) / (rpivot ** 2)))
                thetadd = (-g * sin(theta) - 2 * rd * omega) / l1
            else:
                rdd = (m1 * l1 * (omega ** 2) + m1 * g * cos(theta) - m2 * g) / (m1 + m2)
                thetadd = (-g * sin(theta) - 2 * rd * omega) / l1

            rd += rdd * dt
            omega += thetadd * dt
            l1 += rd * dt
            theta += omega * dt

            if l1 < 0.1:
                l1 = 0.1
                rd = 0
            if l1 > L - 0.1:
                l1 = L - 0.1
                rd = 0

            if step_counter % 20 == 0:
                gPhase.plot(theta, omega)
                rPhase.plot(l1, rd)

    if multi_mode:
        update_multi_visuals()
    else:
        update_visuals()
