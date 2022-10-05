invalid_msg = "Oops! Invalid input."

def rgb_hex():
    red = int(input("Enter the value for RED: "))
    if red < 0 or red > 255:
        print(invalid_msg)
        return
    green = int(input("Enter the value for GREEN: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return
    blue = int(input("Enter the value for BLUE: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return
    val = (red << 16) + (green << 8) + blue
    print(str(hex(val)[2:]).upper())

def hex_rgb():
    hex_val = input("Enter a hexadecimal value: ")
    if len(hex_val) != 6:
        print(invalid_msg)
    else:
        hex_val = int(hex_val,16)
        
        two_hex_digits = 2**8
    
        blue = hex_val % two_hex_digits
        hex_val = hex_val >> 8
    
        green = hex_val % two_hex_digits
        hex_val = hex_val >> 8
    
        red = hex_val % two_hex_digits
        hex_val = hex_val >> 8
        print("Red: " + str(red) + " Green: " + str(green) + " Blue: " + str(blue))

def convert():
    while True:
        option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
        if option == "1":
            rgb_hex()
        elif option == "2":
            hex_rgb()
        elif option == "X" or option == "x":
            break
        else:
            print(invalid_msg)

convert()
    