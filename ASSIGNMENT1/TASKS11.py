##using date and time library

from datetime import datetime
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

##using library os
import os
current_directory = os.getcwd()
files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]


