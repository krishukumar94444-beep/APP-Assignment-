import threading
import time

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# Task 1: Calculate the sum of numbers
def calculate_sum():
    print("Thread 1: Calculating sum...")
    time.sleep(1)
    total = sum(numbers)
    print(f"Thread 1: Sum = {total}")


# Task 2: Find even numbers
def find_even():
    print("Thread 2: Finding even numbers...")
    time.sleep(1)
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Thread 2: Even Numbers = {even_numbers}")


# Task 3: Find odd numbers
def find_odd():
    print("Thread 3: Finding odd numbers...")
    time.sleep(1)
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print(f"Thread 3: Odd Numbers = {odd_numbers}")


# Task 4: Calculate squares
def calculate_squares():
    print("Thread 4: Calculating squares...")
    time.sleep(1)
    squares = [num ** 2 for num in numbers]
    print(f"Thread 4: Squares = {squares}")


# Creating multiple threads
t1 = threading.Thread(target=calculate_sum)
t2 = threading.Thread(target=find_even)
t3 = threading.Thread(target=find_odd)
t4 = threading.Thread(target=calculate_squares)

# Starting all threads
print("Main Thread: Starting multiple threads...\n")

t1.start()
t2.start()
t3.start()
t4.start()

# Waiting for all threads to finish
t1.join()
t2.join()
t3.join()
t4.join()
Comment :- 
Main Thread: Starting multiple threads...

Thread 1: Calculating sum...
Thread 2: Finding even numbers...
Thread 3: Finding odd numbers...
Thread 4: Calculating squares...
Thread 1: Sum = 550
Thread 2: Even Numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Thread 3: Odd Numbers = []
Thread 4: Squares = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000]

Main Thread: All tasks completed successfully!
print("\nMain Thread: All tasks completed successfully!")
