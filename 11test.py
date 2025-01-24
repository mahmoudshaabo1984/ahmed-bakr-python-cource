

# loop
# وظيفة هذا اللوب تكرار العملية 
# لكننا نحتاج الى كسر اللوب 
# لأنه من دون الكسر سوف يتنفذ 
# الكود الى ما لا نهاية 
# a = 0
# while a <= 10:
#     print(a)
#     a += 1



# طباعة رسالة بعد كسر اللوب 
# a = 0
# while a <= 10:
#     print(a)
#     a += 1
# print('loop is done')

#using else 
# a = 0
# while a <= 10:
#     print(a)
#     a += 1
# else:
#     print('loop is dun')



# قائمة تحتوي على جميع أصدقاء احمد
# f = ["Ahmed", "Bakr", "Mohammed", "Ali", "nacer", "Mahmoud", "Qais", "Hero", "zozo", "Youssef"]
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[3])
# print(f[4])
# print(f[5])
# print(f[6])
# print(f[7])
# print(f[8])
# print(f[9])



# طباعة عناصر القائمة بأستخدام loop
# f = ["Ahmed", "Bakr", "Mohammed", "Ali", "nacer", "Mahmoud", "Qais", "Hero", "zozo", "Youssef"]
# print(len(f))

# a = 0
# while a < len(f):
#     print(f[a])
#     a += 1

# # طباعة علامة @ 
# f = ["Ahmed", "Bakr", "Mohammed", "Ali", "nacer", "Mahmoud", "Qais", "Hero"]
# a = 0
# while a < len(f):
#     print(f"@{f[a]}")
#     a += 1


# طباعة عناصر القائمة مع طباعة علامة # ورقم الأندكس 
# f = ["Ahmed", "Bakr", "Mohammed", "Ali", "nacer", "Mahmoud", "Qais", "Hero"]
# a = 0
# while a < len(f):
#     print(f"#{a} {f[a]}")
#     a += 1


# بداية من الرقم 1 
# هنا سوف يعد العناصر من رقم 1 وليس 0
# f = ["Ahmed", "Bakr", "Mohammed", "Ali", "nacer", "Mahmoud", "Qais", "Hero"]
# a = 0
# while a < len(f):
#     print(f"#{a + 1} {f[a]}")
#     a += 1



# مشروع آخر لأستخدام while in loop
# كتابة وتكرار المواقع المفضلة الي myFWeb = []
# myFWeb = []
# maxWeb = 5
# while maxWeb > 0:
#     web = input('قم بادخال الموقع الخاص بك بدون "https://" ')
#     myFWeb.append(f"https://{web}".strip().lower())
#     maxWeb -= 1
#     print(f"تم أدخال الموقع بنجاح \n يتبقى لك {maxWeb }أماكن")
#     print(myFWeb )

# else:
#     print("لقد أمتلءت القائمة لا يمكنك أضافة المزيد ")





# مشروع آخر لأستخدام while in loop
# كتابة وتكرار المواقع المفضلة الي myFWeb = []
# هنا سوف نستخدم if الشرطية myFWeb = []
# myFWeb = []
# maxWeb = 5

# while maxWeb > 0:
#     web = input('قم بادخال الموقع الخاص بك بدون "https://" ')
#     myFWeb.append(f"https://{web.strip().lower()}")
#     maxWeb -= 1
#     if maxWeb == 0:
#         print('لم يعد لديك أي أماكن')
#     else:
#         print(f"تم أدخال الموقع بنجاح \n يتبقى لك {maxWeb }أماكن")

        
# print(myFWeb)

# print("لقد أمتلءت القائمة لا يمكن أضافة المزيد")




# مشروع آخر لأستخدام while in loop
# كتابة وتكرار المواقع المفضلة الي myFWeb = []
# هنا سوف نطلب من المستخدم أدخال عدد المحاوالات 
# myFWeb = []
# maxWeb = int(input("ادخل عدد المحاوالات \n"))
# while maxWeb > 0:
#     web = input("قم بادخال الموقع الخاص بك بدون 'https://' ")
#     myFWeb.append(f"https://{web}".strip().lower())
#     maxWeb -= 1
#     if maxWeb == 0:
#         print("لم يتم   لديك أي أماكن")
#     else:
#         print(f"تم إضافة الموقع بنجاح.\nيتبقى لك   {maxWeb} أماكن")
# print(myFWeb)
# print("لقد أمتلءت القائمة لا يمكن أضافة المزيد")



#الكود المصحح من الذكاء الصناعي 
# هنا قمنا بأستبدال المسافات اثناء كتابة الموقع 
# بمعنى آخر اذا قام المستخدم بكتابة مسافات فلا تكتب 
# myFWeb = []
# maxWeb = 5

# while maxWeb > 0:
#     web = input('قم بادخال الموقع الخاص بك بدون "https://" ').strip().lower()
#     web = web.replace(' ', '')
#     myFWeb.append(f"https://{web}")
#     maxWeb -= 1

#     if maxWeb == 0:
#         print("لم يعد لديك أي أماكن")
#     else:
#         print(f"تم إضافة الموقع بنجاح.\nيتبقى لك   {maxWeb} أماكن")

#     print(myFWeb)
# else:
#     print("لقد امتلأت القائمة. لا يمكنك إضافة المزيد")




# الكود المصحح من المدرب احمد بكر 
# هنا ازلنا المسافات myFWeb = []
# myFWeb = []
# maxWeb = 5
# while maxWeb > 0:
#     web = input('قم بادخال الموقع الخاص بك بدون "https://" ').strip().lower()
#     web = web.replace(' ', '')

#     myFWeb.append(f"https://{web}")
#     maxWeb -= 1
#     if maxWeb == 0:
#         print("لم يعد لديك أي أماكن")
#     else:
#         print(f"تم إضافة الموقع بنجاح.\nيتبقى لك   {maxWeb} أماكن")

#     print(myFWeb)
# else:
#     print("لقد امتلأت القائمة. لا يمكنك إضافة المزيد")





# هنا قمنا بترتيب المواقع المفضلة لدي 
# هنا أستخدمنا if  الشرطية  لترتيب المواقع 
# myFWeb = []
# maxWeb = 5
# while maxWeb > 0:
#     web = input('قم بادخال الموقع الخاص بك بدون "https://" ').strip().lower()
#     web = web.replace(' ', '')

#     myFWeb.append(f"https://{web}")
#     maxWeb -= 1
#     if maxWeb == 0:
#         print("لم يعد لديك أي أماكن")
#     else:
#         print(f"تم إضافة الموقع بنجاح.\nيتبقى لك   {maxWeb} أماكن")

#     print(myFWeb)
# else:
#     print("لقد امتلأت القائمة. لا يمكنك إضافة المزيد")

# if len(myFWeb) > 0:
#     myFWeb.sort()
#     index = 0
#     print('هذه هي قائمة المواقع المفضلة الخاصة بك')
#     while index < len(myFWeb):
#         print(myFWeb[index])
#         index += 1

