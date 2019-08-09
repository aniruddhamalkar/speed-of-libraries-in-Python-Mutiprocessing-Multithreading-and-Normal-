import time
start_time4 = time.time()
def num_calc(number1, number2):
    start_time1 = time.time()

    for no1 in range(1, number1):
        for no2 in range(1, number2):
            print("{} multiplied by {} is {}".format(no1, no2, no1*no2))
        print("=" * 30)
    elasped_time1 = time.time() - start_time1
    print("The elapsed time for num_cal is {} ".format(elasped_time1))

def no_square(number):
    start_time2 = time.time()
    for no in range(0, number):
        print("Number {} square is {}".format(no, no**2))
    print(" " * 30)
    elasped_time2 = time.time() - start_time2
    print("The elapsed time for no_square is {} ".format(elasped_time2))

def no_qube(number):
    start_time3 = time.time()
    for no in range(0, number):
        print("Number {} qube is {}".format(no, no**3))
    print(" " * 30)
    elasped_time3 = time.time() - start_time3
    print("The elapsed time for no_qube is {} ".format(elasped_time3))
my_number1 = int(input("Please enter the number1: "))
my_number2 = int(input("Please enter the number2: "))
num_calc(my_number1, my_number2)
no_square(my_number1)
no_qube(my_number1)
elasped_time4 = time.time() - start_time4
print("The elapsed time is {} ".format(elasped_time4))
