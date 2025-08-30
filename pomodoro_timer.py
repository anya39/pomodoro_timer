#Import libraries
import time 
import os
import random
from colorama import Fore, Style, init

init(autoreset=True) #Resets color after each print

#Sets up long break celebration and themes
def celebrate(theme):
    if theme == 1:
        emojis = ["🎉", "🎊", "🥳"]
    elif theme == 2:
        emojis = ["🎈"]
    elif theme == 3:
        emojis = ["⭐", "🌟", "✨"]
    elif theme == 4:
        emojis = ["🔥", "💥"]
    elif theme == 5:
        emojis = ["❤️", "💖", "💕", "🧡", "💛",]
    else:
        emojis = ["🎉", "🎊", "🥳", "🎈", "⭐", "🌟", "✨", "🔥", "💥", "💫"]
    
    for _ in range(2): #Number of confetti lines
        line = ""
        for _ in range(7): #Number of emojis per line
            line += random.choice(emojis)
            print(line)
            time.sleep(0.1)

#For clearing screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

#Statistics tracking
pomodoro_count = 0
total_work_time = 0
short_break_count = 0
long_break_count = 0

#Countdown function displaying remaining time
def countdown(seconds, session_type):
    #Color coding for type of session
    if session_type == "Work":
        color = Fore.RED
    elif session_type == "Break":
        color = Fore.GREEN
    elif session_type == "Long Break":
        color = Fore.BLUE
    else:
        color = Fore.WHITE

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        #Formats time as mm:ss
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"{color}{session_type} Time Remaining: {timeformat} ", end = '\r')
        time.sleep(1)
        seconds -= 1
    print(f"{color}{session_type} session ended!\n")
    #Play sound at end of session (only works on Mac)
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    

#Ask user for duration of work session
work_duration = int(input("\nEnter work duration in minutes: ")) * 60
#Ask user for duration of break session
break_duration = int(input("Enter break duration in minutes: ")) * 60
#Ask user for duration of long break session
long_break_duration = int(input("Enter long break (achieved after 4 work sessions) duration in minutes: ")) * 60
#Ask user for celebration theme preference
theme = int(input("\nChoose an emoji celebration theme for long breaks\n(1: Confetti, 2: Balloons, 3: Stars, 4: Fire, 5: Hearts, 6: Random)\nEnter #: "))


#Main while loop to alternate between work and break sessions
while True:
    #Start Pomodoro timer
    print("\n\nStarting Pomodoro Timer...\n")

    time.sleep(1.5)

    #Starts work session
    print("Work session started!\n")
    countdown(work_duration, "Work")
    total_work_time += work_duration // 60 #Updates work time stats in mins
    
    #Update pomodoro count
    pomodoro_count += 1
    
    #Decide which type of break to take
    if pomodoro_count % 4 == 0:
        #Clear screen between sessions
        clear_screen()
        print(f"✅ {pomodoro_count} Pomodoros completed! You finished a full set, it's time for a longer break! 🌴\n")
        celebrate(theme) #Calls emoji celebration function
        countdown(long_break_duration, "Long Break")
        long_break_count += 1
    else:
        #Clear screen between sessions
        clear_screen()
        #Starts standard break session
        print("Break session started!\n")
        countdown(break_duration, "Break")
        short_break_count += 1
    
    #Update and display pomodoro count
    if pomodoro_count == 1:
        print("1 Pomodoro session completed! Great start! 🚀 \n")
    elif pomodoro_count == 2:
        print("2 Pomodoro sessions completed! Keep it up! 💪 \n")
    elif pomodoro_count == 3:
        print("3 Pomodoro sessions completed! Almost a full set! 🎯 \n")
    else:
        print(f"{pomodoro_count} Pomodoro sessions completed! 🙌\n")

    #Asks user if want to repeat cycle (loop)
    repeat = input("Do you want to start another Pomodoro cycle? (y/n): ").lower()
    if repeat != 'y':
        print("\nPomodoro session ended. Good job!\n\n")
        time.sleep(2)
        print("📊 Session Statistics Summary:\n")
        print(f"Total Pomodoro sessions Completed: {pomodoro_count}")
        time.sleep(1)
        print(f"Total Work Time: {total_work_time} minutes")
        time.sleep(1)
        print(f"Total Short Breaks Taken: {short_break_count}")
        time.sleep(1)
        print(f"Total Long Breaks Taken: {long_break_count}\n\n\n")
        break #Ends the while loop