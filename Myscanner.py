import sys
import socket
from datetime import datetime


# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()


print("~!" * 50)
print("Welecome In My Port Scanner By S4L1M Learned From The Cyber Mentor " )
print("##" * 50)
print("Scanning Target: " + target)
print("Time started: " + str(datetime.now()))
print("##" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    print("##" * 50)
    print("Time Finish: " + str(datetime.now()))   
    print("~!" * 50)   

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()


except socket.gaierror : 
     print("\n could not analyse this domain .")
     sys.exit()
     
except socket.error : 
     print("\n could not analyse this domain .")
     sys.exit()