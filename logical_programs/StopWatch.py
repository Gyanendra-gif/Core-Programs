'''
@Author: Gyanendra
@Date: 31/12/2021 
@Last Modified by: Gyanendra
@Last Modified time: 03/01/2021 
@Title : Gyanendra
'''

import time

try:
    def fuction_inputString(string):
        while True:
            try:
                return input(string)
            except Exception as e:
                print(e)             

    def function_startStopWatch():
        while True:                  
            choice = 'Enter start to Begin StopWatch: '
            if fuction_inputString(choice) == 'start':
                return round(time.time(), 2)                
            else:
                print('Provide Correct Input to Start Watch')                

    def function_stopStopWatch(): 
        while True:            
            choice = 'Enter stop to End StopWatch: '
            if fuction_inputString(choice) == 'stop':
                return round(time.time(), 2)               
            else:
                print('Provide Corrrect input to Stop Watch')
                

    if __name__ == '__main__':
        startTime = function_startStopWatch()
        stopTime = function_stopStopWatch()

        print('Here the Time Escalped is: ', round(startTime-stopTime,2), 'second' ) 

except Exception as e:
    print(e)
