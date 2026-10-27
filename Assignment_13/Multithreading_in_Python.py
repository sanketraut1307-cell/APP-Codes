import threading
import time

# Task 1: Display numbers
def display_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Task 2: Display squares
def display_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)

# Task 3: Display messages
def display_messages():
    messages = ["Hello", "Welcome", "Learn Python"]
    for message in messages:
        print("Message:", message)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=display_numbers)
t2 = threading.Thread(target=display_squares)
t3 = threading.Thread(target=display_messages)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("All tasks completed.")

# Output - 
# Number: 1
# Square of 1 = 1
# Message: Hello
# Number: 2
# Square of 2 = 4
# Message: Welcome
# Number: 3
# Square of 3 = 9
# Message: Learn Python
# Number: 4
# Square of 4 = 16
# Number: 5
# Square of 5 = 25
# All tasks completed.
