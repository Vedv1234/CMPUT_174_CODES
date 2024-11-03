# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my final version of the TV show search program, and it's pretty
# awesome! Now users can not only search for shows and see their details, but they can also search
# for specific actors or characters within a show. When they find someone, they'll see detailed info
# about the actor including their birthday and country. I've also added support for identifying if
# they're doing voice acting or regular acting. This is definitely the most comprehensive version
# of my program!

import json

"""
New features in this version:
* Searching for an actor/character in the cast
* Showing detailed information about a selected actor/character
"""

def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    # My JSON loading function - still using it throughout the program
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    # Looking through my shows to find a match
    for key in shows.keys():
        if query.lower() == key.lower():
            return query
    return None

def find_actor(query: str, cast: list[dict]) -> dict:
    """
    Search for an actor in the cast list
    Return the actor's data if found
    If the actor is not found, return None
    """
    # I'm searching through the cast list for matching actor or character names
    for actor in cast:
        # I'm checking both actor and character names to be user-friendly
        if query.lower() in actor['person']['name'].lower() or query.lower() in actor['character']['name'].lower():
            return actor
    return None

def get_show_data_by_name(show_name: str, shows: dict) -> dict:
    """
    Return the data for a show based on its name
    """
    # Looking for my show in the dictionary
    for show in shows.keys():
        if show_name.lower() == show.lower():
            return shows[show]
    return None

def format_show_details(show: dict) -> str:
    """
    Format the show details
    """
    # Getting all my show information with fallback values
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
    # Building my cast file path and loading the data
    filename = f"cast/{show_id}_cast.json"
    return load_json(filename)

def format_cast(cast: list[dict]) -> str:
    """
    Format the cast
    """
    # Creating my formatted cast list with actor and character names
    formatted_cast = "\n".join([f"{actor['person']['name']} as {actor['character']['name']}" for actor in cast])
    return formatted_cast

def format_actor_info(actor_dict: dict) -> str:
    """
    Format the actor's information
    """
    # Getting all my actor details with fallback values
    actor_name = actor_dict['person']['name']
    gender = actor_dict['person'].get('gender', 'Unknown')
    birthday = actor_dict['person'].get('birthday', 'Unknown')
    country = actor_dict['person'].get('country', 'Unknown')
    country_name = actor_dict['person']['country'].get('name', 'Unknown')
    role = actor_dict['voice']
    
    # I'm determining if they're doing voice acting or regular acting
    if role == True:
        output = 'voices'
    else:
        output = 'plays'
    
    # Getting the character name
    character_name = actor_dict['character']['name']
    
    # Creating my detailed actor information string
    formatted_info = f"{actor_name} ({gender}, born {birthday} in {country_name}) {output} {character_name}"
    return formatted_info

def main():
    """
    Main function 
    """
    # Loading my TV shows data
    shows = load_json("tvshows.json")

    # Getting the user's show search
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)

    if show_name:
        # If I found the show, getting its details
        show_data = get_show_data_by_name(show_name, shows)
        formatted_details = format_show_details(show_data)
        print(f"Found: {formatted_details}")

        # Getting and displaying cast information
        show_id = show_data.get('id')
        if show_id:
            cast = get_cast_by_id(show_id)
            print("Cast:")
            formatted_cast = format_cast(cast)
            print(formatted_cast)
            
            # Now letting the user search for an actor or character
            actor_query = input("Enter an actor or character: ")
            actor_info = find_actor(actor_query, cast)

            # If I found their search, showing the detailed information
            if actor_info:
                formatted_actor_info = format_actor_info(actor_info)
                print(f"Found: {formatted_actor_info}")
            else:
                print("Can't find this actor or character in the cast!")
        else:
            print("Cast details not available.")
    else:
        print("Can't find this TV show in the Top 100!")

# Running my program
if __name__ == '__main__':
    main()