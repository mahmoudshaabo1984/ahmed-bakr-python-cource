# تعريف قائمة تحتوي على أسماء فريق TecWindow
tecwindow_team = ['mahmoud', 'ahmed', 'qais']

# تعريف قائمة جديدة تحتوي على أسماء إضافية
new_team = ['zeinab', 'hero']

# طباعة القائمة الأصلية
# print(tecwindow_team)  # ['mahmoud', 'ahmed', 'qais']

# إضافة عنصر جديد للقائمة باستخدام append()
# tecwindow_team.append('aly')
# print(tecwindow_team)  # ['mahmoud', 'ahmed', 'qais', 'aly']

# إضافة قائمة أخرى كعنصر واحد باستخدام append()
# tecwindow_team.append(new_team)
# print(tecwindow_team)  # ['mahmoud', 'ahmed', 'qais', 'aly', ['zeinab', 'hero']]

# الوصول إلى العنصر المضاف (القائمة)
# print(tecwindow_team[4])  # ['zeinab', 'hero']

# الوصول إلى العنصر الأول داخل القائمة الفرعية
# print(tecwindow_team[4][0])  # 'zeinab'

---

# دمج عناصر قائمة أخرى داخل القائمة الأصلية باستخدام extend()
tecwindow_team.extend(new_team)
# print(tecwindow_team)  
# ['mahmoud', 'ahmed', 'qais', 'zeinab', 'hero']

# وظيفة extend():
# تُضيف عناصر القائمة الجديدة كعناصر مستقلة إلى القائمة الأصلية.

---

# إزالة عنصر معين من القائمة باستخدام remove()
tecwindow_team.remove('hero')
# print(tecwindow_team)  
# ['mahmoud', 'ahmed', 'qais', 'zeinab']

# وظيفة remove():
# تُزيل أول ظهور للعنصر المحدد من القائمة.
# إذا كان العنصر غير موجود، تُظهر خطأ `ValueError`.

# تجربة إزالة عنصر غير موجود
# tecwindow_team.remove('nacer')  # ValueError: list.remove(x): x not in list
# print(tecwindow_team)

---

# تعريف قائمة تحتوي على أرقام
a = [5, 6, 2, 3, 7, 8, 0]

# ترتيب القائمة تصاعديًا باستخدام sort()
# a.sort()
# print(a)  # [0, 2, 3, 5, 6, 7, 8]

# وظيفة sort():
# تُرتب عناصر القائمة تصاعديًا (افتراضيًا) أو تنازليًا عند تمرير `reverse=True`.

---

# إضافة عناصر متكررة وأرقام إلى القائمة
tecwindow_team.append('hero')
tecwindow_team.append('hero')
tecwindow_team.append('nacer')
tecwindow_team.append(55)

# محاولة ترتيب القائمة التي تحتوي على نصوص وأرقام باستخدام sort()
# tecwindow_team.sort(reverse=True)  
# TypeError: '<' not supported between instances of 'str' and 'int'

# وظيفة sort():
# تُرتب العناصر، ولكنها تتطلب أن تكون العناصر جميعها من نفس النوع (إما نصوص أو أرقام).

---

# عكس ترتيب العناصر في القائمة باستخدام reverse()
# tecwindow_team.reverse()
# print(tecwindow_team)

# وظيفة reverse():
# تُعكس ترتيب العناصر في القائمة دون ترتيبها تصاعديًا أو تنازليًا.

---

# طباعة القائمة النهائية
print(tecwindow_team)
# النتيجة: ['mahmoud', 'ahmed', 'qais', 'zeinab', 'hero', 'hero', 'nacer', 55]
