from collections import Counter
import math


#Receives a string and returns its reverse
#This is the simplest and most basic method. There are many other approaches
def reverse_string(s:str)->str:
    return s[::-1]


#Finds the number that occurs most frequently in the list
def find_most_frequent(numbers:list[int])->int |None:
    if not numbers:
        return None

    counts=Counter(numbers)
    most_common_item=counts.most_common(1)[0]
    return most_common_item[0]    


#Checks if a number is a prime number
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False 
            
    return True 


#Calculates the sum of the main diagonal of a square matrix
def sum_main_diagonal(matrix: list[list[int]]) -> int:
    total = 0
    for i in range(len(matrix)):
        if i < len(matrix[i]): 
            total += matrix[i][i]
    return total


#Sorts the words in a sentence alphabetically
def sort_words_in_sentence(sentence: str) -> str:
    words = sentence.split()
    words.sort() 
    return " ".join(words)



