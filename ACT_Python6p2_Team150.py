# Activity Python 3: Task 2
# File: ACT_Python_HeaderTemplate_Team150_maarabrn.py 
# Date:    1 24 2024
# By:      Rania Maaraba
# Section: 09
# Team:    150
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# 

snowList = open('Snow_Fall.txt', 'r')
percentage = open('percentage.txt' , 'r')

List = snowList.readlines()

for i in range(len(List)):
    List[i] = str(List[i])

MS = []
D = []
T = []

for i in range(len(List)):
    snowL = List[i].split()
    T.append(str(snowL[0]))
    D.appen(str(snowL[1]))
    MS.append(D[i] + T[i])
    print(max(snowL))
