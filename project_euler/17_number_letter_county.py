from num2words import num2words


number_dict = {}

for i in range(1,1001):
    number_dict[i] = num2words(i)

number_list = (number_dict.values())
string_number = ""
listt = string_number.join(number_list).replace(" ", "")
print(len(listt.replace("-", "")))
