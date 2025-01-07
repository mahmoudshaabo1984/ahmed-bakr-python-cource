

# استخدام if statement
# انشاء اربع متغيرات 
# name = 'ahmed'
# cName = 'Python Course'
# price = 50
# print(f' hello {name} this is: "{cName}" the course price is: ${price}')



# استخدام if statement
#انشاء 5 متغيرات 
# هنا أنشءنا متغير رابع باسم  country  
# ووضعنا شرط للتخفيض الكورس 
# name = 'ahmed'
# course = 'Python Course'
# price = 50
# country = 'egypt' 
# if country == 'egypt':
#     print(f'Hello {name}, this is: "{course}". Because you are from {country}, the course price is: ${price - 40}')




# استخدام if statement
# هنا نستخدم if statement بشكل تفاعلي 
# عن طريق طلب من المستخدم أدخال أسمه  ودولته 
# اذا ادخلنا دولة غير مصر لن يطبع اي شيء
# name = input('enter your name: ')
# cName = 'Python Course'
# price = 50
# country = input('enter your country: ')

# if country == 'egypt':
#     print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 40}')      


# استخدام if statement
# هنا نستخدم if statement بشكل تفاعلي 
# عن طريق طلب من المستخدم أدخال أسمه  ودولته 
# هنا سوف نقوم بأدخال دولة غير مصر
# name = input('enter your name: ')
# country = input('enter your country: ')
# cName = 'Python Course'
# price = 100

# if country == 'egypt':
#     print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      

# else :
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price}')      




# استخدام if statement
# هنا نستخدم if statement بشكل تفاعلي 
# عن طريق طلب من المستخدم أدخال أسمه  ودولته 
# هنا سوف نقوم بتغير سعر الكورس  ليصبح 100 دولار 
# name = input('enter your name: ')
# country = input('enter your country: ')
# cName = 'Python Course'
# price = 100

# if country == 'egypt':
#     print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      

# else :
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price}')      






# استخدام if statement
# هنا سوف نعطي السعودية خصم بقيمة 50 دولار 
# عن طريق أستخدام الدالة االشرطية elif 
# name = input('enter your name: ')
# country = input('enter your country: ')
# cName = 'Python Course'
# price = 100

# if country == 'egypt':
#     print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      
# elif country == 'ksa':
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 50}')      

# else :
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price}')      




# وضع أسماء الدول باللغة العربية 
# name = input('enter your name: ')
# country = input('enter your country: ')
# cName = 'Python Course'
# price = 100

# if country == 'مصر':
#     print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      
# elif country == 'السعودية':
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 50}')      

# else :
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price}')      




# طباعة الدول سوائا كانت بالعربي  أو باللغة الأنجليزية 
# هنا ستظهر النتيجة بشكل صحيح سواءا وضعنا المعلومات 
# بالعربي  او باللغة الأنجليزية 
# name = input('enter your name: ')
# country = input('enter your country: ')
# cName = 'Python Course'
# price = 100

# if country == 'مصر' or country == 'egypt':
#     print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      
# elif country == 'السعودية' or country == 'ksa':
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 50}')      

# else :
#         print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price}')      




# استخدام if الداخلية
#  طباعة نوع الجنس
# هنا سوف يطبع نوع الجنس 
# name = input('enter your Name: ')
# country = input('enter your Country: ')
# cName = 'Python Course'
# gender = input('enter your Gender: ')
# price = 100
# if country == 'مصر' or country == 'egypt':
#     if gender == 'ذكر':
#             print(f' hello mr {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      


# else:
#             print(f' hello  ms {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      


# هذا كود خاطء  بكتابة الشرط وجوابه على نفس الصطر 
# فيكون صطر طويل يصعب فهمه 
# نحتاج الى clean code لكي يكون الكود  منظم وسهل للقراءة والفهم 
# if country == 'مصر' or country == 'egypt': print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 90}')      

# elif country == 'السعودية' or country == 'ksa': print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price - 50}')      

#         # else : print(f' hello {name} this is: {cName} Because u r from {country} the course price is: ${price}')      





# استخدام  if العادية 
# هنا حاولنا حساب عمر الشخص اذا اراد مشاهدة فلم القناص 
# اذا كان عمره اقل من 15 عام الفلم ليس جيدا لعمره 
# movie = 'القناص'
# movreRate = 18
# age = 15

# if age < movreRate:
#     print(f"the movie {movie} is not good for u")
# else:
#     print(f"the movie {movie} is good For u")




# استخدام  if العادية 
# هنا غيرنا العمر الى 25 
# فأصبح الفلم مناسب للعمر المختار وفق الشرط 
# movie = 'القناص'
# movreRate = 18
# age = 25

# if age < movreRate:
#     print(f"the movie {movie} is not good for u")
# else:
#     print(f"the movie {movie} is good For u")



# using short if in the print 
# هنا أستخدمنا if القصيرة  بنفس صطر الطباعة 
# movie = 'القناص'
# movreRate = 18
# age = 25
# print(f"the movie {movie} is not good For u!" if age < movreRate else f"the movie {movie} is good For u!")




# using short if in the print 
# هنا أستخدمنا if القصيرة  بنفس صطر الطباعة 
# هنا سوف نقوم بتغير عمر المستخدم
# movie = 'القناص'
# movreRate = 18
# age = 15
# print(f"the movie {movie} is not good For u!" if age < movreRate else f"the movie {movie} is good For u!")



# طباعة نص عادي 
# هنا طبعنا نص عادي 
# هنا اذا غيرنا العمر  سوف تتغيرأمر الطباعة 
# movreRate = 18
# age = 15
# print("the movie is not good For u!" if age < movreRate else "the movie is good For u!")




# using in in if statement
# هنا أنشءنا متغيرين الأول بأسم ادمن 
# يحتوي على قائمة 
# الثاني بأسم name  أستخدمنا فيه الآمر input   للتحقق من أسم موجود في القائمة 
# اذا كان موجود يطبع الشرط الآول 
# واذا لم يكن موجود يطبع الشرط الثاني 
# admins = ['ahmed', 'qais']
# name = input('enter your name: ')
# if name in admins:
#     print('hello admin')
# else:
#     print('hello user')



# using match  and case 
# هنا الحالة  in_progress
# سوف يطبع  task is currently in progress
# status = "in_progress"
# match status:
#     case "new":
#         print("The task is new.")
#     case "in_progress":
#         print("The task is currently in progress.")
#     case "completed":
#         print("The task has been completed.")
#     case _:
#         print("Unknown status.")




# using match  and case 
# هنا الحالة Unknown status
# ل لأننا غيرنا قيمة المتغير الى 1
status = 1
match status:
    case "new":
        print("The task is new.")
    case "in_progress":
        print("The task is currently in progress.")
    case "completed":
        print("The task has been completed.")
    case _:
        print("Unknown status.")

