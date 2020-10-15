def add_time(start, duration, weekday = None):
    # Split and rename the data:
    # Split time from daytime
    start_split = start.split(" ")
    start_time = start_split[0]
    start_daytime = start_split[1]
    
    # Split time in hours and minutes:
    start_splittime = start_time.split(":")
    start_hour = start_splittime[0]
    start_min = start_splittime[1]
    
    # In case of start hour being 12, to prevent errors, restart the
    # time to 0:
    if int(start_hour) == 12:
        start_hour = int(start_hour) - 12
    
    # Split duration variable in hours and minutes:
    duration_split = duration.split(":")
    duration_hour = duration_split[0]
    duration_min = duration_split[1]
    
    # Calculate the total hour and min:
    calculating_hour = int(start_hour) + int(duration_hour)
    
    calculating_min = int(start_min) + int(duration_min)
    if calculating_min >= 60:
        calculating_min -= 60
        calculating_hour += 1
    
    # If the minutes has only one number, add a 0:
    if calculating_min <= 9:
        calculating_min = "0" + str(calculating_min)
        
    # Add a counter to calculate if it is AM or PM depending
    # on the starting daytime:
    counter = 0
    
    # The counter is triggered whenever it passes more than 12 hours, that is
    # a change between one daytime to another:
    while calculating_hour > 12:
        calculating_hour -= 12
        counter +=1
        
    # Add a new rule to prevent errors when the start hour is 12
    # (didn't detect well changes in daytime):
    if calculating_hour == 12:
        if start_daytime == "AM":
            start_daytime = "PM"
        elif start_daytime == "PM":
            start_daytime = "AM"
            # Add 2 to the counter to count a change of the day, rule 
            # developed in more detail later
            counter +=2
        else:
            return ("Error in daytime input")
    
    # Use counters obtained to check when days have passed:
    # Added a new variable to have a separate counter for the days:
    counter_days = counter
    
    # In case the starting daytime is AM, every 2 counters we return
    # to AM and has passed a day:
    days = 0
    if start_daytime == "AM":
        while counter_days >= 2:
            counter_days -= 2
            days += 1
        # In case the counter is odd, it means that is PM and viceversa:
        if counter % 2 == 0:
            start_daytime = "AM"
        else:
            start_daytime = "PM"
    
    # In case the starting daytime is PM, every 1 counter it has passed
    # to AM, and to count another day we substract 2 to the counter:
    elif start_daytime == "PM":
        while counter_days >= 1:
            counter_days -= 2
            days += 1
        # In case the counter is odd it means that is AM and viceversa:
        if counter % 2 == 0:
            start_daytime = "PM"
        else:
            start_daytime = "AM"
    # We add this in case of error:
    else:
        return("Incorrect input format")
    
    # If it has passed 1 day or more, it returns how many days passed:
    day = ""
    if days == 1:
        day = " (next day)"
    elif days == 0:
        day = ""
    else:
        day = " ({} days later)".format(days)
    
    # If the optional argument is entered, we load a list with the weekdays:
    week_result = ""
    week_result_comma = ""
    if weekday != None:
        list_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # We obtain the index on the list from the input day:
        index = [item.lower() for item in list_week].index(weekday.lower())
        # Add the days passed to the index, if it exceeds the list index, substract
        # a week  (6 days numbers in the list_week because we count from 0)
        total_weekday = index + days
        while total_weekday > 6:
            total_weekday -= 7
        week_result = list_week[total_weekday]
        week_result_comma = ", " + str(week_result)
    
    # We make a variable to return:
    new_time = str(calculating_hour) + ":" + str(calculating_min) + " " + str(start_daytime) + week_result_comma + str(day)
    return new_time
