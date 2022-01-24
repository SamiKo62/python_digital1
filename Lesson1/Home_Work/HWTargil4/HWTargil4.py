#Write a Python program to accept a filename from the user
# and print the extension of that.
# Sample filename : abc.java Output : java
extension=input("Enter file name and extension:")
f=extension.split('.')
print("extension of file is:" + f[-1])






