# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my third version of the TV show search program. I've made it even
# better by adding cast information! Now users can see not just show details but also all the actors
# and their character names. I'm pretty proud of how this is coming along - it's becoming a really
# useful tool for finding information about TV shows.

import json

"""
New features in this version:
* Showing all actors in the show and their roles
"""

def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    # My trusty JSON loading function - still working great!
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    # My show finding logic is still solid - keeping it the same
    for key in shows.keys():
        if query.lower() == key.lower():
            return query
    return None

def get_show_data_by_name(show_name: str, shows: dict) -> dict:
    """
    Return the data for a show based on its name
    """
    # Looking through my shows to find a match
    for show in shows.keys():
        if show_name.lower() == show.lower():
            return shows[show]
        
    return None

def format_show_details(show: dict) -> str:
    """
    Format the show details
    """
    # Getting all my show details with fallback values
    show_name = show.get('name', '?')
    premiere_year = show.get('premiered', '?')
    end_year = show.get('ended', '?')
    genres = ', '.join(show.get('genres', '?'))

    # Creating my formatted string
    formatted_details = f"{show_name} ({premiere_year} - {end_year}, {genres})"
    return formatted_details

def get_cast_by_id(show_id: int) -> list[dict]:
    """
    Get the cast for a show
    """
    # I'm constructing the filename for the cast JSON file using the show's ID
    filename = f"cast/{show_id}_cast.json"
    # Loading and returning the cast data
    return load_json(filename)

def format_cast(cast: list[dict]) -> str:
    """
    Format the cast
    """
    # I'm creating a nicely formatted string with each actor and their character
    formatted_cast = "\n".join([f"{actor['person']['name']} as {actor['character']['name']}" for actor in cast])
    return formatted_cast

def main():
    """
    Main function 
    """
    # Loading my shows data
    shows = load_json("tvshows.json")

    # Getting user's search query
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)

    if show_name:
        # If I found the show, I'll get its details
        show_data = get_show_data_by_name(show_name, shows)
        formatted_details = format_show_details(show_data)
        print(f"Found: {formatted_details}")

        # Now I'll try to get and display the cast information
        show_id = show_data.get('id')
        if show_id:
            cast = get_cast_by_id(show_id)
            print("Cast:")
            formatted_cast = format_cast(cast)
            print(formatted_cast)
        else:
            print("Cast details not available.")
    else:
        print("Can't find this TV show in the Top 100!")

# Running my program
if __name__ == '__main__':
    main()