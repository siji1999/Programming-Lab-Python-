

row=int(input("\nEnter the no. of steps required: "))
for rows in range(1,row+1):
    for col in range(1,rows+1):
        print(rows*col, end=' ')
    print(" ")
