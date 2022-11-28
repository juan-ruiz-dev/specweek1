### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['chuck palahniuk', "orsen wells", "mark twain"]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append("Andy Weir")

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_authors.remove("chuck palahniuk")

# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
my_authors[0]

# Now slice the list.

# Code here
# Example: my_authors[1:4]
my_authors[1:1]

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.
my_author_tuple = ("chuck palahniuk", "orsen wells", "mark twain")
# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.
my_author_set = {"chuck palahniuk", "orsen wells", "mark twain"}
 
# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
my_author_set.add("Andy Weir")

# Try adding the same author again, and be sure to print your set.
my_author_set.add("Andy Weir")
print(my_author_set)
# Code here
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)
for book in my_authors:
    print(book)
# for book in my_authors_tuple:
    # print(book)
for book in my_author_tuple:
    print(book)
# for book in my_authors_set:
    # print(book)
for book in my_author_set:
    print(book)
