# تعريف قائمة تحتوي على أسماء فريق TecWindow
tecwindow_team = ['hero', 'mahmoud', 'qais', 'nacer']

# إضافة الرقم 5 إلى نهاية القائمة باستخدام append()
tecwindow_team.append(5)

# إضافة النص 'aly' إلى نهاية القائمة باستخدام append()
tecwindow_team.append('aly')

# تعريف قائمة جديدة
new_team = ['ahmed', 'zeinab']

# إضافة القائمة new_team كعنصر واحد داخل القائمة الأصلية
tecwindow_team.append(new_team)

# طباعة القائمة الأصلية مع العناصر المضافة
# print(tecwindow_team)  # ['hero', 'mahmoud', 'qais', 'nacer', 5, 'aly', ['ahmed', 'zeinab']]

# الوصول إلى العنصر الأخير (القائمة الفرعية)
# print(tecwindow_team[6])  # ['ahmed', 'zeinab']

# الوصول إلى العنصر الثاني داخل القائمة الفرعية
# print(tecwindow_team[6][1])  # 'zeinab'

# الوصول إلى أول حرف في العنصر الثاني داخل القائمة الفرعية
# print(tecwindow_team[6][1][0])  # 'z'

# تفريغ القائمة من جميع العناصر باستخدام clear()
# tecwindow_team.clear()
# print(tecwindow_team)  # []

# وظيفة clear():
# تُزيل جميع العناصر من القائمة وتتركها فارغة.

# إزالة عنصرين محددين من القائمة باستخدام remove()
# tecwindow_team.remove('hero')  # إزالة العنصر 'hero'
# tecwindow_team.remove(5)       # إزالة العنصر 5
# print(tecwindow_team)  # ['mahmoud', 'qais', 'nacer', 'aly', ['ahmed', 'zeinab']]

# وظيفة remove():
# تُزيل أول ظهور للعنصر المحدد من القائمة.
# إذا لم يكن العنصر موجودًا، تُظهر خطأ `ValueError`.

# إزالة عنصر من موقع محدد باستخدام pop()
# tecwindow_team.pop(3)  # إزالة العنصر الموجود في الموقع 3 ('nacer')
# print(tecwindow_team)  # ['mahmoud', 'qais', 'aly', ['ahmed', 'zeinab']]

# وظيفة pop():
# تُزيل وتُرجع العنصر الموجود في الموقع المحدد. إذا لم يتم تحديد الموقع، تُزيل العنصر الأخير.

# تعريف قائمة تحتوي على أرقام
num = [5, 6, 6, 9, 7]

# دمج عناصر القائمة num داخل القائمة الأصلية باستخدام extend()
# tecwindow_team.extend(num)
# print(tecwindow_team)  # ['hero', 'mahmoud', 'qais', 'nacer', 5, 'aly', ['ahmed', 'zeinab'], 5, 6, 6, 9, 7]

# طباعة آخر عنصر في القائمة
# print(tecwindow_team[-1])  # 7

# الجمع بين قائمتين باستخدام علامة +
# print(tecwindow_team + num)  
# النتيجة: دمج القائمتين في قائمة جديدة دون تعديل القائمتين الأصليتين.

# إضافة عنصر في موقع معين باستخدام insert()
# tecwindow_team.insert(0, 'perfect')  # إضافة العنصر 'perfect' في الموقع 0
# test1 = 'hello'
# tecwindow_team.insert(0, test1)  # إضافة العنصر 'hello' في الموقع 0
# print(tecwindow_team)  

# وظيفة insert():
# تُضيف عنصرًا إلى موقع محدد داخل القائمة، وتقوم بإزاحة العناصر الأخرى.

# نسخ القائمة باستخدام copy()
# new_list = tecwindow_team.copy()

# تعديل العنصر الأول في القائمة الأصلية
# tecwindow_team[0] = 'python'

# دمج عناصر قائمة الأرقام num داخل القائمة الأصلية
# tecwindow_team.extend(num)

# طباعة القائمة الأصلية والقائمة المنسوخة
# print(tecwindow_team)  # القائمة المعدلة
# print(new_list)  # النسخة الأصلية قبل التعديل

# وظيفة copy():
# تُنشئ نسخة منفصلة من القائمة. التعديلات على القائمة الأصلية لا تؤثر على النسخة.

# تعريف قائمة أرقام وترتيبها
numbers = [5, 6, 6, 9, 7, 3, 1, 2]

# طباعة القائمة قبل الترتيب
# print(numbers)  # [5, 6, 6, 9, 7, 3, 1, 2]

# ترتيب القائمة تصاعديًا باستخدام sort()
# numbers.sort()
# print(numbers)  # [1, 2, 3, 5, 6, 6, 7, 9]

# ترتيب القائمة تنازليًا باستخدام sort(reverse=True)
# numbers.sort(reverse=True)
# print(numbers)  # [9, 7, 6, 6, 5, 3, 2, 1]

# وظيفة sort():
# تُرتب عناصر القائمة تصاعديًا (افتراضيًا) أو تنازليًا عند تمرير reverse=True.

# تعريف قائمة تحتوي على أسماء
names = ['zozo', 'perfect', 'qais', 'nacer', 'mahmoud', 'hero']

# ترتيب الأسماء تصاعديًا
# names.sort(reverse=False)
# print(names)  # ['hero', 'mahmoud', 'nacer', 'perfect', 'qais', 'zozo']

# إضافة رقم 5 إلى القائمة ومحاولة الترتيب
names.extend(5)  # TypeError: 'int' object is not iterable
names.sort(reverse=True)
print(names)

# وظيفة extend():
# تُضيف عناصر المجموعة إلى القائمة، ولكنها تتطلب أن تكون القيم من نوع قابل للتكرار (iterable).
