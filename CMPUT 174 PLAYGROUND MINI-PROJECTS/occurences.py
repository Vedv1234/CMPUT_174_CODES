# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my word counter program that reads the Cinderella
# story and counts how many times each word appears. It helps me learn about
# dictionaries and file processing.

''' storing count of items such as count of words from cinderella text file'''

def main():
    # Setting up my dictionary to store word counts
    count_words = {}
    filename = 'cinderella.txt'
    
    # Reading the file and counting words
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            record = line.split()  # Breaking each line into words
            
            for word in record:
                # Converting to lowercase to count same words regardless of case
                word = word.lower()
                
                # This is my clever way to count words using get()
                # If the word is new, it starts at 0 and adds 1
                # If it exists, it adds 1 to the current count
                count_words[word] = count_words.get(word, 0) + 1
                
                # This was my original longer way to do it:
                '''if word not in count_words:
                    count_words[word] = 1
                else:
                    count_words[word] += 1'''
    
    # Showing how many times each word appeared
    for key, value in count_words.items():
        print(f" {key} occurs {value} times.")

if __name__ == '__main__':
    main()