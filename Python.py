class MultiplyTable():
    description="Generates Multiplication table"
    def table(n):
        for i in range(2,n+1): # For every number between 2 and n
            print("\nMultiplication table for %d\n"%i)
            for j in range(1,11):
                print("%d x %d = %d"%(i,j,i*j))

val=int(input("Enter the value for the table :"))

print(" ------------------------ ")
print("|  Multiplication Table  |")
print(" ------------------------ ")

MultiplyTable.table(val)