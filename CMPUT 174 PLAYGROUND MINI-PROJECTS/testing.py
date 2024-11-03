# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I created this program to find the longest word in a list of words. 
# It helped me understand functions with return values and list operations.

# My function that finds the longest word in a list
def find_longest_word(words: list):
    # I start with an empty string as my initial longest word
    longest_word = ''
    # I check each word in my list
    for word in words:
        # If the current word is longer than my longest word so far
        if len(word) > len(longest_word):
            # I update my longest word
            longest_word = word
    # After checking all words, I return the longest one
    return longest_word
        
# My main function to test my longest word finder
def main():
    # Creating my test list of words
    words = ['cat', 'tiger']
    # Bug: I forgot to add parentheses to call the function
    longest_word = find_longest_word  # Should be find_longest_word(words)
    print(longest_word)

# I commented out the main guard for testing
#if __name__ == '__main__':
#    main()