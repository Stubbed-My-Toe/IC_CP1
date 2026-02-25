#IC 1st CP2 time handling for word counter.

import time

def show_time():
    curr = time.ctime(time.time())
    print("last updated", curr)