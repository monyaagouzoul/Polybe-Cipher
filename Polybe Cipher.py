"""POLYBE CIPHER :  *Polybius  A Tool for Polybe decoder / encoder automatically. The square of polybe (5*5)..This system of encryption can be coupled with a password that is a messy alphabet to fill the grid """
motcle=input("saisir votre chaine:\n")
alpha="ABCDEFGHIJKLMNOPQRSTUVXYZ"
mat=[[0]*5 for _ in range(5)]
mat[0][0]=motcle[0]
i=0
j=1
for pos in range(1,len(motcle)):
  if j==5:
      i+=1
      j=0
  if motcle[pos] not in motcle[:pos]:
     mat[i][j]=motcle[pos]
     j+=1
for pos in range (len(alpha)):
   if j==5:
      i+=1
      j=0
   if alpha[pos] not in motcle :
       mat[i][j]=alpha[pos]
       j+=1
print(mat)
""" CRYPTAGE"""
msg=input("saisir votre message\n !")
mat==motcle
res=""
for pos in range(len(msg)):
   if msg[pos]=="":
      res+="_"
   elif msg[pos]=="W":
      res+="00"
   else :
      i=0
      j=0
      while mat[i][j]!=msg[pos]:
       j+=1
       if j==5:
          j=0
          i+=1
       res+=str(i+1)+str(j+1)
print("le cryptage de cette chaine est:",res)
"""DECRYPTAGE"""
mat==motcle
res=""
k=0
while k<len(msg)-1:
  s=msg[k]
  if msg[k]=="_":
     res+=""
     k+=1
  elif msg[k]=="0":
     res+="W"
     k+=2
  else:
   i=int(msg[k])-1
   j=int(msg[k+1])-1
   res+=mat[i][j]
   k+=2
print("le decryptage de ce cle est:",res)
"""Coded by Monya agouzoul"""
