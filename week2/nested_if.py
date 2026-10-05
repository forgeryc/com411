hos = int(input("Is the book 1. Hard or 2. Soft? Input 1 or 2"))
if hos == 2:
    bound = int(input("Is the book soft bound? 1 for yes 2 for no"))
    if bound == 1:
        print("Soft cover, perfect bound books are very popular!")
    else:
         print("Soft covers with coils or stitches are great for short books")

else:
    print("Books with hard covers can be more expensive!")