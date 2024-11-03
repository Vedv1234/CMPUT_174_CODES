# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I created this program to make Simpsons episode names look nicer! 
# It takes those ugly technical episode codes (like S01_E01_ShowName) and turns them into 
# something that's actually readable. I used string slicing and the find() function to make it work.

# First, I ask the user to give me the episode name in that technical format
OriginalEpisodeFormat = input("Please enter the episode name in the initial format: ")

# I'm using find() to locate all the important parts in the text:
# This finds the first underscore that separates the season number
underscore_index = OriginalEpisodeFormat.find("_")

# Here I'm looking for the second underscore that comes before the episode name
second_underscore_index = OriginalEpisodeFormat.find("_", 4, len(OriginalEpisodeFormat))

# These help me find where the season and episode numbers are
S_index = OriginalEpisodeFormat.find("S")
E_index = OriginalEpisodeFormat.find("E")

# Now I'm slicing up the string to get each part:
# This gets me just the season number
Season = OriginalEpisodeFormat[1:underscore_index]

# This extracts the episode number
Episode = OriginalEpisodeFormat[E_index+1:second_underscore_index]

# And this gives me the actual episode name
EpisodeName = OriginalEpisodeFormat[second_underscore_index+1:len(OriginalEpisodeFormat)]

# Finally, I put it all together in a nice format that humans can actually read!
print(f" Season {Season} , Episode {Episode}: {EpisodeName} (The Simpsons)")