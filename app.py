# Define the tasks as functions that return True upon success
def task1():
    print("Line 1")
    return True

def task2():
    print("Feature branch change")
    return True

# Execute the conditional check
if task1() and task2():
    print("Yes")
else:
    print("No")

