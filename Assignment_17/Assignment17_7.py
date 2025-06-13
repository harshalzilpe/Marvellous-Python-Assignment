""" 
    Schedule a function that performs file backup every hour and writes a log entry into backup_log.txt.
"""
import os, time

source_file = 'source.txt'
backup_file = 'backup.txt'
log_file = 'backup_log.txt'
    
def backup_file():
    f1 = open(source_file, 'r')
    data = f1.read()
    f1.close()

    f2 = open(backup_file, 'w')
    f2.write(data)
    f2.close()

    f3 = open(log_file, 'a')
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    f3.write('Backup completed at: ' + timestamp + '\n')
    f3.close()
    
def main():
    while True:
        if os.path.exists(source_file):
            backup_file()
        time.sleep(10)
                
if __name__ == "__main__":
    main()

"""  
   
"""