


# new dict 
# قاموس جديد يحتوي على 3 مفاتيح وثلاث قيم 
# user = {'username': 'ahmedbakr', 'age': 25, 'rank': 9.5}
# print(user)
# print(type(user))



# new dict 
# انشاء قاموس يحتوي على 3 قواميس 
# القاموس الأول يحتوي على 3 مفاتيح و3 قيم 
# القاموس الثاني يحتوي على مفتحين وقيمتين 
# القاموس الثالث فارغ
# techwindow = {
#     'user1': {
#         'name': 'ahmed',
#         'age': 25,
#         'Email': 'ahmedbakr593@gmail.com',
#     },
#     'user2': {
#         'name': 'hero',
#         'age': 27,
#     },
#     'user3': {},
# }
# print(techwindow)




# new dict 
# انشاء قاموس يحتوي على 3 قواميس 
# القاموس الأول يحتوي على 3 مفاتيح و3 قيم 
# القاموس الثاني يحتوي على مفتحين وقيمتين 
# القاموس الثالث فارغ
# هنا في القاموس الأول وضعنا مفتاح جديد بأسم l
# techwindow = {
#     'user1': {
#         'name': 'ahmed',
#         'age': 25,
#         'Email': 'ahmedbakr593@gmail.com',
#         'l': ['html', 'css', 'php', 'js', 'python', 'dart']
#     },
#     'user2': {
#         'name': 'hero',
#         'age': 27,
#     },
#     'user3': {},
# }
# print(techwindow)



# طباعة القاموس الأول فقط 
# عن طريق indexes 
# هنا قمنا بطباعة القاموس الآول من القاموس الكبير 
# techwindow = {
#     'user1': {
#         'name': 'ahmed',
#         'age': 25,
#         'Email': 'ahmedbakr593@gmail.com',
#         'l': ['html', 'css', 'php', 'js', 'python', 'dart']
#     },
#     'user2': {
#         'name': 'hero',
#         'age': 27,
#     },
#     'user3': {},
# }
# print(techwindow['user1'])


# الوصول الى المفتاح الثالث  l في القاموس الأول user1
# وطباعتها فقط 
# techwindow = {
#     'user1': {
#         'name': 'ahmed',
#         'age': 25,
#         'Email': 'ahmedbakr593@gmail.com',
#         'l': ['html', 'css', 'php', 'js', 'python', 'dart']
#     },
#     'user2': {
#         'name': 'hero',
#         'age': 27,
#     },
#     'user3': {},
# }
# print(techwindow['user1']['l'])




# انشاء 3 قواميس كل قاموس يحتوي على مفتحيم وقيمتين 
#  وجمع هذه القواميس الثلاث في قاموس رابع 
# user1 = {
#     'name': 'ahmed',
#     'age': 25,
# }

# user2 = {
#     'name': 'qais',
#     'age': 23,
# }

# user3 = {
#     'name': 'mahmoud',
#     'age': 26,
# }

# all_user = {
#     'user1': user1,
#     'user2': user2,
#     'user3': user3,
# }

# print(all_user)



# حتى ولو غيرنا أسماء الى المفاتيح في القاموس الرابع
# سوف تعمل القواميس الثلاثة 
# المهم القيم لا تتغير 
# user1 = {
#     'name': 'ahmed',
#     'age': 25,
# }

# user2 = {
#     'name': 'qais',
#     'age': 23,
# }

# user3 = {
#     'name': 'mahmoud',
#     'age': 26,
# }

# all_user = {
#     'u': user1,
#     'r': user2,
#     's': user3,
# }

# print(all_user)



# انشاء متغير يحتوي على قائمة 
# وأعطاء كل قاموس عنصر واحد من هذه القائمة 
l = ['html', 'css', 'php']
# user1 = {
#     'name': 'ahmed',
#     'age': 25,
#     'l': l[0],
# }

# user2 = {
#     'name': 'qais',
#     'age': 23,
#     'l': l[1],
# }

# user3 = {
#     'name': 'mahmoud',
#     'age': 26,
#     'l': l,
# }

# all_user = {
#     'u': user1,
#     's2': user2,
#     's3': user3,
# }

# print(all_user)



# طباعة محتويات القاموس الثالث 
# user3 
# هنا عندما وحدنا أسماء المفاتيح في القاموس الرابع 
# تجاهل القاموسين الالول والثاني وطبع محتويات القاموس الثالث 
l = ['html', 'css', 'php']
# user1 = {
#     'name': 'ahmed',
#     'age': 25,
#     'l': l[0],
# }

# user2 = {
#     'name': 'qais',
#     'age': 23,
#     'l': l[1],
# }

# user3 = {
#     'name': 'mahmoud',
#     'age': 26,
#     'l': l,
# }

# all_user = {
#     'u': user1,
#     'u': user2,
#     'u': user3,
# }

# print(all_user)



# أنشاء قاموس يحتوي على أربع مفاتيح وأربع قيم 
# user = {
#     'name': 'ahmed',
#     'age': 24,
#     'email': 'ahmedbakr593@gmail.com',
#     'phone': '01554240991'
# }
# print(user)


# أستخدام الدالة .keys 
# وظيفة هذه الدالة اظهار المفاتيح في القاموس 
# user = {
#     'name': 'ahmed',
#     'age': 24,
#     'email': 'ahmedbakr593@gmail.com',
#     'phone': '01554240991'
# }
# print(user.keys())



# استخدام الدالة .values
# وظيفة هذه الدالة عرض القيم في القاموس أثناء الطباعة  
# user = {
#     'name': 'ahmed',
#     'age': 24,
#     'email': 'ahmedbakr593@gmail.com',
#     'phone': '01554240991'
# }
# print(user.values())



# استخدام الدالة .update
# وظيفة هذه الدالة تحديث القيمة الأولى في المفتاح الأول
# name 
# user = {
#     'name': 'ahmed',
#     'age': 24,
#     'email': 'ahmedbakr593@gmail.com',
#     'phone': '01554240991'
# }
# user.update({'name': 'ahmedbakr'})
# print(user)



# طريقة ثانية لتحديث القاموس عن طريق indexes 
# هنا قمنا بتحديث المفتاح الثاني age  بقيمة جديدة  25
# user = {
#     'name': 'ahmed',
#     'age': 24,
#     'email': 'ahmedbakr593@gmail.com',
#     'phone': '01554240991'
# }
# user.update({'name': 'ahmedbakr'})
# user['age'] = 25
# print(user)



# استخدام .fromkeys
#  هنا قمنا بأنشاء متغيرين  a and b 
# المتغير الأول a يحتوي على  مصفوفة tuple 
# المتغير الثاني b يحتوي عىل نص str
# بأستخدام الدالة .fromkeys قمنا بتحويل 
# المتغيرين الى قاموس 
# هنا تم أسناد كل مفتاح من المصفوفة 
# الى القيمة ahmed في المتغير الثني 
# a = ('key1', 'key2', 'key3')
# b = 'ahmed'
# print(dict.fromkeys(a, b))




# # هنا كانت قيمة كل مفتاح في المصفوفة الأولى 
# # جميعة العناصر في المصفوفة الثانية 
# # {'key1': ('ahmed', 'bakr', 'perfect'), 
# # key2': ('ahmed', 'bakr', 'perfect'), 
# # key3': ('ahmed', 'bakr', 'perfect')} 
# a = ('key1', 'key2', 'key3')
# b = 'ahmed', 'bakr', 'perfect'
# print(dict.fromkeys(a, b))




# تحويل البيانات 
# انشاء 5 أنواع بيانات 
# النوع الآول نص 
# النوع الثاني قائمة 
# النوع الثالث مجموعة set 
# النوع الرابع مصفوفة tuple 
# النوع الخامس قاموس dict
# قمنا بطباعة 5 أنواع بيانات 
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(a)
# print(b)
# print(c)
# print(d)
# print(f)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(f))


# تحويل النوع الآول {a} الى قائمة 
# كان هذا النوع هو عبارة عن نص str 
# وتم تحويله  الى  قائمة 
a = 'ahmed'
b = ['ahmed', 'bakr']
c = {'ahmed', 'bakr'}
d = 'ahmed', 'bakr'
f = {'f': 'ahmed', 'l': 'bakr'}
# print(list(a))
# print(type(list(a)))



# تحويل النوع الثالث set الى قائمة 
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(list(c))
# print(type(list(c)))



# تحويل النوع الرابع الى قائمة 
# النوع الرابع هو بالآصل مصفوفة 
# سنقوم بتحويله الى قائمة 
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(list(d))
# print(type(list(d)))



# تحويل النوع الخامس وهو بالأصل قاموس 
# الى قائمة list
# هنا تم طباعة المفاتيح فقط وليست القيم 
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(list(f))
# print(type(list(f)))



# تحويل الانوع الثاني وهو بالأصل قائمة الى نص str
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(str(b))
# print(type(str(b)))



# تحويل النوع الثالث الى نص str
# النوع الثالث بالآصل مجموعة set
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(str(c))
# print(type(str(c)))



# تحويل النوع الرابع الى نص str
# النوع الرابع بالأصل مصفوفة tuple
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(str(d))
# print(type(str(d)))



# # تحويل النوع الخامس الى نص str
# # النوع الخامس بالأصل قاموس 
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(str(f))
# print(type(str(f)))




# تحويل اأنواع البيانات الثلاثة  a b c 
# الى قاموس 
# لم نحول النوع الرابع لأنه بالأصل قاموس 
#  هنا سوف يحدث خطء لأنه لتحويل  نوع البيانات الى قاموس 
# يحتاج قيمتين على الآقل 
# ValueError: dictionary update sequence element #0 has length 1; 2 is required   
# a = 'ahmed'
# b = ['ahmed', 'bakr']
# c = {'ahmed', 'bakr'}
# d = 'ahmed', 'bakr'
# f = {'f': 'ahmed', 'l': 'bakr'}
# print(dict(a))
# print(type(dict(a)))
# print(dict(b))
# print(type(dict(b)))
# print(dict(c))
# print(type(dict(c)))
# print(dict(d))
# print(type(dict(d)))



# العمليات المنطقية 
# false
# print(50 < 40)


# العمليات المنطقية 
# True
# print(50 > 40)



# العمليات المنطقية 
# false
# print(50 > 50)



# العمليات المنطقية 
# false
# print(50 < 50)


# العمليات المنطقية 
# True
# print(50 <= 50)


# العمليات المنطقية 
# True
# print(50 >= 50)



# العمليات المنطقية 
# True
# print(50 == 50)



# العمليات المنطقية 
# False
# print(50 == 49)


# using and with priint with numbers 
# False
# وظيفة and التحقق من الشرطين 
# بمعنى آخر لا تعطيك True الا اذا كان الشرطين صحيحين 
# هنا أعطانا False
# print(50 == 50 and 50 < 48)




# هنا سوف نقوم بتغيير الشرط الثاني 
# لكي يتتطابق مع الشرط الأول 
# True
# print(50 == 50 and 50 > 48)



# using or 
# وظيفة or هو طباعة شرط من شرطين 
# Tru 
# هنا طبع True  لأن الشرط الآول صحيح 
# print(50 == 50 or 50 > 48)




# using not 
# وظيفة not هو نفي الشرط حتى ولو كان صحيحا 
# False 
print(not 50 == 50)
