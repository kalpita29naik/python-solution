class Solution(object):
   def checkValid(self, matrix):
        n = len(matrix)
        
        # Check uniqueness in rows
        for i in range(n):
            set1 = set()  # Initialize set1 as an empty set
            for j in range(n):
                element = matrix[i][j]
                set1.add(element)
            if len(set1) != n:
                return False

        # Check uniqueness in columns
        for j in range(n):
            set2 = set()
            for i in range(n):
                element = matrix[i][j]
                set2.add(element)
            if len(set2) != n:
                return False

        return True  # If all rows and columns pass the condition, return True
