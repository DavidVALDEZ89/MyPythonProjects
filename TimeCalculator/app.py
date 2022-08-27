def add_time(start, duration,*week_day):
    
    # SEPARATE START
    num_start= start.split()[0]
        
    # TRANSFORM START INTO INTO MINUTES? AM/PM
    if start.split()[1] == "AM":
        start_ttl = (int(num_start.split(":")[0])*60) + int(num_start.split(":")[1])        
    else :
        start_ttl = (int(num_start.split(":")[0])*60) + (12*60) + int(num_start.split(":")[1])
        
    # TRANSFOR DURATION INTO MINUTES
    drtn_ttl = (int(duration.split(":")[0])*60) + int(duration.split(":")[1])
        
    new_time_raw = start_ttl + drtn_ttl
    new_time_hrs = new_time_raw//60
    if new_time_raw%60 <10:
        new_time_mins = "0"+ str(new_time_raw%60)
    else:
        new_time_mins = new_time_raw%60
    new_time_days = new_time_raw//(24*60)
    
    # FIND WEEK DAY
    week_list = ["Monday", "Tuesday","Wenesday","Thursday","Friday","Saturday","Sunday"]  #Create a list of week to find Index
    
    week_day = list(week_day)
    if len(week_day) == 1 :
        x = (week_list.index(str.capitalize(week_day[0]))) #Find Current Day in owr list
        new_week_day = (", " + week_list[x+new_time_days%7])  #Find future day
    else :
        new_week_day = "" #not day in imput
    
    # PROCESS THE ARGUMENTS
    if new_time_days > 1:
        if new_time_hrs%24 > 12:
            new_time = str(new_time_hrs%24 - 12) + ":" + str(new_time_mins) + " PM" + new_week_day + " (" + str(new_time_days) + " days later)"
        else :
            new_time = str(new_time_hrs%24) + ":" + str(new_time_mins) + " AM" + new_week_day + " (" + str(new_time_days) + " days later)"
            
    elif new_time_days == 1:
        if new_time_hrs-24 > 12:
            new_time = str(new_time_hrs - 36) + ":" + str(new_time_mins) + " PM" + new_week_day + " (next day)"
        else :
            new_time = str(new_time_hrs - 24) + ":" + str(new_time_mins) + " AM" + new_week_day + " (next day)"
        
    else :
        if new_time_hrs > 12:
            new_time = str(new_time_hrs - 12) + ":" + str(new_time_mins) + " PM" + new_week_day
        else :
            new_time = str(new_time_hrs) + ":" + str(new_time_mins) + " AM" + new_week_day
    
    # RESULT
    return new_time #returns newtime
