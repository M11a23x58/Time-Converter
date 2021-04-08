print("This program will convert seconds to hours, minutes and seconds.")

def main():
# input time
    time = int(input("Please input the seconds.\n"))

# converter
    Second = time % 60
    Minute = ((time - Second) / 60 ) % 60
    Hour = ((time - Second) / 60 ) / 60

# output time format
    h = "%02d" % Hour
    m = "%02d" % Minute
    s = "%02d" % Second
    print(h,":",m,":",s)

# exception detect
while True:
    try:
        main()
    except ValueError:
        print("Wrong input, try again.\n")

