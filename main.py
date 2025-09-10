import subprocess

print("1", "pi")
print("2", "t")

choice = input("Enter choice: ")

if choice == "1":
    subprocess.run(["python", "pi.py"])