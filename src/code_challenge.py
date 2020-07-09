# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# array of arrays, any size inner array
# compare elements in the array for least, and then add the least term to running sum
# 

# We will need: 
# Test array
# running sum
# comparison loop for internal array

test_array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

sum = 0
for inner in test_array:
    least = 500
    print(f'the inner: {inner}')
    for item in inner:
        print(f' the item: {item}')
        if item <= least:
            least = item
            print(f'the least: {least}')
    sum += least
print(sum)


