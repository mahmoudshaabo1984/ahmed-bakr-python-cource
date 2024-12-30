# تعريف المتغيرات التي تمثل مجموعات البيانات المختلفة في Python
string_data = "Hello, World!"
list_data = [1, 2, 3, 4, 5]
tuple_data = (10, 20, 30, 40, 50)
set_data = {"apple", "banana", "cherry"}
dict_data = {"name": "Alice", "age": 30, "city": "Cairo"}

# طباعة المتغيرات
print("المتغيرات الأصلية:")
print("String:", string_data)
print("List:", list_data)
print("Tuple:", tuple_data)
print("Set:", set_data)
print("Dictionary:", dict_data)

# طباعة المتغيرات مع النوع باستخدام دالة type()
print("\nالمتغيرات مع الأنواع:")
print("String:", string_data, "Type:", type(string_data))
print("List:", list_data, "Type:", type(list_data))
print("Tuple:", tuple_data, "Type:", type(tuple_data))
print("Set:", set_data, "Type:", type(set_data))
print("Dictionary:", dict_data, "Type:", type(dict_data))

# التحويل بين الأنواع المختلفة
# تحويل string إلى list
converted_list = list(string_data)
print("\nتحويل string إلى list:", converted_list)

# تحويل list إلى tuple
converted_tuple = tuple(list_data)
print("تحويل list إلى tuple:", converted_tuple)

# تحويل tuple إلى set
converted_set = set(tuple_data)
print("تحويل tuple إلى set:", converted_set)

# تحويل set إلى list
converted_list_from_set = list(set_data)
print("تحويل set إلى list:", converted_list_from_set)

# تحويل dictionary keys إلى list
keys_as_list = list(dict_data.keys())
print("تحويل مفاتيح dictionary إلى list:", keys_as_list)

# تحويل dictionary values إلى tuple
values_as_tuple = tuple(dict_data.values())
print("تحويل قيم dictionary إلى tuple:", values_as_tuple)
