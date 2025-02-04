

# using for 
# انشاء قائمة تحتوي على أرقام من 1 الى 10
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)

# using for 
# انشاء قائمة تحتوي على أرقام من 1 الى 10
# هنا اأستخدمنا else بعد for 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)
# else:
#     print('تم طباعة قائمة الأرقام ')

# using for 
# هنا أستخدمنا if الشرطية لطباعة الأرقام الزوجية 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(f"الرقم {num} زوجي")
#     else:
#         print(f"الرقم {num} فردي")


# using for 
# هنا أستخدمنا if الشرطية لطباعة الأرقام الزوجية 
# اعادة كتابة الكود مرة اأخرى 
# لوضع else   الخاصة بfor 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(f"الرقم {num} زوجي")
#     else:
#         print(f"الرقم {num} فردي")

# else:
#     print('تم طباعة قائمة الأرقام')


# مثال ثاني لأستخدام for
# هنا طبع ahmedbakr حرف حرف
# myName = 'ahmedbakr'
# for name in myName:
#     print(name)



# مثال ثاني لأستخدام for
# هنا أستخدمنا الدالة range()
# وظيفة هذه الدالة انشاء قائمة من الأرقام 
#  يحددها المستخدم 
# هنا قمنا بأنشاء قائمة من الرقم 5 الى الرقم 50 
# myName = range(5, 50)
# for name in myName:
#     print(name)


# مثال ثاني لأستخدام for
# أنشاء قائمة من الرقم 5 الى الرقم 10 
# myName = range(5, 11)
# for name in myName:
#     print(name)


# استخدام  for في القواميس 
# هنا أولا قمنا بأنشاء قاموس يحتوي عىل
# 4 مفاتيح و4 قيم 
# mySkills = {
#     'HTML': '100%',
#     'CSS': '50%',
#     'js': '60%',
#     'php': '80%'
# }
# print(mySkills)
# print(mySkills['HTML'])



# استخدام  for في القواميس 
# هنا عندما قمنا بأنشاء حلقة for مع متغير جديد 
# اسمه skill  تم طباعة المفاتيح او المهارات فقط 
# mySkills = {
#     'HTML': '100%',
#     'CSS': '50%',
#     'js': '60%',
#     'php': '80%'
# }
# for skill in mySkills:
#     print(skill)


# استخدام  for في القواميس 
# هنا اذا اردنا ان نطبع القيم نطبعها برسالة ثانية 
# مع أستخدام الفورمات 
# mySkills = {
#     'HTML': '100%',
#     'CSS': '50%',
#     'js': '60%',
#     'php': '80%'
# }
# for skill in mySkills:
    # print(skill)
    # print(f'انا اتعلم {skill} و مستوايا الحالي هو {mySkills[skill]}')

# استخدام  for في القواميس 
# طباعة المفاتيح والقيم بأستخدام الفورمات 
# mySkills = {
#     'HTML': '100%',
#     'CSS': '50%',
#     'js': '60%',
#     'php': '80%'
# }
# for skill in mySkills:
#     print(f'انا اتعلم {skill} و مستوايا الحالي هو {mySkills[skill]}')


# انشاء for داخل for 
# هنا قمنا بأنشاء قائمتين 
# هنا طبع اسماء المستخدمين في القائمة الأولى  
# users = ['ahmed', 'qais', 'hero', 'mahmoud']
# skills = ['html', 'css', 'js', 'php', 'mysql', 'react']
# for user in users:
#     print(user)	


# انشاء for داخل for 
# هنا قمنا بأنشاء for ثانية لطباعة القائمة الثانية 
# التي تحتوي على المهارات فتم طباعة كل مستخدم مع مهاراته 
# users = ['ahmed', 'qais', 'hero', 'mahmoud']
# skills = ['html', 'css', 'js', 'php', 'mysql', 'react']
# for user in users:
#     print(user)
#     for skill in skills:
#         print(f'- {skill}')

# هنا قمنا بأنشاء 3 قواميس كل قاموس يحتوي 
# على 4  مفاتيح و4 قيم 
# tecWindowTeam = {
#     'ahmed': {
#         'HTML': '90%',
#         'CSS': '70%',
#         'Python': '80%',
#         'Dart': '60%',
#     },
#     'perfect': {
#         'JavaScript': '85%',
#         'Ruby': '75%',
#         'C++': '65%',
#         'Go': '50%',
#     },
#     'qais': {
#         'PHP': '95%',
#         'Java': '80%',
#         'Kotlin': '70%',
#         'Swift': '60%',
#     }
# }

# print(tecWindowTeam)


# هنا قمنا بأنشاء 3 قواميس كل قاموس يحتوي 
# على 4  مفاتيح و4 قيم 
# هنا سوف نقوم بطباعة القاموس الثالث qais
# بمفاتيحه وقيمه
# tecWindowTeam = {
#     'ahmed': {
#         'HTML': '90%',
#         'CSS': '70%',
#         'Python': '80%',
#         'Dart': '60%',
#     },
#     'perfect': {
#         'JavaScript': '85%',
#         'Ruby': '75%',
#         'C++': '65%',
#         'Go': '50%',
#     },
#     'qais': {
#         'PHP': '95%',
#         'Java': '80%',
#         'Kotlin': '70%',
#         'Swift': '60%',
#     }
# }

# print(tecWindowTeam['qais'])


# هنا قمنا بأنشاء 3 قواميس كل قاموس يحتوي 
# على 4  مفاتيح و4 قيم 
# هنا سوف نقوم بطباعة القاموس الثالث qais
# بمفاتيحه وقيمه
# هنا سوف نطبع قيمة المفتاح  PHP
# tecWindowTeam = {
#     'ahmed': {
#         'HTML': '90%',
#         'CSS': '70%',
#         'Python': '80%',
#         'Dart': '60%',
#     },
#     'perfect': {
#         'JavaScript': '85%',
#         'Ruby': '75%',
#         'C++': '65%',
#         'Go': '50%',
#     },
#     'qais': {
#         'PHP': '95%',
#         'Java': '80%',
#         'Kotlin': '70%',
#         'Swift': '60%',
#     }
# }

# print(tecWindowTeam['qais'])
# print(tecWindowTeam['qais']['PHP'])


# استخدام for داخل القواميس 
# هنا قام بطباعة فقط القواميس يعني المفاتيح 
# tecWindowTeam = {
#     'ahmed': {
#         'HTML': '90%',
#         'CSS': '70%',
#         'Python': '80%',
#         'Dart': '60%',
#     },
#     'perfect': {
#         'JavaScript': '85%',
#         'Ruby': '75%',
#         'C++': '65%',
#         'Go': '50%',
#     },
#     'qais': {
#         'PHP': '95%',
#         'Java': '80%',
#         'Kotlin': '70%',
#         'Swift': '60%',
#     }
# }

# for user in tecWindowTeam:
#     print(user)



# استخدام for داخل القواميس 
# هنا قمنا بطباعة المستخدمين مع مهراتهم 
# والمستوى الذي وصلو اليه 
# tecWindowTeam = {
#     'ahmed': {
#         'HTML': '90%',
#         'CSS': '70%',
#         'Python': '80%',
#         'Dart': '60%',
#     },
#     'perfect': {
#         'JavaScript': '85%',
#         'Ruby': '75%',
#         'C++': '65%',
#         'Go': '50%',
#     },
#     'qais': {
#         'PHP': '95%',
#         'Java': '80%',
#         'Kotlin': '70%',
#         'Swift': '60%',
#     }
# }

# for user in tecWindowTeam:
#     print(f'مهارات المستخدم {user} هي {tecWindowTeam[user]}')



# استخدام for داخل القواميس 
# هنا قمنا بأستخدام for اخرى 
# استخدمنا for اخرى لطباعة اللغة للمستخدم 
# والمستوى الذي وصل اليه فيها 
# tecWindowTeam = {
#     'ahmed': {
#         'HTML': '90%',
#         'CSS': '70%',
#         'Python': '80%',
#         'Dart': '60%',
#     },
#     'perfect': {
#         'JavaScript': '85%',
#         'Ruby': '75%',
#         'C++': '65%',
#         'Go': '50%',
#     },
#     'qais': {
#         'PHP': '95%',
#         'Java': '80%',
#         'Kotlin': '70%',
#         'Swift': '60%',
#     }
# }

# for user in tecWindowTeam:
#     print(f'مهارات المستخدم {user} هي {tecWindowTeam[user]}')
#     for skill in tecWindowTeam[user]:
#         print(f'اللغات هي{skill} والمستوى  هو: {tecWindowTeam[user][skill]}')



# استخدام for داخل القواميس 
# هنا قمنا بأستخدام for اخرى 
# هنا قمنا بتعديل الكود 
# قمنا بتعديل الكود بحيث يطبع اسم كل مستخدم 
# واللغات التي  يتقنها مع المستوى الذي وصل اليه 
# tecWindowTeam = {
#     'ahmed': {
#         'HTML': '90%',
#         'CSS': '70%',
#         'Python': '80%',
#         'Dart': '60%',
#     },
#     'perfect': {
#         'JavaScript': '85%',
#         'Ruby': '75%',
#         'C++': '65%',
#         'Go': '50%',
#     },
#     'qais': {
#         'PHP': '95%',
#         'Java': '80%',
#         'Kotlin': '70%',
#         'Swift': '60%',
#     }
# }

# for user in tecWindowTeam:
#     for skill in tecWindowTeam[user]:
#          print(f'المستخدم{user} يجيد لغ {skill } ومستواه هو : {tecWindowTeam[user][skill]}')



# انشاء قائمة تحتوي على أرقام 
# هنا أستخدمنا الأمر     continue
#  هنا بدء بالعد من الأول لكنه تجاهل الرقم  5
# numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num == 5:
#         continue
#     print(num)
    

# انشاء قائمة تحتوي على أرقام 
# هنا أستخدمنا الأمر break
# وظيفة هذا الأمر كسر اللوب عندما يصل الى الرقم 5
#  يقوم بكسر اللوب 
# numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num == 5:
#         break
#     print(num)


# انشاء قائمة تحتوي على أرقام 
# هنا أستخدمنا الأمر break
# وظيفة هذا الأمر كسر اللوب عندما يصل الى الرقم 5
# اذا اردنا ان نطبع الرقم المتاجهل نستخدم
#  أمر الطباعة بعد اللوب 
numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)
#     if num == 5:
#         break


# انشاء قائمة تحتوي على أرقام 
#  أستخدام الأمر pass
# أحيانا نستخدم هذا الأمر بدل التعليقات 
# نستخدم الأمر pass ايضا اذا اردنا ان نترك الأمر الشرطي
# بدون حذف ولا نريد ان نكمله 
# numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num == 5:
#         pass
#     print(num)


