import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_characters():
    for i in ['A', 'B', 'C', 'D', 'E']:
        print(i)
        time.sleep(2)

#print_numbers()
#print_characters()

thread1 = threading.Thread(target=print_numbers)   # Threading is a module.. and Thread is a class
thread2 = threading.Thread(target=print_characters)
thread1.start() # start() It is method..
thread2.start()

thread1.join() # join() it is also method
thread2.join()


#print("All thread Executed")

print(f"Is Thread1 alive? {thread1.is_alive()}")
print('All thread Executed')