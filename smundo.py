import os
import pickle

# Ask the user if they want to undo the process
response = input("Do you want to undo the process? [y/n]: ")

# Check the user's input and respond
if response.lower() == 'y':
    count, filename = pickle.load(open("counts.pkl", "rb"))
    print("Undoing the process...")
    path = "Data/"+filename
    try:
        os.remove(path)
    # Add code here to undo the process
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    except PermissionError:
        print(f"Permission denied: unable to delete {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    if count > 0:
        count -= 1
    pickle.dump([count, filename], open("counts.pkl", "wb"))
elif response.lower() == 'n':
    print("No action taken.")
else:
    print("Invalid input. Please enter 'y' or 'n'.")
