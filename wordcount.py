print("Please enter the matrix in followng style: ")
print("a b c;d e f")
matrix = input()
mat=[]
# split the matrix in rows
matr = matrix.split(";")
#print (matr)
row = 0
row = matr.__len__()
# Split the matrix in colomns
col = matr[0].split(' ').__len__()
mat =[]
mdel=[]
k = 0

#print(row, col)

#left i,j = i, j-1
# right i , j = i , j+1
# up i , j = i-1 , j
#down i,j = i+1, j
i=0
j=0
# Definition of the SearchWord
print("Please enter the word that you want to search: ")
word = input()
word = list(word)
#print(word.__len__())
flag = False
#print(matr.__len__())

for i in range(matr.__len__()):

    j=0
    for j in range (matr[0].split(" ").__len__()):

        if (word[0] == matr[i][2*j]):
            starti = i
            sti = i
            startj = j
            stj = j
            beforei = starti
            beforej = 2*startj
 #           print(starti, startj)
            matr2 = matr
            for k in range(word.__len__()-1):
#               check the left side of the element
                if (startj!= 0 and (k!=0) and word[k+1] == matr2[starti][2*(startj-1)] and beforej != 2*(startj-1)):

                        beforej= startj
                        startj = 2*(startj-1)
                        flag=True
#               check the right side of the first colomn's elements
                elif (startj!= col-1 and startj == 0 and word[k+1] == matr2[starti][2*(startj+1)] and beforej != 2*(startj+1)):

                        beforej = startj
                        startj = (startj+1)
                        flag=True
#               check the right side of the element
                elif (startj!= col-1 and startj != 0 and word[k+1] == matr2[starti][2*(startj)+2] and beforej != 2*(startj)+2):

                        beforej = startj
                        startj = 2*(startj)
                        flag=True
#               check the down side of the element
                elif (starti!= row-1 and word[k+1] == matr2[starti+1][2*(startj)] and beforei != starti+1):

                        beforei = starti
                        starti = starti+1
                        flag=True
#               check the up side of the element
                elif (starti !=0 and word[k+1] == matr2[starti-1][2*(startj)] and beforei != starti-1):

                        beforei = starti
                        starti = starti-1
                        flag=True
#               check the integrity of the program
                elif(2*startj> col and startj %2==0): startj = int (startj/2)

                elif ( k+1 == word.__len__()-1 and flag): break
                else:
                    flag = False
            if (k + 1 == word.__len__() - 1 and flag): break

print(flag)










































#Nazanin Bayati

