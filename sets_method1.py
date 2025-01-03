# تعريف مجموعة تحتوي على عناصر متكررة
my_set1 = {'ahmed', 'ahmed', 'bakr', 5}
print(my_set1)  # النتيجة: {'ahmed', 'bakr', 5}
print(type(my_set1))  # النتيجة: <class 'set'>

# المجموعات (Set) تُزيل العناصر المكررة تلقائيًا.

---

# إزالة عنصر معين باستخدام remove()
my_set1 = {'ahmed', 'ahmed', 'bakr', 5}
my_set1.remove('ahmed')  # إزالة العنصر 'ahmed' من المجموعة
print(my_set1)  # النتيجة: {'bakr', 5}

# ملاحظة: إذا كان العنصر غير موجود، فستُظهر remove خطأ KeyError.

---

# تفريغ المجموعة باستخدام clear()
my_set1 = {'ahmed', 'ahmed', 'bakr', 5}
my_set1.clear()  # تفريغ جميع العناصر من المجموعة
print(my_set1)  # النتيجة: set()

---

# إضافة عنصر جديد باستخدام add()
my_set1 = {'ahmed', 'ahmed', 'bakr', 5}
my_set1.add('[perfect]')  # إضافة العنصر '[perfect]' إلى المجموعة
print(my_set1)  # النتيجة: {'ahmed', 'bakr', 5, '[perfect]'}

---

# دمج مجموعتين باستخدام union() وعلامة |
a = {1, 1, 2, 3, 4, 4}  # المجموعة a تحتوي على أرقام
b = {True, False, 'ahmed', 'ahmed', True}  # المجموعة b تحتوي على قيم منطقية ونصوص
print(b.union(a))  # النتيجة: {False, True, 1, 2, 3, 4, 'ahmed'}
print(b | a)  # نفس النتيجة باستخدام علامة |.

# وظيفة union():
# تُرجع مجموعة جديدة تحتوي على جميع العناصر من المجموعتين دون تكرار.

---

# إزالة عنصر باستخدام remove() وdiscard()
a = {1, 1, 2, 3, 4, 4}

# محاولة إزالة عنصر غير موجود باستخدام remove()
# print(a.remove('perfect'))  # KeyError: 'perfect'

# محاولة إزالة عنصر غير موجود باستخدام discard()
print(a.discard('perfect'))  # النتيجة: None (لا يُظهر خطأ)

# الفرق بين remove وdiscard:
# - remove: يُظهر خطأ إذا لم يكن العنصر موجودًا.
# - discard: لا يُظهر خطأ إذا لم يكن العنصر موجودًا.

---

# إزالة عنصر عشوائي باستخدام pop()
a = {'ahmed', 'ahmed', 'bakr', 5}
print(a.pop())  # يزيل عنصرًا عشوائيًا من المجموعة.
print(a)  # النتيجة: المجموعة بدون العنصر الذي تمت إزالته.

---

# تحديث مجموعة باستخدام update()
a = {1, 1, 2, 3, 4, 4}  # المجموعة a تحتوي على أرقام
b = {True, False, 'ahmed', 'ahmed', True}  # المجموعة b تحتوي على قيم منطقية ونصوص

# إضافة عناصر من المجموعة a إلى المجموعة b
b.update(a)

# إضافة عناصر أخرى إلى المجموعة b
b.update(['ahmed', True, '6'])
print(b)  # النتيجة: {False, True, 1, 2, 3, 4, 'ahmed', '6'}

# وظيفة update():
# تُضيف جميع العناصر من المجموعة أو القيم القابلة للتكرار إلى المجموعة الأصلية.
