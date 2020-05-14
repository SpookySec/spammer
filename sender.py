from pynput.mouse import Controller, Button
from pynput import keyboard
from pynput.keyboard import Key
from time import sleep

keyboard1 = keyboard.Controller()
mouse = Controller()

input("[+] PLACE YOUR MOUSE ON TYPING AREA AND PRESS ENTER : ")
bar = Controller().position
print("[*] POSITIONS LOGGED!")
print("=== MAKE SURE YOU DON'T MOVE THE MOUSE! ===")
input("[+] PRESS ENTER TO PROCEED")
file = open("words.txt", "r")
lines = file.readlines()
for line in lines:
    word = str(line.rstrip())
    mouse.position = bar
    mouse.click(Button.left)
    keyboard1.type(word)
    keyboard1.press(Key.enter)
    sleep(0.2)
print("[*] FINISHED SENDING!")