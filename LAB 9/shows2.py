# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my second version of the TV show search program. I've improved it by
# adding better formatting for show details. Now when someone searches for a show, they'll see not just
# the name but also when it premiered, ended, and what genres it belongs to. This makes my program
# much more informative and user-friendly. 

import json

"""
New features in this version:
* Formatting the show details
"""

def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    # I'm using the same file loading logic as before - it works well!
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    # My show finding logic remains the same - it's case-insensitive and works well
    for key in shows.keys():
        if query.lower() == key.lower():
            return query
    return None

def get_show_data_by_name(show_name: str, shows: dict) -> dict:
    """
    Return the data for a show based on its name
    """
    # I'm searching through all my shows to find the one with matching name
    for show in shows.keys():
        # I'm doing a case-insensitive comparison here too
        if show_name.lower() == show.lower():
            # Once I find the show, I return all its data
            return shows[show]
        
    # If I can't find the show, I return None
    return None

def format_show_details(show: dict) -> str:
    """
    Format the show details
    """
    # I'm getting all the show details, using '?' as a fallback if something's missing
    show_name = show.get('name', '?')
    premiere_year = show.get('premiered', '?')
    end_year = show.get('ended', '?')
    # I'm joining all genres with commas to make them look nice
    genres = ', '.join(show.get('genres', '?'))

    # I'm creating a nice formatted string with all the show details
    formatted_details = f"{show_name} ({premiere_year} - {end_year}, {genres})"
    return formatted_details

def main():
    """
    Main function 
    """
    # Loading my TV shows data
    shows = load_json("tvshows.json")
    
    # Getting the user's search query
    query = input("Search for a TV show: ")
    
    # Looking for their show
    show_name = find_show(query, shows)
    print(show_name)
    
    # If I found their show, I'll get and display all its details
    if show_name:
        show_data = get_show_data_by_name(show_name, shows)
        formatted_details = format_show_details(show_data)
        print(formatted_details)

# Running my main function
main()