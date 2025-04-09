# myArr = [0,0,0,0]
# 
# def mySum(a,b):
#     if isinstance(a, int) and isinstance(b, int):
#         return a + b
#     else:
#         print("Vale sisestatud numbri tüüp")
#         
# def myCalculate(a,b,choice):
#     if isinstance(a, int) and isinstance(b, int):
#         if isinstance(choice, str):
#             if choice == '+':
#                 return a + b
#             elif choice == '-':
#                 return a - b
#             elif choice == '*':
#                 return a * b
#             elif choice == '/':
#                 if b != 0:
#                     return a / b
#                 else:
#                     return "Ei saa jagada nulliga"
#             else:
#                 return "Vale operaator"
#         else:
#             print("Vale sisestatud operaatori tüüp")
#     else:
#         print("Vale sisestatud numbri tüüp")
#         
# def myKorr(a,b):
#     if isinstance(a, int) and isinstance(b, int):
#         return a * b
#     else:
#         print("Vale sisestatud numbri tüüp")
#         
# def myMiinus(a,b):
#     if isinstance(a, int) and isinstance(b, int):
#         return a - b
#     else:
#         print("Vale sisestatud numbri tüüp")
#         
# def myJagamine(a,b):
#     try:
#         if isinstance(a, int) and isinstance(b, int):
#             return a / b
#         else:
#             print("Vale sisestatud numbri tüüp")
#     except ZeroDivisionError:
#         print("Ei saa jagada nulliga")
#         
# def main():
#     valik = input("Mida sa tahad? ")
#     if valik == "1":
#         a = int(input("Sisesta number 1: "))
#         b = int(input("Sisesta number 2: "))
#         myArr[0] += 1
#         print("Tulemus on:", mySum(a,b))
#     elif valik == "2":
#         a = int(input("Sisesta number 1: "))
#         b = int(input("Sisesta number 2: "))
#         myArr[1] += 1
#         print("Tulemus on:", myMiinus(a,b))
#     elif valik == "3":
#         a = int(input("Sisesta number 1: "))
#         b = int(input("Sisesta number 2: "))
#         myArr[2] += 1
#         print("Tulemus on:", myKorr(a,b))
#     elif valik == "4":
#         a = int(input("Sisesta number 1: "))
#         b = int(input("Sisesta number 2: "))
#         myArr[3] += 1
#         print("Tulemus on:", myJagamine(a,b))
#     elif valik == "5":
#         displayInfo()
#     elif valik == "6":
#         exit()
#     else:
#         print("Seda valikut ei ole")
# def displayInfo():
#     print("Kokku oli ", sum(myArr), "tehet")
#     print("Nendest oli ", myArr[0], " summeerimine")
#     print("Nendest oli ", myArr[1], " lahutamine")
#     print("Nendest oli ", myArr[2], " korrutamine")
#     print("Nendest oli ", myArr[3], " jagamine")
# 
# while True:
#     main()
# 


