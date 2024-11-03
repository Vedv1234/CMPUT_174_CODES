# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my container calculator program. It helps me figure out
# how many containers Carol needs for her smoothie by converting between liters and
# cubic centimeters and using the container dimensions.

import math

# Starting with Carol's smoothie volume in liters
carol_smoothie_ltr = 8

# I'm converting liters to cubic centimeters (1L = 1000cm³)
carol_smoothie_cm_cubed = 8/0.001

# Calculating the volume of one container in cubic centimeters
container_volume = 21.3 * 26.7 * 29.7

# I'm using math.ceil to round up - we can't have partial containers!
containers_needed = math.ceil(carol_smoothie_cm_cubed/container_volume)

# Showing my result
print(f"containers needed are {containers_needed}")