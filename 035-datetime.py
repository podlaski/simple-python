# Source: https://docs.python.org/3/library/datetime.html

from datetime import datetime

dt = datetime(2023, 1, 13, 20, 20, 20)
today = datetime.now()
today = today.strftime('Today is %A %d-%m-%Y, %H:%M.')
print('\nExample:', today, '\n')

types = ['%a (%%a) - Weekday as locale’s abbreviated name.',
    '%A (%%A) - Weekday as locale’s full name.', 
    '%w (%%w) - Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.',
    '%d (%%d) - Day of the month as a zero-padded decimal number.',
    '%b (%%b) - Month as locale’s abbreviated name.',
    '%B (%%B) - Month as locale’s full name.',
    '%m (%%m) - Month as a zero-padded decimal number.',
    '%y (%%y) - Year without century as a zero-padded decimal number.',
    '%Y (%%Y) - Year with century as a decimal number.',
    '%H (%%H) - Hour (24-hour clock) as a zero-padded decimal number.',
    '%I (%%I) - Hour (12-hour clock) as a zero-padded decimal number.',
    '%p (%%p) - Locale’s equivalent of either AM or PM.',
    '%M (%%M) - Minute as a zero-padded decimal number.',
    '%S (%%S) - Second as a zero-padded decimal number.',
    '%f (%%f) - Microsecond as a decimal number, zero-padded to 6 digits.',
    '%j (%%j) - Day of the year as a zero-padded decimal number.',
    '%U (%%U) - Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number.',
    '%W (%%W) - Week number of the year (Monday as the first day of the week) as a zero-padded decimal number.',
    '%c (%%c) - Locale’s appropriate date and time representation.',
    '%x (%%x) - Locale’s appropriate date representation.',
    '%X (%%X) - Locale’s appropriate time representation.',
    ]

for x in types:
    print(dt.strftime(x))
