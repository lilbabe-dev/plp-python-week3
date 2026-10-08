count = 1
total = 0

#Bug: Full colon was missing, so I fixed it by add colon to form a block
#Bug: equal sign was missing I fixed it by adding <= to make the equation true
while count <= 5: 
    total = total + count
    count = count + 1

# Bug: typeError, can only concatenate str (not "int") to str. I fixed this by using coma
print("Sum of 1 to 5 is: ", total)