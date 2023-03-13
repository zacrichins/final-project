import time
import random

# Initialize game variables
start_time = time.time()
escaped = False

# Define game functions
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

