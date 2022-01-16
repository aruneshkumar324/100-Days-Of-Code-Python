# try:
#     file = open('demo.txt', 'r')
#
#     dic = {"key":"value"}
#     print(dic['keysd'])
#
# except FileNotFoundError:
#     file = open('demo.txt','w')
#     file.write('Hello')
#
# except KeyError as error_message:
#     print(error_message)
#
# # else will work if try correct
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     # file.close()
#     # print('file closed')
#
#     raise TypeError('this is error')


height = float(input('Height : '))
weight = int(input('Weight : '))

if height > 3:
    raise ValueError('Height must be below 3 meter')

BMI = weight / height ** 2

print(BMI)
