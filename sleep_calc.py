import time
from datetime import datetime, timedelta

def calculate_wake_up_times(sleep_time):
    sleep_cycle = timedelta(minutes=90)  # 90 minutes in a timedelta
    print("\nSuggested wake-up times (avoid REM sleep):")
    
    # Loop to calculate wake-up times for 1 to 6 sleep cycles
    for i in range(1, 7):
        wake_up_time = sleep_time + i * sleep_cycle  # Calculate wake-up time
        print(f"{i} cycles: {wake_up_time.strftime('%I:%M %p')}")

def calculate_sleep_times(wake_up_time):
    sleep_cycle = timedelta(minutes=90)  # 90 minutes in a timedelta
    print("\nSuggested sleep times (avoid waking up during REM sleep):")
    
    # Loop to calculate sleep times for 1 to 6 sleep cycles before the desired wake-up time
    for i in range(1, 7):
        sleep_time = wake_up_time - i * sleep_cycle  # Calculate sleep time
        print(f"{i} cycles: {sleep_time.strftime('%I:%M %p')}")

def get_current_time():
    return datetime.now()  # Return the current date and time

def get_user_input_time():
    user_input = input("Enter the time (hh:mm AM/PM): ")
    
    # Convert input to datetime object
    return datetime.strptime(user_input, '%I:%M %p')

def main():
    running = True  # Control variable for program loop
    
    # Main program loop
    while running:
        print("\n--- Sleeping Calculator ---")
        print("1. Enter a sleep time (or use current time)")
        print("2. Enter the time you want to wake up")
        print("Enter -1 to exit.")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            use_current = input("\nWould you like to use the current time? (y/n): ").lower()
            if use_current == 'y':
                sleep_time = get_current_time()  # Use current time
            else:
                sleep_time = get_user_input_time()  # Get user-defined sleep time

            calculate_wake_up_times(sleep_time)  # Calculate wake-up times based on sleep time
        
        elif choice == '2':
            wake_up_time = get_user_input_time()  # Get user-defined wake-up time
            calculate_sleep_times(wake_up_time)  # Calculate sleep times based on wake-up time
        
        elif choice == '-1':
            running = False  # Exit the loop if ESC key is pressed
        
        else:
            print("\nInvalid choice. Please enter 1 or 2.")  # Handle invalid input
    
    print("\nExiting the program...")  # Program exit message

if __name__ == "__main__":
    main()  # Run the main function
