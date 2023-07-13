import time, os

def convert(t):
    return t * 60

def countdown(t, label):
    # 60
    while t:
        min, sec = divmod(t, 60)
        # t // 60
        print(f"{label}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1) 
        t -= 1
        if label == "Rest" and t == 0 or label == "Work" and t == 0:
            print("Drink some water")
            time.sleep(5)
        
        
#convert min to sec 
def pomodor(work, rest):
    running = True
    while running:
        w = convert(work)
        r = convert(rest)
    
        countdown(w, "Work")
        os.system("clear||cls")
        countdown(r, "Rest")
        os.system("clear||cls")
    

work = int(input("Enter work time (min): "))
rest = int(input("Enter rest time (min): "))


pomodor(work,rest)