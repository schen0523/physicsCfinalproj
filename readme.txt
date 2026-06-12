Web VPython 3.2

scene.height = 0
scene.width = 0
box()

scene.caption = """
<b style="font-size:24px;">Swinging Atwood Machine (SAM)</b><br>
<b style="font-size:20px;">Serena Chen, Kyle Liu</b><br>
<b style="font-size:18px;">Introduction</b><br>
Our project is a simulation of the Swinging Atwood Machine (SAM). The setup consists of two masses that are connected by a string that sits on two pivots. 
In our simulation, we will assume that there is no air resistance, no friction, and a massless string.
The user will be able to control different aspects of the simulation and see how each one affects the orbit of the swinging mass. 
This simulation will be able to reproduce the non-linear oscillations and chaotic dynamics created by this system. 

<b style="font-size:18px;">UI & Instructions</b><br>
Our user interface will consist of buttons and sliders. 
The user will not be able to adjust the sliders while the simulation is running. 
The reset button resets the simulation to the conditions the user had set before pressing the start button. 
The multi-mode button runs 25 swinging atwood machines at the same time. Each one varies slightly by the last slider that the user changed.
If the user did not change any sliders, it defaults to small variations in the angle. 
For example, if the last slider the user adjusted is the mass of the swinging ball, the 25 different balls will all have slightly different masses.
The user will be able to observe how these conditions affect the swinging mass overtime as this system is extremely sensitive to its initial conditions. 
There are also three different preset conditions that produce satisfying oscillations.
Note that trails may become blocky if the ball moves too fast when sped up. Additionally, the simulation may lag or slow down in multi-mode. 

<b style="font-size:18px;">Derivation of Equations of Motion</b><br>
There will be two parts to the derivation: one with massless pivots and the other with large pulleys. 
Assumptions can be made about the system, including negligible air resistance, massless strings, zero initial velocity, and the conservation of energy.

<b style="font-size:16px;">Variables</b><br>
<table border="1" cellspacing="0" cellpadding="6">
    <thead>
        <tr>
            <th>Symbol</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><i>m</i><sub>1</sub></td>
            <td>Mass of swinging ball (kg)</td>
        </tr>
        <tr>
            <td><i>m</i><sub>2</sub></td>
            <td>Mass of non-swinging ball (kg)</td>
        </tr>
        <tr>
            <td><i>r</i><sub>1</sub></td>
            <td>Distance from pivot to swinging mass (m)</td>
        </tr>
        <tr>
            <td><i>r</i><sub>2</sub></td>
            <td>Distance from pivot to non-swinging mass (m)</td>
        </tr>
        <tr>
            <td>&theta;</td>
            <td>Angular displacement (rad)</td>
        </tr>
        <tr>
            <td>r&#775;</td>
            <td>Radial speed (m/s)</td>
        </tr>
        <tr>
            <td><i>g</i></td>
            <td>Gravitational acceleration (9.81 m/s²)</td>
        </tr>
        <tr>
            <td><i>L</i></td>
            <td>Total rope length (m)</td>
        </tr>
    </tbody>
</table>

<b style="font-size:16px;">Massless Pivots</b><br>
Our derivation will be using Lagrangian mechanics:

\\( \mathcal{L} = K - U \\)

where \\( K \\) is the kinetic energy and \\( U \\) is the potential energy of the system. 

\\( K = \\frac{1}{2}m_1( \\dot{r}^2+ r_1^2\\dot{\\theta}^2) + \\frac{1}{2}m_2\\dot{r}^2 \\)

\\( U = m_1g(-r_1\\cos{\\theta}) + m_2g(-r_2) \\)

Combining these, we get 

\\( \mathcal{L} = \\frac{1}{2}m_1( \\dot{r}^2+ r_1^2\\dot{\\theta}^2) + \\frac{1}{2}m_2\\dot{r}^2 +m_1r_1\\cos{\\theta}g + m_2r_2g 
= \\frac{1}{2}(m_1+m_2)\\dot{r}^2 + \\frac{1}{2}m_1r_1^2\\dot{\\theta}^2 +m_1r_1\\cos{\\theta}g + m_2r_2g \\)

Next, we will be using the Euler-Lagrange equation, which is defined as:

\\( \\frac{\\partial \mathcal{L}}{\\partial f} - \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial f^\\prime}\\right) = 0 \\)

We can substitute the equations we derived above into the Euler-Lagrange equation, replacing \\( f \\) with \\(r \\):

\\( \\frac{\\partial \mathcal{L}}{\\partial r} = \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{r}}\\right) \\)

\\( \\frac{\\partial \mathcal{L}}{\\partial r}
= \\frac{\\partial}{\\partial r}\\left[ \\frac{1}{2}m_1r_1^2\\dot{\\theta}^2 + mgr_1\\cos{\\theta} + m_2gr_2\\right]
= \\frac{\\partial}{\\partial r}\\left[ \\frac{1}{2}m_1r_1^2\dot{\\theta}^2 + mgr_1\cos{\\theta} + m_2g(L-r_1)\\right] 
= m_1r_1\\dot{\\theta}^2 + m_1g\\cos{\\theta} - m_2g \\)

\\( \\frac{\\partial \mathcal{L}}{\\partial \\dot{r}}
= \\frac{\\partial}{\\partial \\dot{r}}\\left[ \\frac{1}{2}(m_1+m_2)\\dot{r}^2\\right]
= (m_1+m_2)\\dot{r} \\)

\\( \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{r}}\\right)
= \\frac{d}{dt}\\left[(m_1+m_2)\\dot{r}\\right]
= (m_1+m_2)\\ddot{r} \\)

Finally, we get 

\\( m_1r_1\\dot{\\theta}^2 + m_1g\\cos{\\theta} - m_2g = (m_1+m_2)\\ddot{r} \\)

We can solve this equation for \\( \\ddot{r} \\) to get

\\( \\boxed{\\ddot{r} = \\frac{m_1r_1\\dot{\\theta}^2 + m_1g\\cos{\\theta} - m_2g}{m_1+m_2}} \\)

We can also replace \\(f \\) with \\( \\theta \\) in the Euler-Lagrange equation:

\\( \\frac{\\partial \mathcal{L}}{\\partial \\theta} = \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{\\theta}}\\right)
\\frac{\\partial \mathcal{L}}{\\partial \\theta}
= \\frac{\\partial}{\\partial \\theta}\\left[mgr_1\\cos{\\theta}\\right]
= -mgr_1\\sin{\\theta} \\)

\\( \\frac{\\partial \mathcal{L}}{\\partial \\dot{\\theta}}
= \\frac{\\partial}{\\partial \\dot{\\theta}}\\left[ \\frac{1}{2}m_1r_1^2\\dot{\\theta}^2\\right]
= m_1r_1^2\\dot{\\theta} \\)

\\( \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{\\theta}}\\right)
= \\frac{d}{dt}\\left[m_1r_1^2\\dot{\\theta}\\right]
= m_1(2r_1\\dot{r}\\dot{\\theta} + r_1^2\\ddot{\\theta}) \\)

Note that this equation was derived using the product rule since both \\( r_1 \\) and \\( \\theta \\) vary with time.

Substituting in the equations above, we get

\\( -m_1gr_1\\sin{\\theta} = m_1(2r_1\\dot{r}\\dot{\\theta} + r_1^2\\ddot{\\theta}) \\)

We can solve the equation for \\( \\ddot{\\theta} \\) to get

\\( \\boxed{\\ddot{\\theta} = \\frac{-g\\sin{\\theta} - 2\\dot{r}\\dot{\\theta}}{r_1}} \\)

With \\( \\ddot{r} \\) and \\( \ddot{\\theta} \\), we can find \\( r_1 \\) and \\( \\theta \\) at any time \\( t \\) using Euler's method.

<b style="font-size:16px;">Large Pulleys</b><br>
For the derivation with large pulleys, it is very similar to the derivation with massless pulley, except now we include rotational kinetic energy of the pivots. 
We assume that both pivots are uniform discs and have the same mass and radius.

Once again, we start with the Lagrangian:

\\( \mathcal{L} = K - U \\)
\\( K = \\frac{1}{2}m_1( \\dot{r}^2+ r_1^2\\dot{\\theta}^2) + \\frac{1}{2}m_2\\dot{r}^2 + I\\left(\\frac{\\dot{r}}{R}\\right)^2 \\)
\\( U = m_1g(-r_1\\cos{\\theta}) + m_2g(r_1-L) \\)

where \\( I \\) is the moment of inertia of one pivot and \\( R \\) is the radius of one pivot.

We can get the Lagrangian to be,

\\( \mathcal{L} = \\frac{1}{2}(m_1+m_2+2\\frac{I}{R^2})\\dot{r}^2 + \\frac{1}{2}m_1r_1^2\\dot{\\theta}^2 + m_1gr_1\\cos{\\theta} + m_2g(L-r_1) \\)

Using the Euler-Lagrange equation,

\\( \\frac{\\partial \mathcal{L}}{\\partial r} = \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{r}}\\right) \\)

\\( \\frac{\\partial \mathcal{L}}{\\partial r} = \\frac{\\partial}{\\partial r}\\left[\\frac{1}{2}m_1r_1^2\\dot{\\theta}^2 + m_1gr_1\\cos{\\theta}+m_2g(L-r_1)\\right]
= m_1r_1\\dot{\\theta}^2+m_1g\\cos{\\theta}-m_2g \\)

\\( \\frac{\\partial \mathcal{L}}{\\partial \\dot{r}} = \\frac{\\partial}{\\partial \\dot{r}}\\left[ \\frac{1}{2}(m_1+m_2+2\\frac{I}{R^2})\\dot{r}^2\\right]
= (m_1+m_2+2\\frac{I}{R^2})\\dot{r} \\)

\\( \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{r}}\\right)
= \\frac{d}{dt}\\left[(m_1+m_2+2\\frac{I}{R^2})\\dot{r}\\right]
= (m_1+m_2+2\\frac{I}{R^2})\\ddot{r} \\)

In the end, we get

\\( m_1r_1\\dot{\\theta}^2+m_1g\\cos{\\theta}-m_2g = (m_1+m_2+2\\frac{I}{R^2})\\ddot{r} \\)

Rearranging the equation, the result is

\\( \\boxed{\\ddot{r} = \\frac{m_1r_1\\dot{\\theta} + g(m_1\\cos{\\theta} - m_2)}{m_1+m_2+2\\frac{I}{R^2}}} \\)

We can do the same for \\( \\theta \\):

\\( \\frac{\\partial \mathcal{L}}{\\partial \\theta} = \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{\\theta}}\\right) \\)

\\( \\frac{\\partial \mathcal{L}}{\\partial \\theta} = \\frac{\\partial}{\\partial \\theta}\\left[m_1gr_1\\cos{\\theta}\\right]= -m_1gr_1\\sin{\\theta} \\)

\\( \\frac{\\partial \mathcal{L}}{\\partial \\dot{\\theta}} = \\frac{\\partial}{\\partial \\theta}\\left[\\frac{1}{2}m_1r_1^2\\dot{\\theta}^2\\right] 
= m_1r_1^2\\dot{\\theta} \\)

\\( \\frac{d}{dt}\\left(\\frac{\\partial \mathcal{L}}{\\partial \\dot{\\theta}}\\right)
= \\frac{d}{dt}\\left[m_1r_1^2\\dot{\\theta}\\right]
= 2m_1r_1\\dot{r}\\dot{\\theta} + m_1r_1^2\\ddot{\\theta} \\)

We end up with,

\\( -m_1gr_1\\sin{\\theta} = 2m_1r_1\\dot{r}\\dot{\\theta} + m_1r_1^2\\ddot{\\theta} \\)

This results in

\\( \\boxed{\\ddot{\\theta}=\\frac{-g\\sin{\\theta}-2\\dot{r}\\dot{\\theta}}{r_1}} \\)

Using Euler's method, we can once again find \\( r_1 \\) and \\( \\theta \\) at any time \\( t \\)."""

MathJax.Hub.Queue(["Typeset",MathJax.Hub,scene.caption])