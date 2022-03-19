from pynput.keyboard import Key, Controller
import time
from timeit import default_timer as timer

cmds = ['hunt', 'fish', 'beg', 'dig', 'dep all']

cooldowns = [43, 44, 49, 49, 50]

incs = [-1]*len(cooldowns)

start = timer()

keyboard = Controller()

time.sleep(2)

def runCommand(command):
    for letter in command:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

while True:
    current = timer()
    for i in range(len(cooldowns)):
        if (current-start) // cooldowns[i] > incs[i]:
            incs[i] += 1
            runCommand('pls ' + cmds[i])

time = time.getSeconds()
