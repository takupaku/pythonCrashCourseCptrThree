invitation=["makichan","tsuyoshi","atsushi"]

print("Mr. "+invitation[0]+" you are invited to the dinner party")
print("we will be delighted if you, "+invitation[1]+" come to visit our party")
print("At thursday you are invited Mr."+invitation[2]+"\n")

print("alas! mr "+invitation[1]+" can't make in our dinner party"+"\n")

invitation.remove("tsuyoshi")   #removing tsuyoshi
invitation.insert(1,"echizen")  #adding new member

print("At thursday you are invited Mr."+invitation[0])
print("At thursday you are invited Mr."+invitation[1])
print("At thursday you are invited Mr."+invitation[2]+"\n")

print("i've found a bigger table " +invitation[0]+", "+invitation[1]+", "+invitation[2]+"."+"\n")

invitation.insert(0,"kurama")
invitation.insert(1,"toya")
invitation.append("kangkai")
#print(invitation)

print("come Mr "+invitation[0]+" you are invited ")
print("come Mr "+invitation[1]+" you are invited ")
print("come Mr "+invitation[2]+" you are invited ")
print("come Mr "+invitation[3]+" you are invited ")
print("come Mr "+invitation[4]+" you are invited ")
print("come Mr "+invitation[5]+" you are invited ")



