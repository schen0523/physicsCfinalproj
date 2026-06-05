Web VPython 3.2

g = 9.81
m1 = 1     # swinging mass
m2 = 1.5555   # hanging mass
L = 6     # total rope length
r = 2.0       # distance from pulley to swinging mass
rd = 0.0

theta = pi / 2
omega = 0.0

dt = 0.001

scene = canvas(
    width=800,
    height=600,
    background=color.black
)

scene.center = vector(0, -2, 0)

left_pulley = vector(0, 0, 0)
right_pulley = vector(2, 0, 0)

ring(
    pos=left_pulley,
    axis=vector(0,0,1),
    radius=0.001,
    thickness=0.03,
    color=color.white
)

ring(
    pos=right_pulley,
    axis=vector(0,0,1),
    radius=0.001,
    thickness=0.03,
    color=color.white
)


ball1 = sphere(
    pos=vector(
        r*sin(theta),
        -r*cos(theta),
        0
    ),
    radius=0.15,
    color=color.cyan,
    make_trail=True,
    retain=10000, interval=10,
    trail_type = "points"
)

y2 = -(L - r)

ball2 = sphere(
    pos=vector(2, y2, 0),
    radius=0.15,
    color=color.orange
)

rope1 = cylinder(
    pos=left_pulley,
    axis=ball1.pos-left_pulley,
    radius=0.02,
    color=color.white
)

rope_top = cylinder(
    pos=left_pulley,
    axis=right_pulley-left_pulley,
    radius=0.02,
    color=color.white
)

rope2 = cylinder(
    pos=right_pulley,
    axis=ball2.pos-right_pulley,
    radius=0.02,
    color=color.white
)

while True:
    rate(5000)

    rdd = (
        m1*r*omega**2
        - g*(m2 - m1*cos(theta))
    ) / (m1 + m2)

    thetaddot = (
        -g*sin(theta)
        - 2*rd*omega
    ) / r

    rd += rdd*dt
    omega += thetaddot*dt

    r += rd*dt
    theta += omega*dt

    if r < 0.001:
        r = 0.001
        rd = 0

    if r > L - 0.001:
        r = L - 0.001
        rd = 0

    ball1.pos = vector(
        r*sin(theta),
        -r*cos(theta),
        0
    )

    y2 = -(L - r)

    ball2.pos = vector(
        2,
        y2,
        0
    )

    rope1.axis = ball1.pos - left_pulley
    rope2.axis = ball2.pos - right_pulley

    scene.center = vector(1, -L/2, 0)