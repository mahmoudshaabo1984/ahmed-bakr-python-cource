

# new list  قائمة جديدة تحتوي على عنصريين 
#  احمد وقيس
# tech_window_team = ['ahmed', 'qais']


# تغيير أماكن عناصر القائمة 
# طباعة القائمة وطباعة نوعها 
# tech_window_team = ['hero', 'ahmed', 'qais']
# print(tech_window_team)
# print(type(tech_window_team))

# اضافة عناصرلنفس القائمة عناصر مثل 
# رقم صحيح ورقم عشري
# tech_window_team = ['hero', 'ahmed', 'qais', 50, 1.5]
# print(tech_window_team)



#  new set set  يعني مجموعة 
# tech_window_team = {'hero', 'ahmed', 'qais', 50, 1.5}
# print(tech_window_team)
# print(type(tech_window_team))




# new tuple tuple يعني مصفوفة 
# tech_window_team = ('hero', 'ahmed', 'qais', 50, 1.5)
# print(tech_window_team)
# print(type(tech_window_team))


#أضافة عناصر نصية للمصفوفة tuple
# tech_window_team = ('ahmed', 'hero', 'ahmed', 'qais', 50, 1.5)
# print(tech_window_team)


#أضافة عناصر نصية للمجموعة tuple
# tech_window_team = {'ahmed', 'hero', 'ahmed', 'qais', 50, 1.5}
# print(tech_window_team)


# مصفوفى جديدة new tuple تحتوي على عنصر واحد
# test = ('ahmed',)
# print(test)
# print(type(test))


#other type of tuple
# مصفوفة جديدة تحتوي على عدة أنواع من البيانات 
# هذا نوع من أنواع المصفوفات نستخدمه من دون أقواس ()
# test = "ahmed" , 50 , 1.50  , True
# print(test)
# print(type(test))
 

# قائمة جديدة new list بأسم my_list قائمة فارغة 
# my_list = []
# print(my_list)
# print(type(my_list))


# #  مصفوفة جديدة  new tuple مصفوفة فارغة  بأسم my _tuple
# my_tuple = ()
# print(my_tuple)
# print(type(my_tuple))


# مجموعة جديدة  new set بأسم my_set 
# هنا يجب وبشكل أجباري أضافة عنصر لكي يتعرف الكود انها مجموعة set 
# وليست قاموس 
# my_set = {'ahmed'}
# print(my_set)
# print(type(my_set))
 

# قاموس جديد my_dec
# dec
# my_dec = {'user_name' : 'ahmed'}
# print(my_dec)
# print(type(my_dec))


#اضافة مفتاح آخر وقيمة لنفس القاموس السابق 
# my_dec = {'user_name' : 'ahmed', 'age' : 25}
# print(my_dec)
# print(type(my_dec))


# #input take the value from the user 
# # دالة input وظيفتها أخذ قيمة من المستخدم 
# user_name = input('inter your name:')
# print('hello',user_name)


# input take the value from the user such as name and age
# دالة input تأخذ قيم من المستخدم كالأسم والعمر 
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print('Your name: ', name, 'and Youur age: ', age)


#عمليات حسابية  
# محاولة جمع أرقام 
# هنا نحتاج الى تحويل البيانات casting int قبل الدالة input
# لكي نقوم بعملية الجمع بشكل صحيح 
# num1 = input("inter num1: ")
# num2 = input("inter num2: ")
# print(num1 +num2)




# عمليات حسابية باستخدام تحويل البيانات casting
# الطريقة الأولى نستخدم الدالة  int مع أقواسها () قبل الدالة هinput
# هذه الطريقة الأكثر شيوعا وأستخداما لسهولتها 
# num1 = int(input('inter num1: '))
# num2 = int(input('inter num2: '))
# print(num1 +num2)


# عمليات حسابية باستخدام تحويل البيانات casting الطريقة الثانية 
#هذه الطريقة لا تحول البيانت في الدالة print لذا لا تستخدمها 
# لذا لا ينصح بأستخدامها 
# num1 = input("inter num1: ")
# num2 = input("inter num2: ")
# print(int(num1 +num2))




#عمليات حسابية بأستخدام تحويل البيانات casting 
 # الطريقة الثالثة  وضع الدالة مع أسناد المتغير في صطر جديد 
# num1 = input('inter num1: ')
# num1 = int(num1)
# num2 = input('inter num2: ')
# num2 = int(num2)
# print(num1 +num2)




# العمليات الحسابية الطريقة الرابعة 
# يعرض هذا الكود نوع المتغير 
# كل صطر من الكود سوف يتم طباعة نوعه 
# في هذا الكود قام بالتحويل وطباعة ننوع المتغير لكل صطر 
# num1 = input('inter num1: ')
# print(type(num1))
# num1 = int(num1)
# print(type(num1))
# num2 = input('inter num2: ')
# print(type(num2))
# num2 = int(num2)
# print(type(num2))
# print(num1 +num2)

# انشاء متغير يحتوي على رقم صحيح وطباعة نوع هذا المتغير 
# phone_number = 7594322297
# print(type(phone_number))




# تحويل int to str 
# تحويل رقم صحيح الى نص 
# هنا حولنا الرقم الى نص str بأستخدام اسناد دالة str الى المتغير  
# phone_number  في صطر جديد 
# ايضا هنا قمنا بطباعة نوع المتغير بعد كل صطر 
phone_number = 7594322297
print(type(phone_number))
phone_number = str(phone_number)
print(type(phone_number))
