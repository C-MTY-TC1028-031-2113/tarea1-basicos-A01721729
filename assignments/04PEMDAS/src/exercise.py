def main():
    from math import sqrt
    import math
    oper1 = (2+3/4) + (4 + 2/3) - (3 + 1/5) + (5 + 1/2)
    oper2 = 2*math.sqrt(35**2) + 4*math.sqrt(36**3) - 6*math.sqrt(49**2)
    a = 4
    b = 5
    oper3 = (a**3 + 2*b**2) / (4*a)
    oper4 = ((2*((a+b)**2) + 4*((a-b)**2)) / (a*b**2))
    oper5 = math.sqrt((a+b)**2 + 2**(a+b)) / (2*a + 2*b)**2

    oper1 = round(oper1,4)
    oper2 = round(oper2,4)
    oper3 = round(oper3,4)
    oper4 = round(oper4,4)
    oper5 = round(oper5,4)

    print(oper1)
    print(oper2)
    print(oper3)
    print(oper4)
    print(oper5)
<<<<<<< HEAD
=======
    
>>>>>>> c2ceebafba41cd6cfdd3c2d926cceb21cb1a35fa
   



if __name__ == '__main__':
    main()
