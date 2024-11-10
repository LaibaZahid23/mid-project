# Timezone-Aware Scheduling System
from datetime import datetime
import pytz

# Event scheduled in New York time
first_timezone = pytz.timezone('America/New_york')
first_event = first_timezone.localize\
    (datetime(2024, 8, 22, 15, 0, 0))

# Convert to German time
second_timezone = pytz.timezone('Europe/Berlin')
second_event = first_event.\
    astimezone(second_timezone)

#print(pytz.all_timezones)

# Extract and display location names
# from timezone objects
first_location = first_timezone.zone
second_location = second_timezone.zone

# Display times
print(f"Time at {first_location}:{first_event}")
print(f"Time at{second_location}:{second_event}")
