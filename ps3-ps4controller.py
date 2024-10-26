from time import sleep
from approxeng.input.selectbinder import ControllerResource, ControllerRequirement
from approxeng.input.dualshock3 import DualShock3
import vgamepad as vg
gamepad = vg.VDS4Gamepad()
def presses_button():
    if 'cross' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    if 'circle' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
    if 'square' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    if 'triangle' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    if 'ddown' in dualshock3.presses:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
    if 'dleft' in dualshock3.presses:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST)
    if 'dright' in dualshock3.presses:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
    if 'dup' in dualshock3.presses:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
    if 'l1' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)        
    if 'r1' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
    if 'start' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS) 
    if 'select' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHARE)  
    if 'home' in dualshock3.presses:
        gamepad.press_special_button(special_button=vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS)
    if 'l2' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
    if 'r2' in dualshock3.presses:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
    gamepad.update()
def release_button():
    if 'cross' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    if 'circle' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
    if 'square' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    if 'triangle' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    if 'ddown' in dualshock3.releases:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
    if 'dleft' in dualshock3.releases:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
    if 'dright' in dualshock3.releases:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
    if 'dup' in dualshock3.releases:
        gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
    if 'l1' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)        
    if 'r1' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
    if 'start' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHARE) 
    if 'select' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)  
    if 'home' in dualshock3.releases:
        gamepad.release_special_button(special_button=vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS)
    if 'l2' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
    if 'r2' in dualshock3.releases:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)
    gamepad.update()    
def sticks():
    lx,ly = dualshock3['lx', 'ly']
    gamepad.left_joystick_float(x_value_float=lx, y_value_float=-ly) 
    rx,ry = dualshock3['rx', 'ry']
    gamepad.right_joystick_float(x_value_float=-ry, y_value_float=-(rx)) 
    gamepad.update()  
while True:
    try:
        with ControllerResource(ControllerRequirement(require_class=DualShock3), hot_zone=0.1, dead_zone=0.1) as dualshock3:
            while dualshock3.connected:
                button_presses = dualshock3.check_presses()
                presses_button() 
                release_button()
                sticks()
                if 'home' in dualshock3.releases:
                    exit()
                sleep(0.1)
    except IOError:
        print('No controller found yet')
        sleep(1)

