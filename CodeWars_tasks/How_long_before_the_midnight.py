```
The function minutesToMidnight(d) will take a date object as parameter. Return the number of minutes in the following format:

"x minute(s)"
```

def minutes_to_midnight(time_inp):
    minutes = time_inp.hour*60 + time_inp.minute
    result = (23*60+60 - minutes - round(time_inp.second / 60))

    return f"{result} minute{'s' if result > 1 else ''}"
