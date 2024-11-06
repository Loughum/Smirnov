# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, divider=','):
    participants_list1 = str1.split(divider)
    participants_list2 = str2.split(divider)
    common = []
    for elem in participants_list1:
        if elem in participants_list2:
            common.append(elem)
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(participants)
