'''
Q: Write a Python class to find a pair of elements (indices of the two numbers)
    from a given array whose sum equals a specific target number.
'''

class pair:
    def __init__(self,array,target):
        self.array=array
        self.target=target
    
    def find_pair(self):
        for i in range(len(self.array)):
            for j in range(i+1, len(self.array)):
                if self.array[i] + self.array[j] == self.target:
                    print("The indices' value that make up to target are ", i, j)

object=pair([10,20,8,9,15,5],25)
object.find_pair()