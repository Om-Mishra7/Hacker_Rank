def timeConversion(s):
    
    if (s[8::1]).upper() == "AM":

        # Making hour part 00 if it is 12
        if s[0:2] == "12":
            return("00" + str(s[2:-2]))
        else:
            return (str(s[0:-2]))
    
    elif (s[8::1]).upper() == "PM":
        
        # Making hour part 12 if it is 12
        if s[0:2] == "12":
            return(str(s[0:-2]))
        else:
            return(str(int( s[0:2] ) + 12) + str(s[2:-2]))
    
    else:
        return ("Invalid Time Format")

# Sample Input

s = "12:45:54PM"

print(timeConversion(s))