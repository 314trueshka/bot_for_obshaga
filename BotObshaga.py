
import random


admins = []
studsovet = []
stores = {}
ads = []


def work_data(list_data, delete = False, update = False, add = False, new_data = None):
    data = ''

    if delete is not False:
        list_data.pop(delete)
        return "Удаление данных прошло успешно"

    if update is not False or (add and type(list_data) == dict):
        list_data[update or add] = new_data
        return "Обновление данных прошло успешно"

    if type(list_data) == list:
        if add:
            list_data.append(new_data)
            return "Обновление данных прошло успешно"
        for i in list_data:
            data+= f"{i}\n"

    elif type(list_data) == dict:
        for key in list_data:
            data+=f"{key}: \n {list_data[key]} \n \n"
    else:
        return "Непонятный тип данных"

    return data


print(work_data(admins, add=True,new_data='alik'))
print(admins)
print(work_data(admins,delete=0))
print(admins)