import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

import  game

def ButtonCallback(event):
    global gravity, velocity, height, fuel
    """closing the window, run the game"""
    plt.close()
    #running the game
    game.run_game(height, gravity, velocity, fuel)

#updating values using widgets callacks
def gravityCallback(gravity_new):
    """assign gravity value"""
    global gravity
    gravity = float(gravity_new)

def heightCallback(height_new):
    """assign height value"""
    global height
    height = float(height_new)

def fuelCallback(fuel_new):
    """assign fuel value"""
    global fuel
    fuel = float(fuel_new)

def velocityCallback(vel_new):
    """assign velocity value"""
    global velocity
    velocity = float(vel_new)

#creaating start screen
#create window
fig = plt.figure(figsize=(5, 5))

#writing title, rules and controls
tax = plt.axes([0.3, 0.9, 0.4, 0.1])
tax.text(0.5, 0.5, 'Lunar Lander', fontsize=18,  horizontalalignment='center',\
    verticalalignment='center')
tax.set_axis_off()

tax1 = plt.axes([0.1, 0.8, 0.8, 0.07])
aim = 'Aim: land a lunar lander slower than max safe landing velocity'
tax1.text(0.5, 0.5, aim, fontsize=10, verticalalignment='center', \
    horizontalalignment='center')
tax1.set_axis_off()

tax2 = plt.axes([0.1, 0.75, 0.8, 0.07])
controls1 = 'Press Space to turn on the engine.'
tax2.text(0.5, 0.5, controls1, fontsize=10, horizontalalignment='center',\
    verticalalignment='center')
tax2.set_axis_off()

tax3 = plt.axes([0.1, 0.7, 0.8, 0.07])
controls2 = "Hold Space and use up and down arrows to control thrust"
tax3.text(0.5, 0.5, controls2, fontsize=10, horizontalalignment='center',\
    verticalalignment='center')
tax3.set_axis_off()

#settings
#title
tax4 = plt.axes([0.4, 0.5, 0.2, 0.1])
tax4.text(0.5, 0.5, 'Settings', fontsize=14, horizontalalignment='center',\
    verticalalignment='center')
tax4.set_axis_off()

#initial height
bax = plt.axes([0.43, 0.45, 0.15, 0.07])
height = 100
boxHandle = widgets.TextBox(bax, 'Initial Height ', initial=str(height))
boxHandle.on_submit(heightCallback)

#gravity
bax1 = plt.axes([0.43, 0.35, 0.15, 0.07])
gravity = -1
boxHandle1 = widgets.TextBox(bax1, 'Acceleration due to gravity ', initial=str(gravity))
boxHandle1.on_submit(gravityCallback)

#fuel
fuel = 100
bax2 = plt.axes([0.43, 0.25, 0.15, 0.07])
boxHandle2 = widgets.TextBox(bax2, 'Fuel', initial=str(fuel))
boxHandle2.on_submit(fuelCallback)

#velocity slider
velocity = 3
sax = plt.axes([0.3, 0.17, 0.4, 0.05])
sliderHandle = widgets.Slider(sax, 'Max landing velocity', valmin=1, valmax=10, valinit=velocity, \
    valstep=1, valfmt='%d')
sliderHandle.on_changed(velocityCallback)


#play button
bax4 = plt.axes([0.4, 0.02, 0.2, 0.1])
buttonHandle = widgets.Button(bax4, 'Play!')
buttonHandle.on_clicked(ButtonCallback)

plt.show()
