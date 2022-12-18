def horizont(yp, y1, x1, x2): # функция рассчета по горизонту
    if yp == y1:
        if max(x1, x2) < xp: 
            return 1
        elif min(x1, x2) > xp:
            return -1
        else: 
            return 3
    else: 
        return 0

def vertical(yp, y1, y2, x1, x2): # функция рассчета по вертикали
    if ((yp > y1) == (yp < y2)) or (y1 == yp) or (y2 == yp):
        if xp > max(x1, x2):
            return 1
        elif xp < min(x1, x2):
            return -1
        else: 
            return 3
    else:
        return 0

def diagonal(xt, xp): # функция вывода рассчетов по диагонали
    if xp > xt:
        return 1
    elif xp < xt:
        return -1
    else:
        return 3


def figure1(x0, y0, x1, y1, yp): # функция рассчета по дмгонали
    if x1 > x0:
        xt = x0 + ((yp-y0)*(x1-x0))/(y1-y0)
    else:
        xt = x0 + ((yp-y0)*-1*(x1-x0))/(y1-y0)
    if ((xt > x0) == (xt < x1)) or (x0 == xt) or (x1 == xt):
        return diagonal(xt, xp)
    else:
        return 0

x0 = 1
y0 = 2
x1 = 4
y1 = 5
x2 = 5
y2 = 1
x3 = 8
y3 = 5
x4 = 8
y4 = 3
x5 = 5
y5 = 0

xp = 6
yp = 5

# фигура 1 (проверяем первую фигуру) (проверяем каждую линию фигуры) (используем логические операции)
# if ((figure1(x0, y0, x1, y1, yp) == 1) and 
#    (figure1(x1, y1, x2, y2, yp) == -1) and 
#    (figure1(x2, y2, x3, y3, yp) == 0) and 
#    ((y3 == y0) and (horizont(yp, y0, x0, x3))==1)):
#     print("точка внутри")
# else:
#     print("точка снаружи")


# фигура 2, 3 (проверяем вторую фигуру) (проверяем каждую линию фигуры) (используем логические операции)
# if ((figure1(x0, y0, x1, y1, yp) == 1) and 
#    (figure1(x1, y1, x2, y2, yp) == -1) and 
#    ((y2 == y3) and (horizont(yp, y2, x2, x3))== 0) and 
#    (figure1(x3, y3, x0, y0, yp) == 0)): 
#     print("точка внутри")
# else:
#     print("точка снаружи")


# фигура 4 ()(проверяем последнюю фигуру) (проверяем каждую линию фигуры) (используем логические операции)
if ((figure1(x0, y0, x1, y1, yp) == 1) and 
   (figure1(x1, y1, x2, y2, yp) == 1) and 
   (figure1(x2, y2, x3, y3, yp) == 1) and
   ((x3 == x4) and (vertical(yp, y3, y4, x3, x4))== -1) and 
   (figure1(x4, y4, x5, y5, yp) == -1) and 
   (figure1(x5, y5, x0, y0, yp) == 0)):
    print("точка внутри")
else:
    print("точка снаружи")