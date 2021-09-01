import serial
import serial.tools.list_ports
# ser = serial.Serial('COM5', 9600, timeout=1)



def get_arduino_push_buttons(button,ser):

    if button == 'yes_no':
        print("waiting for yes_no button")
        arduinodata = ser.readlines()  # reads the setup output
        ser.write(b'o')
        arduinodata = ser.readlines()
        print(arduinodata)  #for checks
        answer = arduinodata[-1].decode('utf-8')  #take last print in arduino which is the answer of patient (green/red) and convert is from byte class to string
        if answer =='yes\r\n':
            print("yes button pressed")
        elif answer =='no\r\n':
            print("no button pressed")
    elif button == 'blue':
        print("waiting for blue button")
        arduinodata = ser.readlines()  # reads the setup output
        ser.write(b'p')
        arduinodata = ser.readlines()
        print(arduinodata)  # for checks
        print("blue button pressed")

def get_cup_order_from_arduino (ser):
    print("waiting for cups reading")
    arduinodata = ser.readlines()  # reads the setup output
    ser.write(b'c')
    arduinodata = ser.readlines()
    print(arduinodata)  # for checks
    answer = arduinodata[-1].decode('utf-8')  # take last print in arduino which is the answer of patient (green/red) and convert is from byte class to string
    print(answer)
    print("got arduinodata")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arduino_ports = [p.device for p in serial.tools.list_ports.comports() if 'Arduino' in p.description]
    ser = serial.Serial(arduino_ports[0], 9600, timeout=1)
    # get_arduino_push_buttons('yes_no',ser)
    # get_arduino_push_buttons('blue',ser)
    get_cup_order_from_arduino(ser)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
