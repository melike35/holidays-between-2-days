from DateTime import DateTime
import holidays

a = [ ]

tr_holidays = holidays.Turkey ()



print ( "Please use one of these formats :  dd/mm/yyyy  , dd,mm,yyyy    or   dd.mm.yyyy " )

dt = DateTime ( input ( "Write first date  : " ) )

first_year = dt.year ()

dt2 = DateTime ( input ( "Write second date : " ) )

second_year = dt2.year ()

x = first_year
print ( type ( x ) )
while x <= second_year :
    tr_holidays = holidays.Turkey ( years=x )
    for date, occasion in tr_holidays.items ():
        a.append ( f'{date} - {occasion}' )
    x = x + 1

y = 0
print ( "There is  " + str ( len ( a ) ) + " holiday(s) between dates . " )
print ( "List of holidays  :  " )
for i in range(len(a)):

    print ( a[i])