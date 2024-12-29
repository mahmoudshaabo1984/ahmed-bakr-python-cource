
# new set 
# مجموعة جديدة تحتوي على عدد مختلف من البيانات 
# هنا ملاحظ  المجموعات لا تقبل التكرار 
# العناصر غير مرتبة في set 
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# print(type(a))
# print(a)


# العناصر غير مرتبة في set 
# هنا سوف يحدث خطء لأنني لا يمكنني 
# ان اصل الى العناصر as indixes 
# TypeError: 'set' object is not subscriptable
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# a [0]
# print(a)



# حذف عناصر من المجموعة 
# بأستخدام method remove 
# هنا حذفنا ا العنصر true  بنجاح 
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# a.remove(True)
# print(a)


# افراع المجموعة 
# بأستخدام clear 
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# a.clear()
# print(a)



# حذف عنصر غير موجود سوف يحدث خطء
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# a.remove("True")
# print(a)


# هنا اذا  حاولنا حذف عنصر غير موجود 
# بأستخدام the method discard 
# البرنامج سوف يعمل ولن يحدث خطء
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# a.discard("nasser")
# print(a)



# pop ترجع عنصر عشاوئي
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# print(a.pop())



# اضافة عنصر الى المجموعة 
# بأستخادام the method add
# هنا تم الأضافة للعنصر بشكل عشاوئي 
# من دون indexes 
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# a.add("qais")
# print(a)


# توحيد مجمعتين 
# بأستخدام الطريقة union
# a = {"ahmed", 'ahmed', True, False, 5, 6, 5}
# b = {1, 2, 3, 4, 5, 6, 6}
# a.union(b)
# print(a)


# تحديث مجموعة باستخدام update()
# هنا تم تحديث المجموعة القديمة 
# بمعلومات جديدة من المجموعة الجديدة
# a = {1, 1, 2, 3, 4, 4}
# b = {True, False, 'ahmed', 'ahmed', True}
# b.update(a)
# print(b)


# # تحديث المجموعة بقائمة list
# a = {1, 1, 2, 3, 4, 4}
# b = {True, False, 'ahmed', 'ahmed', True}
# b.update(a)
# b.update(["perfect", "tech window"])
# print(b)


# عرض الأختلاف بين مجمعتين بأستخدام الطريقة difference
# هنا سوف يطبع فقط الأختلاف
# يكون الأختلاف 3 4 5 
# a = {1, 2, 3, 4, 5}
# b = {1, 2, True, False, 'ahmed'}
# print(a.difference(b))


# using the method difference_update
# a = {1, 2, 3, 4, 5}
# b = {1, 2, True, False, 'ahmed'}
# a.difference_update(b)
# print(a)
# print(b)


# أظهار العناصر المتشابهة بين المجموعتين 
# عكس الطريقة السابقة 
# هنا العناصر المتشابهة 1 2 
# a = {1, 2, 3, 4, 5}
# b = {1, 2, True, False, 'ahmed'}
# print(a.intersection(b))


# استخدام intersection_update
# قامت هذه الطريقة بتحديث  المجموعة الثانية
# وأضافت المتشابهات بين المجموعتين 
# a = {1, 2, 3, 4, 5}
# b = {1, 2, True, False, 'ahmed'}
# a.intersection_update(b)
# print(b)


# # استخدام symmetric_difference() لإيجاد العناصر غير المشتركة بين المجموعتين
# # نستخدم طريقة  symmetric_difference لأظهار العناصر غير متشابهة 
# # غير متاشبهة عناصر موجودة في مجموعة وليست موجودة في الثانية 
# a = {'a', 'b', 'c', 'd', 'f', True}
# b = {'a', 'b', 'c'}
# print(a)
# print(a.symmetric_difference(b))


# new tuple  مصفوفة جديدة
# a = ("ahmed",)
# print(a)
# print(type(a))


# معرفة طول العناصر في المصفوفة 
a = ("ahmed",)
# print(len(a))
# print(type(a))


# مصفوفة جديدة من دون أقواس 
# a = "ahmed",
# print(a)
# print(type(a))


# اضافة عناصر جديدة للمصفوفة بدون أقواس
# a = "ahmed", True, False
# print(a)
# print(type(a))
# print(len(a))


# الوصول الى  العنصر الأخير in indixes 
# a = ("ahmed", True, False)
# print(a[-1])


# الوصول الى العنصر الثاني in indexes 
# a = ("ahmed", True, False)
# print(a[1])


# لا يمكن تعديل the first index in tuple او اي اندكس 
# لانه لا يمكن تعديل المصفوفة سوف يحدث خطء
# TypeError: 'tuple' object does not support item assignment
# a = ("ahmed", True, False)
# a[0] = "perfect"
# print(a)



#  مصفوفة جديدة تحتوي على عدة متغيرات 
# هنا في هذه المصفوفة أنشءنا اربع متغيرات على صطر واحد
# وأسندنا كل متغير لقيمته بنفس المصفوفة على نفس الصطر 
# a, b, c, d = "ahmed", "bakr", "mester", "perfect"
# print(a)
# print(b)
# print(c)
# print(d)



#  انشائ نفس المصفوة لكن بطريقة أخرى 
# حيث وضعنا هذه المصفوفة في متغير جديد f
# وفي الصطر الثاني قمنا بأنشاء ثلاث متغيرات a b c = 
# وجعلنا هذه المتغيرات تساوي قيمة المتغير الرابع f
# فيكون f قيمته المصفوفة 
# f = "ahmed", "bakr", "mester", "perfect"
# a, b, c, d = f
# print(a)
# print(b)
# print(c)
# print(d)


# اضافة عنصر خامس للمصفوة 
# هنا يجب علينا تجاهل واحد من المتغيرات لكي نستطيع ان نضيف 
# عنصر جديد للمصفوفة المتغير الذي تم تجاهله هو d
# f = "ahmed", "bakr", "mester", "perfect", "qais"
# a, b, c, _, d = f
# print(a)
# print(b)
# print(c)
# print(d)


# انشاء قائمة ومجموعة ومصفوفة 
# تكرار عناصر هذه البيانات بأستخدام علامة الضرب * 
# my_list = ["ahmed", "bakr"]
# my_set = {"ahmed", "bakr"}
# my_tuple = ("ahmed", "bakr")
# print(my_list * 50)
# print(my_set * 50)
# print(my_tuple * 50)
