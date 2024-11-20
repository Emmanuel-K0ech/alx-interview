# 0x07. Rotate 2D Matrix

## Description
For the **“0. Rotate 2D Matrix”** project, you are tasked with implementing an **in-place algorithm** to rotate an `n x n` 2D matrix by **90 degrees clockwise**. This challenge requires a strong understanding of matrix manipulation and in-place operations in Python.

---

## Concepts Needed

### Matrix Representation in Python
- Understanding how 2D matrices are represented using **lists of lists** in Python.
- Accessing and modifying elements in a 2D matrix.

### In-place Operations
- Performing operations directly on the data without creating a copy of the data structure.
- Minimizing space complexity by modifying the matrix in place.

### Matrix Transposition
- Understanding the concept of **transposing a matrix** (swapping rows and columns).
- Implementing matrix transposition as a key step in the rotation process.

### Reversing Rows in a Matrix
- Manipulating rows of a matrix by reversing their order as part of the rotation process.

### Nested Loops
- Using nested loops to iterate through 2D data structures like matrices.
- Modifying elements within nested loops to achieve the desired rotation.

---

## Resources

### Python Official Documentation
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (list comprehensions, nested list comprehension)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### GeeksforGeeks Articles
- [In-place Rotate Square Matrix by 90 Degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a Matrix in Single Line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.

---

## Approach
By understanding these concepts and utilizing the provided resources, you can approach the problem methodically:
1. **Transpose the Matrix:** Swap rows and columns.
2. **Reverse Each Row:** Reverse the elements in each row of the matrix.

This project tests your ability to manipulate 2D matrices while challenging you to optimize your solution to operate in-place, enhancing problem-solving and algorithmic thinking in Python.

---

## Additional Resources
- [Mock Technical Interview](https://www.mocktechnicalinterview.com)

---

## Requirements

### General
- **Allowed editors:** `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3 (version `3.8.10`).
- All files should end with a **new line**.
- The first line of all files should be exactly:  
  `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is **mandatory**.
- Code must follow the **pycodestyle** style (version `2.8.0`).
- **No module imports** are allowed.
- All modules and functions must be documented.
- All files must be executable.

