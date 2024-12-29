# the format the first method 
# تعريف المتغيرات 
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my name is : %s and my age is: %d and my rank i: %f"% (name, age, rank))



#التحكم بالنص string وطباعة فقط Mester عىل الشاشة 
# التحكم بالفلوت وطباعة 0 واحد عىل الشاشة 
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my name is : %.6s and my age is: %d and my rank i: %.1f"% (name, age, rank))


# the format the second method 
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my name is : {} and my age is: {} and my rank i: {}".format(name, age, rank))



# تحديد نوع البيانات في طريقة الفورمات الجديدة 
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my name is : {:s} and my age is: {:d} and my rank i: {:f}".format(name, age, rank))



# التحكم بنوع البيانات النصوص والأرقام العشرية float
# هنا سوف يطبع "mester وصفر واحد في المتغير الثالث rank "
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my name is : {:.6s} and my age is: {:d} and my rank i: {:.1f}".format(name, age, rank))


# طريقة تغيير المتغيارات الطريقة الأولى in the format the second method 
# هنا تم تعديل المتغيرات من قبل المستخدم بشكل يدوي 
# .format(rank, name, age)
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my rank is : {} and my  name is: {} and my age is: {}".format(rank, name, age))




# طريقة ترتيب المتغيرات الطريقة الثانية وهي الطريقة الأفضل
# في هذه الطريقة نعتمد بترتيب المتغيرات على indexing 
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my rank is : {2} and my  name is: {0} and my age is: {1}".format(name, age, rank))



# طريقة ترتيب المتغيرات الطريقة الثانية وهي الطريقة الأفضل
# في هذه الطريقة نعتمد بترتيب المتغيرات على indexing 
# هنا نعيد كتابة نفس الكود مع أعادة تحديد أنواع البيانات مرة أخرى
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my rank is : {2:f} and my  name is: {0:s} and my age is: {1:d}".format(name, age, rank))



# طريقة ترتيب المتغيرات الطريقة الثانية وهي الطريقة الأفضل
# في هذه الطريقة نعتمد بترتيب المتغيرات على indexing 
# نعيد كتابة الكود مرة أخرى مع التحكم في النصوص str and float 
# name = "MesterPerfect"
# age = 25
# rank = 10
# print("my rank is : {2:.2f} and my  name is: {0:.6s} and my age is: {1:d}".format(name, age, rank))


# انشاء متغير جديد يحتوي على ارقام صحيحة 
# test = 56532448786
# print("my test number is: {:d}".format(test))




# انشاء متغير جديد يحتوي على ارقام صحيحة 
# التحكم بظهور العلامات عند طباعة الأرقام الصحيحة مثل  (_)
# test = 56532448786
# print("my test number is: {:_d}".format(test))




# انشاء متغير جديد يحتوي على ارقام صحيحة 
# هنا نضع علامة فاصلة ,
# test = 56532448786
# print("my test number is: {:,d}".format(test))


# هنا سوف يحدث خطء لأنه لا مكن أستخدام علامة الدولار في هذا الكود 
# test = 56532448786
# print("my test number is: {:$d}".format(test))




# the thrird method of the format the modern method 
# هذه الطريقة الأحدث للفورمات 
# name = "MesterPerfect"
# age = 25
# rank = 10
# print(f"name is: {name} age is: {age} rank is: {rank}")


# lists 
## new list قائمة جديدة 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# print(techwindow_team)



# اضافة عناصر للقائمة باستخدام الدالةappend
# هنا سوف يضيف عنصر في آخر القائمة 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# print(techwindow_team)


# اضافة عنصر نصي للقائمة 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append("aly")
# print(techwindow_team)




# انشاء قائمة جديدة تحتوي علىعنصرين أحمد ووزينب وأضافة هذه القائمة الى القائمة ارئيسية 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# print(techwindow_team)



# طباعة عنصر الأول من القائمة عن طريقةindexing 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# print(techwindow_team[0])



# طباعة العنصر الرابع من القائمة 
# سوف يطبع قائمة 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# print(techwindow_team)
# print(techwindow_team[4])


#  الدخول الى القائمة الثانية في القائمة الرئيسية وطباعة أول عنصر
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# print(techwindow_team)
# print(techwindow_team[4][0])



# طباعة الحرف الأول من ال العنصر الأول في القائمة الثانية 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# print(techwindow_team)
# print(techwindow_team[4][0][0])


# تفريغ القائمة بشطل نهائي باستخدام الدالة clear 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.clear() 
# print(techwindow_team)  



# حذف عنصر من القائمة 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# techwindow_team.remove("hero")
# print(techwindow_team)  

#  ازالة الرقم 5 من القائمة 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# techwindow_team.remove(5)
# print(techwindow_team)  
 
# ازالة العنصر الأول من اقائمة يعني العنصر الثاني بعد الصفر
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# techwindow_team.pop(1)
# print(techwindow_team)  

# ازالة آخر عنصر من القائمة  الرئيسية وهي القئمة الثانية 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# techwindow_team.pop(-1)
# print(techwindow_team)  






# new list
# توسيع القائمة الرئيسية تكويندو بقائمة أخرى 
# ععن طريق الدالة extend 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# num = [5, 6, 6, 9, 7]
# techwindow_team.extend(num)
# print(techwindow_team)


# طباعة آخر عنصر 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# num = [5, 6, 6, 9, 7]
# techwindow_team.extend(num)
# print(techwindow_team)
# print(techwindow_team[-1])





# دمج قائمتين  بأستخدام العلامة الزائد في دالة الطباعة print 
#  here we use + هنا نستخدم + للدمد بين القوائم 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# num = [5, 6, 6, 9, 7]
# print(techwindow_team + num)



# اضافة عناصر للقائمة باستخدام دالة insert 
# دالة insert  سوف تضيف عناصر جديدة لقائمة teckwindw_team 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# techwindow_team.insert(0, "Perfect")
# print(techwindow_team)


# نسخ القائمة الرئيسية عن طريق الدالةcopy 
# هنا أنشئنا قائمة أخرى وقمنا بنسخ القوائم 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# num = [5, 6, 6, 9, 7]
# techwindow_team.extend(num)
# new_list = techwindow_team.copy()
# print(techwindow_team)
# print(new_list)




# تعديل على القوائم
# تعديل العنصر الأول 
# techwindow_team = ["hero", "mahmoud", "qais", "naser"]
# techwindow_team.append(5)
# new_team = ["ahmed", "zainb"]
# techwindow_team.append(new_team)
# num = [5, 6, 6, 9, 7]
# techwindow_team.extend(num)
# new_list = techwindow_team.copy()
# techwindow_team.extend(num)
# techwindow_team[0] = "python "
# print(techwindow_team)
# print(new_list)




# تعريف قوائم غير مرتبة 
# numbers = [5, 6, 6, 9, 7, 3, 1, 2]
# print(numbers)
# # تعريف قائمة تحتوي على أسماء
# names = ['zozo', 'perfect', 'qais', 'nacer', 'mahmoud', 'hero']
# print(names)




# ترتيب الأرقام بأستخدام الدالة sort 
# هنا قمنا بترتيب الأرقام بشطل صحيح بأستخدام الدالة sort
# numbers = [5, 6, 6, 9, 7, 3, 1, 2]
# numbers.sort()
# print(numbers)



# ترتيب الأرقام بشكل عكسي 
# numbers = [5, 6, 6, 9, 7, 3, 1, 2]
# numbers.sort(reverse=True)
# print(numbers)



# ترتيب الأسماء بشطل صحيح 
# names = ['zozo', 'perfect', 'qais', 'nacer', 'mahmoud', 'hero']
# names.sort
# print(names)


# ترتيب الأسماء بشكل عكسي
names = ['zozo', 'perfect', 'qais', 'nacer', 'mahmoud', 'hero']
names.sort(reverse=True)
print(names)



# محاولة ترتيب رقم في مجموعة فيها أسماء بشكل عكسي سيحدث خطء
# لأنه لا يمكن ترتيب رقم مع أسماء بشكل عكسي
# names = ['zozo', 'perfect', 'qais', 'nacer', 'mahmoud', 'hero']
# names.extend(5)
# names.sort(reverse=True)
# print(names)