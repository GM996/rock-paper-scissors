counter = 0

def on_gesture_shake2():
     hand = randint(1, 3)
    if hand == 1:
       basic.show_icon(IconNames.SQUARE)
    elif hand == 2:
         basic.show_icon(IconNames.SMALL_SQUARE)
    else:
         basic.show_icon(IconNames.SCISSORS)
         pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake2)

def on_button_pressed_a():
    global counter
    counter += 1 
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(counter)
input.on_button_pressed(Button.B, on_button_pressed_b)