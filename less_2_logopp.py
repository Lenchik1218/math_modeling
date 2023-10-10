a = 3
b = 4
c = 5

if a > 4 and b == 2: # and - операция логического "И"
    print('Good')
elif b > 3 or c == 5: # or - операция логического "ИЛИ"
    print('Best')
else:
    print('Bad')
a = 3
b = 5
c = -1

if a > 3 or c == 0:
    print('Good')
elif a <= 3 and b != 5:
    print('Best')
else:
    print('Bad')

if a >= 3 or b == 0:
    print('Good')
elif c == -1 or b > 4:
    print('Best')
else:
    print('Bad')
if((a==3 and c>0) or (b==5 and c<0)) and c ==-1:
    print ('Good')
else:
    print('Bad')