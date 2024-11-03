# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This looks like a simplified version of my fishing program
# but it has some bugs I need to fix in the catch counting and variable names.

# Setting up my fishing limits
required = 5        # Number of trouts I need
catchlimit = 7      # Maximum fish I can catch
releaselimit = 3    # Maximum fish I can release

# Initializing my counters
catch = 0    # Total catches
release = 0  # Total releases
t = 0        # Trout count

# Main fishing loop
while catch < catchlimit and t < required:
    catch = input(' t y/n?')    # Bug: I shouldn't reassign catch variable here
    if catch == 'y':            # If it's a trout
        t = t + 1               # Increment trout count
        catch + catch + 1       # Bug: This line doesn't actually add to catch

    else:                       # If it's not a trout
        if release < releaselimit:  # If I can still release
            print('released')
            release = release + 1

        else:                   # If I can't release anymore
            catch = catch + 1   # Add to catch count

    # Printing my current status
    print(f" {t} t so far")
    print(f" {catch} catch so far")
    print(f" {releases} releases so far")  # Bug: 'releases' variable doesn't exist

# Deciding what to cook
if t == required:
    print("cake")
else:
    print("medley")