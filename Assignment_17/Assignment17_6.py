""" 
    Write a script that schedules multiple tasks: one to print "Lunch Time!" at 1 PM, and another to print
    "Wrap up work" at 6 PM.
"""
import schedule, time

def lunch_time():
    print("Lunch Time!")

def wrap_up_work():
    print("Wrap up work")
    
def main():
    schedule.every().day.at("13:00").do(lunch_time)
    schedule.every().day.at("18:00").do(wrap_up_work)

    while True:
        schedule.run_pending()
        time.sleep(1)
 
                
if __name__ == "__main__":
    main()

"""  
   
"""