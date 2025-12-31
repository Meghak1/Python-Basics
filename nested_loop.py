#basic code 
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0: print("Weird")
    elif n in range(2,6) and n%2==0: print("Not Weird")
    elif n in range(6,21) and n%2==0: print("Weird")
    elif n%2==0 and n>20 : print("Not Weird")


#more better

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0: #why to check again and again for even number condition
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

#most Better

print("Weird" if n % 2 == 1 or 6 <= n <= 20 else "Not Weird")

