#import time runs clock
import time

seconds = 0
minute = 0
hour = 0
#select options
#press 1 for millitart etc.
def engine():

    global seconds
    global minute
    global hour
    
    x =eval(input('[1]millitary, or [2]12 hour?:'))
#anti break
    if x > 2:
        print('invalid input')
        print('select option 1 or 2')
        engine()

    #runs on millitary time, if using 12 hour, it will convert
    print('please enter time in millitary format')
 
    print('if you are using 12 hour format, it will be converted automatically')
    seconds = 0
    minute = eval(input('minute:'))
    hour = eval(input('hour:'))
    #millitary time
    if x == 1:
        def clock():
            r = 1
            while r == 1:
                global seconds
                global minute
                global hour
                time.sleep(1)
                seconds = seconds + 1
                if seconds == 60:
                    seconds = 0
                    minute =minute + 1
                if minute == 60:
                    minute = 0
                    hour = hour + 1
                                
                if hour == 19:
                        minute = minute - 30
                if hour == 21:
                        minute = minute + 30

                for i in range(50):        
                    print()

                print(hour,'h',minute ,'m',seconds,'s')
        clock()
    #12 hour time
    if x == 2:
        def clock():
            r = 1
            global minute
            global seconds
            global hour
#if it is past 12 it shall convert first
            if hour > 12:
                hour = hour - 12
                for i in range(50):        
                    print()
                    
                print(hour,':',minute,'am')
            if hour > 12:
                for i in range(50):        
                    print()
                    
                    print(hour,':',minute,'pm')
            while r == 1:
                time.sleep(1)
                seconds = seconds + 1
                if seconds == 60:
                    seconds = 0
                    minute =minute + 1
                    if hour < 12:
                        for i in range(50):        
                            print()
                            
                        print(hour,':',minute,'pm')
                    if hour > 12:
                        for i in range(50):    
                            print()
                        
                        hour = hour - 12
                        print(hour,':',minute,'am')
                if minute == 60:
                    minute = 0
                    hour = hour + 1
                                
                if hour == 19:
                        minute = minute - 30
                if hour == 21:
                        minute = minute + 30

    #----------------------------
                        
        clock()
 
engine()

            
             
