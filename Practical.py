# 1. 
def main(): 
 
    num1 = float(input("Введіть перше число: ")) 
    num2 = float(input("Введіть друге число: ")) 
    num3 = float(input("Введіть третє число: ")) 
 
     
    if num1 >= 0: 
        num1_square = num1 ** 2 
    else: 
        num1_square = num1 ** 4 
 
    if num2 >= 0: 
        num2_square = num2 ** 2 
    else: 
        num2_square = num2 ** 4 
 
    if num3 >= 0: 
        num3_square = num3 ** 2 
    else: 
        num3_square = num3 ** 4 
 
 
    print("Результати:") 
    print("Піднесення до квадрата чисел, значення яких невід'ємні:") 
    print("Перше число:", num1_square) 
    print("Друге число:", num2_square) 
    print("Третє число:", num3_square) 
 
 
if name == "__main__": 
    main() 
     
def distance_to_origin(x, y): 
    """Функція для обчислення відстані від точки до початку координат.""" 
    return (x  2 + y  2) ** 0.5 
 
# 2. 
 
def main(): 

    x1 = float(input("Введіть координату x для точки A: ")) 
    y1 = float(input("Введіть координату y для точки A: ")) 
    x2 = float(input("Введіть координату x для точки B: ")) 
    y2 = float(input("Введіть координату y для точки B: ")) 
 
    distance_A = distance_to_origin(x1, y1) 
    distance_B = distance_to_origin(x2, y2) 
 
    if distance_A < distance_B: 
        print("Точка A знаходиться ближче до початку координат.") 
    elif distance_B < distance_A: 
        print("Точка B знаходиться ближче до початку координат.") 
    else: 
        print("Точки A і B знаходяться на однаковій відстані до початку координат.") 
 
 
if name == "__main__": 
    main() 
 
# 3. 
 
def is_triangle(angle1, angle2): 
    """Перевіряє, чи існує трикутник з заданими кутами.""" 
    Сума кутів трикутника повинна дорівнювати 180 градусам 
    if angle1 + angle2 < 180: 
        return True 
    else: 
        return False 
 
def is_right_triangle(angle1, angle2): 
    """Перевіряє, чи є трикутник прямокутним.""" 
    if angle1 == 90 or angle2 == 90 or (180 - angle1 - angle2) == 90: 
        return True 
    else: 
        return False 
 
def main(): 
    
    angle1 = float(input("Введіть перший кут трикутника (в градусах): ")) 
    angle2 = float(input("Введіть другий кут трикутника (в градусах): ")) 
 
    if is_triangle(angle1, angle2): 
        print("Трикутник існує.") 
        if is_right_triangle(angle1, angle2): 
            print("Трикутник є прямокутним.") 
        else: 
            print("Трикутник не є прямокутним.") 
    else: 
        print("Такий трикутник не існує.") 
 
 
if name == "__main__": 
    main() 
 
# 4. 
 
def main(): 
  
    x = float(input("Введіть число x: ")) 
    y = float(input("Введіть число y: ")) 
 
     
    if x == y: 
        print("Числа x і y повинні бути різними.") 
        return 
 
   
    min_num = min(x, y) 
    max_num = max(x, y) 
 
   
    new_min = (min_num + max_num) / 2 
    new_max = 2 * min_num * max_num 
 
    print("Після заміни:") 
    print("Менше число:", new_min) 
    print("Більше число:", new_max) 
 
 
if name == "__main__": 
    main() 
 
# 5. 
 
def main():
    
    x = float(input("Введіть координату x точки A: "))
    y = float(input("Введіть координату y точки A: "))

    if x == 0 and y == 0:
        print("Точка A знаходиться в початку координат.")
    elif x == 0:
        print("Точка A лежить на осі OY.")
    elif y == 0:
        print("Точка A лежить на осі OX.")
    elif x > 0 and y > 0:
        print("Точка A знаходиться в першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка A знаходиться в другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка A знаходиться в третьому квадранті.")
    else:
        print("Точка A знаходиться в четвертому квадранті.")

if __name__ == "__main__":
    main()

 
# 6. 
 
def main(): 
    
    a = int(input("Введіть ціле число a: ")) 
    b = int(input("Введіть ціле число b: ")) 
 
    if a != b: 
      
        max_num = max(a, b) 
        a = max_num 
        b = max_num 
    else: 
     
        a = 0 
        b = 0 
 
    print("Після заміни:") 
    print("a =", a) 
    print("b =", b) 
 
 
if name == "__main__": 
    main() 
 
 
# 7. 
def main(): 
 
    a = float(input("Введіть число a: ")) 
    b = float(input("Введіть число b: ")) 
    c = float(input("Введіть число c: ")) 
 
  
    count_positive = 0 
    if a > 0: 
        count_positive += 1 
    if b > 0: 
        count_positive += 1 
    if c > 0: 
        count_positive += 1 
 
    print("Кількість додатних чисел серед a, b, c:", count_positive) 
 
 
if name == "__main__": 
    main()
