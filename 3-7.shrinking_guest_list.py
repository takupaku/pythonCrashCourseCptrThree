invitation=["makichan","tsuyoshi","touya","kurama","toya","kangkai"]

print("only two people can be invited for the dinner"+"\n")

popped_guest=invitation.pop()
print("sorry, we cant invite you to our dinner "+popped_guest)

popped_guest=invitation.pop()
print("sorry, we cant invite you to our dinner "+popped_guest)

popped_guest=invitation.pop()
print("sorry, we cant invite you to our dinner "+popped_guest)

popped_guest=invitation.pop()
print("sorry, we cant invite you to our dinner "+popped_guest+"\n")

print(invitation[0]+" you are still invited")
print(invitation[1]+" you are still invited")

del invitation[0]
print(invitation)
del invitation[0]
print(invitation)

