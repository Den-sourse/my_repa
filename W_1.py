# # # #########################The Tack №1
# # # # # a = input('введите переменную: ')
# # # # # b = int(input("Еще одну переменную "))
# # # # # с = float(input("И снова переменную: "))
# # # # # print(a)
# # # # # print(b)
# # # # # print(C)
# # # #
# # # #########################The Tack №2 ### Программу писал сам, все работает , но выглядит некрасиво
# # # # time_second = int(input('Please enter the time in seconds: '))
# # # # time_minutes = int(time_second / 60)
# # # # ost = int(time_second % 60)
# # # # time_hour = int(time_minutes / 60)
# # # # ost2= int(time_minutes % 60)
# # # # if ost > 60:
# # # #     time_second = ost - 60
# # # #     time_minutes = time_minutes + 1
# # # #     print(f'minutes {time_minutes} : second {time_second}')
# # # # else:
# # # #     print(f'minutes {time_minutes} : second {ost}')
# # # #     if ost2 > 60:
# # # #         time_minutes = ost - 60
# # # #         time_hour = time_hour + 1
# # # #         print(f'hour {time_hour} minutes {time_minutes} : second {ost}')
# # # #     else:
# # # #         print(f'hour {time_hour} minutes {ost2} : second {ost}')
# # # #########################The Tack №3
# # # num_1 = input('Enter number n please: ')
# # # num_2 = num_1 * 2
# # # num_3 = num_2 + num_1
# # # summ = int(num_1) + int(num_2) + int(num_3)
# # # print('суммa чисел n + nn + nnn =', summ)
# # # #########################The Tack №4 , Я немного не понял как это задание можно выполнить через Цикл , прошу прощения
# # number = input('Вводим длинную цифру: ')
# # print(number)
# # number_1 = set(number)
# # print(max(number_1))
# # # #########################The Tack №5 Вообще не понял задачу .
# # # #########################The Tack №6
# a = int(input('Введите результат пробежки (км) спортсмена в первый день: '))
# b = int(input('Введите желаемый результат (км), и я скажу сколько на это уйдет дней: '))
# rez_a = a / 100 * 10
# i = 0
# while True:
#     i += 1
#     rez_a = a / 100 * 10
#     a = a + rez_a
#     if a >= b:
#         print(i)
#         break
#
