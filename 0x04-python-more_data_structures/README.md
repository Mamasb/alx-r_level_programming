# 0x04 Python - Data Structures : Set , Dictionary

![data_structure_in_python](https://www.google.com/url?sa=i&url=https%3A%2F%2Fbdtechtalks.com%2F2022%2F12%2F30%2Fdata-structures-the-fun-way%2F&psig=AOvVaw0nw4KZrEdEGIpQhBTI8EFg&ust=1699681040145000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOiGm7jbuIIDFQAAAAAdAAAAABAJ)

## General

- Why Python programming is awesome
- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the map, reduce and filter functions

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3 (version 3.8.5)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle (version 2.8.*)`
- All your files must be executable
- The length of your files will be tested using `wc`

## 0. Squared simple
## Write a function that computes the square value of all integers of a matrix.
(https://www.google.com/imgres?imgurl=https%3A%2F%2Fi1.wp.com%2Fyutsumura.com%2Fwp-content%2Fuploads%2F2017%2F07%2Fsquareroot-of-matrix.jpg%3Fresize%3D720%252C340%26ssl%3D1&tbnid=mQYYTBLftHcm4M&vet=12ahUKEwjRtsCI3LiCAxXXmicCHTGlAXEQMygUegQIARB5..i&imgrefurl=https%3A%2F%2Fyutsumura.com%2Fnoinfinitely-many-square-roots-of-2-by-2-matrices%2F&docid=3l7cTgWAi2CN8M&w=720&h=340&q=function%20that%20computes%20the%20square%20value%20of%20all%20integers%20of%20a%20matrix&ved=2ahUKEwjRtsCI3LiCAxXXmicCHTGlAXEQMygUegQIARB5)

- Prototype: def square_matrix_simple(matrix=[]):
- matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc
