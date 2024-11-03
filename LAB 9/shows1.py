# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my first version of the TV show search program. I created this to help
# users search through a JSON file containing TV show data. It's pretty basic right now - it just lets
# you search for a show by name and tells you if it's in the database or not. I'm building this as part
# of my CMPUT 174 course to learn how to work with JSON data and implement search functionality.

# I'm importing the json module here because I need it to read my JSON file
import json 

def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    # I'm opening my file in read mode using a with statement for better file handling
    with open(filename, 'r') as file:
        # Here I'm converting my JSON file from string format to a Python dictionary
        data = json.load(file)
    
    # I'm sending back the dictionary containing all my TV show data
    return data

def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    # I'm looking through each show name in my dictionary
    for key in shows.keys():
        # I'm comparing the show names case-insensitively to make the search more user-friendly
        if query.lower() == key.lower():
            # If I find a match, I return the show name the user searched for
            return query
    
    # If I couldn't find the show, I return None to indicate no matches
    return None

def main():
    """
    Main function 
    """
    # First, I'm loading all my TV show data from the JSON file
    shows = load_json("tvshows.json")
    # I'm asking the user what show they want to search for
    query = input("Search for a TV show: ")
    # I'm using my find_show function to look for the show they want
    show_name = find_show(query, shows)
    # If I found their show, I'll tell them
    if show_name:
        print(f"Found: {show_name}")
    # If I couldn't find it, I'll let them know it's not in the top 100
    else:
        print("Can't find this TV show in the Top 100!")

# This is my standard way to run the program - it calls my main function when the script is run directly
if __name__ == '__main__':
    main()