import serial
import serial.tools.list_ports #pip install pyserial
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

def get_cup_order_from_arduino (ser,level):
    print("waiting for cups reading")
    arduinodata = ser.readlines()  # reads the setup output
    ser.write(b'c')
    arduinodata = ser.readlines()
    # print(arduinodata)  # for checks
    i=1
    number_of_cups=0
    if level==1:
        number_of_cups=3
    elif level==2:
        number_of_cups = 4
    elif level == 3:
        number_of_cups = 5
    elif level == 4:
        number_of_cups = 6
    elif level == 5:
        number_of_cups = 7
    cups_reading=[0,0,0,0,0,0,0]
    cups_count=0 ## the number of cups that had been read

    while arduinodata[-i].decode('utf-8') != 'in cups_order_Read functiopn\r\n' and i<=number_of_cups:
       # print (arduinodata[-i].decode('utf-8'))
       cups_reading[-i] = arduinodata[-i].decode('utf-8')  # take last print in arduino which is the answer of patient (green/red) and convert is from byte class to string
       i=i+1
       cups_count=cups_count+1
    ### make cups_reading looks cleaner
    clean_cups_reading=cups_reading[7-cups_count:]
    j=0
    for j in range(len(clean_cups_reading)):
        clean_cups_reading[j]=removetresh(clean_cups_reading[j])

    # answer = arduinodata[-1].decode('utf-8')  # take last print in arduino which is the answer of patient (green/red) and convert is from byte class to string
    # print(answer)
    print (clean_cups_reading)
    print("got arduinodata")
    return clean_cups_reading

def removetresh (cup_read):
    cup_to_parts=cup_read.split(':')
    new_first_step=cup_to_parts[0]+':'+cup_to_parts[2] ## remove 'Card UDI' part
    new_first_step_to_parts = new_first_step.split('\r')
    new_second_step = new_first_step_to_parts[0]  ## remove '\r\n' part
    return new_second_step

def is_correct_order (self,ser,level,picture): ## comper between picture and arduino read
    arduino_read=get_cup_order_from_arduino (ser,level)
    picture_dictionary={'pic1':['Reader 1: B1 DD 27 83','Reader 2: 93 90 24 83','Reader 3: 51 1E 2A 83'],'pic2':[]}
    is_correct=1
    for i in range (len(arduino_read)):
        if picture_dictionary.get(picture)[i] != arduino_read[i]:
            is_correct = 0
            break
    return is_correct

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arduino_ports = [p.device for p in serial.tools.list_ports.comports() if 'Arduino' in p.description]
    ser = serial.Serial(arduino_ports[0], 9600, timeout=1)
    # get_arduino_push_buttons('yes_no',ser)
    # get_arduino_push_buttons('blue',ser)
    get_cup_order_from_arduino(ser,4) ## level1=3 cups, level2=4 cups, level3=5 cups, level4=6 cups, level5=7 cups
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
