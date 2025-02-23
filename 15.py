

# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة all 
# وظيفة هذه الدالة ارجاع العناصر دائما صح 
# num = [1, 2, 3, 4]
# if all(num):
#     print("All elements are True")
# else:
#     print("All elements are not True")



# الدالة all
# هنا اذا اضفنا عنصر خاطء سوف تعطينا 
# All elements are not True
# num = [1, 2, 3, 4, []]

# if all(num):
#     print("All elements are True")
# else:
#     print("All elements are not True")


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة any 
# وظيفة هذه الدالة ارجاع عنصر واحد على الأقل صحيح 
# num = [1, 2, 3, 4, []]
# if any(num):
#     print("All elements are True")
# else:
#     print("All elements are not True")



# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة any 
# وظيفة هذه الدالة ارجاع عنصر واحد على الأقل صحيح 
# هنا طبعنا رسالة بالعربي في الأمر الشرطي 
# num = [1, 2, 3, 4, []]
# if any(num):
#     print("لديك عنصر واحد صحيح على الأقل")
# else:
#     print("All elements are not True")


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة any 
# هنا تم ارجاع عنصر خاطء لأنه لا 
# يوجد عنصر صحيح على الأقل 
# فكانت النتيجة على الشكل التالي 
# All elements are not True
# num = [0, []]
# if any(num):
#     print("لديك عنصر واحد صحيح على الأقل")
# else:
#     print("All elements are not True")


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة bin 
## وظيفة هذه الدالة عرض مكان الرقم  او الحرف 
# في نظام البينري  binary system
# فكانت النتيجة 
#  0b1100100
# print(bin(100))

# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة bin 
# هنا نريد ان نعرف موقع الرقم 1 
# in binary system
# print(bin(1))


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة id وظيفة هذاهذه الدالة 
# معرفة الأيدي لكل عنصر 
# لأن كل عنصر يحجز مكان في الذاكرة 
# a = 20
# b = 30
# print(id(a))
# print(id(b))


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة range
# هذه الدالة تنشء ارقام للمستخدم
# عموما هذه الدالة تأخذ 3 معطيات من المستخدم
# بداياة وليست أجبارية نهاية  اجبارية وتخطي ايضا ليست أجبارية
# هنا  الرقم 10 أعتبرته الدالة نهاية 
# ملاحظة آخر عنصر لا يطبع في بيثون 
# print(list(range(10)))


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة range
# هنا قمنا بتعديل الكود 
#بحيث قمنا بأدخال بداية  5 ونهاية  20 وتخطي 3
# فيكون الناتج كالتالي 
# [5, 8, 11, 14, 17]
# print(list(range(5, 20, 3)))


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة print 
# في العادة هذه الدالة تترك صطر فارغ بعد طباعة الرسائل 
# print('hello ahmed','how r you')


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة print 
# هنا قمنا بتعديل الصطر الفارغ التي تتركه الدالة print
# أفتراضيا بحيث نقوم بأزالته تماما 
# print('hello ahmed','how r u', end='')


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة print 
# هنا قمنا بتعديل الصطر الفارغ ووضعنا علامة # 
# print('hello ahmed', 'how r u', end='#######')



# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة sum 
# هذه الدالة تأخذ معاملين من المستخدم اول معامل  الأول 
# النتيجة 55
# قابل للتكرار   iterable
# a = [5, 8, 11, 14, 17]
# print(sum(a))


# Python built-in functions 
# الدوال المدمجة في بيثون 
# الدالة sum 
# هنا وضعنا المعامل start 
# بعد المعامل iterable
# فقام بجمع الناتج 55 مع المعامل start 45 
# فاصبح الناتج 1000
# a = [5, 8, 11, 14, 17]
# print(sum(a, 45))


#  Python built-in functions 
#  الدوال المدمجة في بيثون 
#  الدالة sum 
#  هنا سوف يحدث خطء لأنه لا يمكن جمع رم مع نص 
# a = [5, 8, 11, 14, 17, 'ahmed']
# print(sum(a, 45))


# العمليات الحسابية فيpython 
# علامة الأس 
# الناتج 16 لأننا ضربنا 2 اربع مرات 
# print(2 ** 4)


# العمليات الحسابية 
# هنا الناتج 32
# print(2 ** 5)



#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة pow  تعامل هذه الدالة معاملة الأس 
# حيث تأخذ معاملين من المستخدم المعامل الأول start 
# وهو الرقم الأجباري المعامل الثاني وهو قوة الأس 
# أحيانا تأخذ معامل ثالث لباقي القسمة ليس أجباري 
# print(pow(2, 5))

#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة pow 
# هنا أعطتنا الدالة باقي القسمة 
# فيكون ناتج باقي القسمة 2
# ملاحظة باقي القسمة ليس اجباري للأدخال 
# print(pow(2, 5, 3))


#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة min 
# وظيفة هذه الدالة طباعة أصغر رقم في القائمة 
# الناتج -100
# a = [1, 50, 60, 70, -50, -2, -100]
# print(min(a))


#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة min 
# وظيفة هذه الدالة طباعة أصغر رقم في القائمة 
# الناتج -50
# a = [1, 50, 60, 70, -50, -2, ]
# print(min(a))




#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة min 
# وظيفة هذه الدالة طباعة أصغر رقم في القائمة 
# فيكون الناتج 1
# a = [1, 50, 60, 70, 50, 2, ]
# print(min(a))



#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة min 
# هنا أستخدمنا هذه الدالة لمعرفة 
# اصغر عنصر في النصوص 
# فيكون الناتج a
# a = [1, 50, 60, 70]
# b = ['ahmed', 'bakr', 'a', 'b']
# print(min(a))
# print(min(b))






#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة min 
# هنا أستخدمنا هذه الدالة لمعرفة 
# اصغر عنصر في النصوص 
# فيكونالناتج  b
# a = [1, 50, 60, 70, ]
# b = ['bakr' 'a', 'b']
# print(min(a))
# print(min(b))



#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة max
# وظيفة هذه الدالة طباعة اعلى عنصر 
# سواءا كان نص او رقم 
# a = [1, 50, 60, 70, ]
# b = ['bakr' 'a', 'b']
# print(max(a))
# print(max(b))




#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة max
# وظيفة هذه الدالة طباعة اعلى عنصر 
# سواءا كان نص او رقم 
# فيكون الناتج 1000 bakr
# a = [1, 50, 60, 70, 100, 1000, 200]
# b = ['bakr', 'a', 'b']
# print(max(a))
# print(max(b))




#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة map
# هذه الدالة تأخذ من المستخدم دالة او متغير 
# وتنفذها على دوال أخرى 
# def textFormat(text):
#     return f'# {text.capitalize()} #'

# tecwindowTeam = ['mahmoud', 'qais', 'ahmed', 'hero']

# myData = map(textFormat, tecwindowTeam)

# for name in myData:
#     print(name)


#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة filter
# وظيفة هذه الدالة فلترة العناصر في المتغيرات او 
# القوائم 
# def myData(data):
#     if data == 10:
#         return data

# myNum = [1, 5, 6, 2, 10, 100, 200]

# dataNum = filter(myData, myNum)

# for x in dataNum:
#     print(x)



#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة filter
# هنا أستخدمنا الكود من دون الأمر الشرطي فكانت 
# النتيجة مثل المثال السابق 
# def myData(data):
#     return data == 10

# myNum = [1, 5, 6, 2, 10, 100, 200]

# dataNum = filter(myData, myNum)

# for x in dataNum:
#     print(x)


#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة filter
# هنا أستخدمنا الدالة مع النصوص لكي نعرف
# هل هذا النص كان فيه أو بدء بأحرف  كبيرة 
# def myStr(data): 
#     if data.startswith('A'):
#         return data

# names = ['Ahmed', 'ali', 'amer']
# myStrData = filter(myStr, names)

# for x in myStrData:
#     print(x)



#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة filter
# هنا سنقوم بطباعة الكلمات في النص التي 
# تبدء بأحرف صغيرة 
# فتكون النتيجة كالتالي 
# ali amer
# def myStr(data): 
#     if data.startswith('a'):
#         return data

# names = ['Ahmed', 'ali', 'amer']
# myStrData = filter(myStr, names)

# for x in myStrData:
#     print(x)



#  Python built-in functions 
#  الدوال المدمجة في بيثون 
# الدالة filter
# هنا أستخدمنا الدالة بدون أمر  شرطي فتكون نفس النتيجة
# def myStr(data): 
#     return data.startswith('a')

# names = ['Ahmed', 'ali', 'amer']

# myStrData = filter(myStr, names)

# for x in myStrData:
#     print(x)

