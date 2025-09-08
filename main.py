from solutions import (
    reverse_string, 
    find_most_frequent, 
    is_prime, 
    sum_main_diagonal, 
    sort_words_in_sentence
)

def main():
    print("Fanap Internship Challenge")

    #Question 1: Reversing a String
    input_str = "hello"
    reversed_str = reverse_string(input_str)
    print(f"Question 1 | Input: '{input_str}', Reversed Output: '{reversed_str}'")


    #Question 2: Most Frequent Number
    numbers = [1, 2, 2, 3, 3, 3, 4]
    most_frequent = find_most_frequent(numbers)
    print(f"Question 2 | Input: {numbers}, Most Frequent Number: {most_frequent}")


    #Question 3 :Prime Number Check
    prime_candidate = 7
    is_p = is_prime(prime_candidate)
    print(f"Question 3 | Input: {prime_candidate}, Is Prime? {is_p}")

    prime_candidate_2 = 10
    is_p_2 = is_prime(prime_candidate_2)
    print(f"Question 3 | Input: {prime_candidate_2}, Is Prime? {is_p_2}")


    #Questuin 4 :Sum of Matrix Diagonal
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diagonal_sum = sum_main_diagonal(matrix)
    print(f"Question 4 | Input: {matrix}, Diagonal Sum: {diagonal_sum}")



    #Question 5 : Sort Words in a Sentence
    sentence = "backend engineering is horrible"
    sorted_sentence = sort_words_in_sentence(sentence)
    print(f"Question 5 | Input: '{sentence}', Sorted: '{sorted_sentence}'")



    
if __name__ == "__main__":
    main()