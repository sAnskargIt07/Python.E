# Experiment No-4

substring = input("Enter the secret message: ")
string = input("Enter the coded message: ")
if substring in string:
    print("Secret message found in the coded message.")
else:
    print("Secret message not found in the coded message.")