import mido
import RPi.GPIO as GPIO

gpio_order = [26,19,13,6,5,22,27,17,4,21,20,16,12,25,24,23,18]

GPIO.setmode(GPIO.BCM)
for i in gpio_order:
    GPIO.setup(i, GPIO.OUT)

def update_lights(msg):
    number_lights = 17
    #order from left to right
    #gpio_order = [26,19,13,6,5,22,27,17,4,21,20,16,12,25,24,18]
    # middle c = note 60a
    try:
        current_gpio = msg.note
    except:
        #print("Not a note")
        return


    #print(current_gpio)
    note_to_play = gpio_order[(current_gpio % number_lights)]
    #print("note_to_play =", note_to_play)
    if msg.type == 'note_on':
        on = True
    else:
        on = False

    turn_on_off_lights(note_to_play, on)



def turn_on_off_lights(pin,on):
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,on)

names = mido.get_input_names()
#print(names)
inport = mido.open_input('Clavinova MIDI 1')
while(True):
    msg = inport.receive()
    #print(msg)
    #print(msg.note)
    #print(msg.type)
    update_lights(msg)


