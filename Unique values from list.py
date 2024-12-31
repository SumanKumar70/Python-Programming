l1 = [5, 8, 9, 3, 6, 9, 7, 23, 93, 25, 5, 3]
l2 = []

# Loop through each element in l1 and add it to l2 if it's not already present
for item in l1:
    if item not in l2:
        l2.append(item)

# Print the unique values while preserving the order
print("Unique values in l2:", l2)
