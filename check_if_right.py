
class CheckIfRight:
    def __init__(self, level, picture ,arduino_read):
        picture_dictionary={'pic1':['Reader 1: B1 DD 27 83','Reader 2: 93 90 24 83','Reader 3: 51 1E 2A 83'],'pic2':[]}
        is_correct=1
        for i in range (len(arduino_read)):
            if picture_dictionary[i] != arduino_read[i]:
                is_correct = 0
                break
        return is_correct
