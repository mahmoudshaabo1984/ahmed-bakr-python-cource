# تعريف قائمة تحتوي على أسماء فريق TecWindow
tecwindow_team = ['mahmoud', 'hero', 'qais', 'ahmed', 'zozo']

# طباعة القائمة الأصلية
# print(tecwindow_team)  # ['mahmoud', 'hero', 'qais', 'ahmed', 'zozo']

# استخدام clear() لتفريغ القائمة من جميع العناصر
# tecwindow_team.clear()
# print(tecwindow_team)  # []

# وظيفة clear():
# تقوم بحذف جميع العناصر من القائمة، وتُصبح فارغة.

---

# استخدام copy() لإنشاء نسخة من القائمة
# a = tecwindow_team.copy()
# print(a)  # ['mahmoud', 'hero', 'qais', 'ahmed', 'zozo']

# وظيفة copy():
# تُنشئ نسخة منفصلة من القائمة. التعديلات على النسخة الأصلية لا تؤثر على النسخة الجديدة.

---

# نسخ القائمة، ثم تعديل الأصل بإضافة عنصر جديد
# a = tecwindow_team.copy()
# tecwindow_team.append('perfect')
# print(a)  # ['mahmoud', 'hero', 'qais', 'ahmed', 'zozo']
# print(tecwindow_team)  # ['mahmoud', 'hero', 'qais', 'ahmed', 'zozo', 'perfect']

# وظيفة append():
# تضيف عنصرًا جديدًا إلى نهاية القائمة. 

# ملاحظة:
# النسخة `a` لم تتأثر بالتعديل لأن `copy()` تُنشئ نسخة منفصلة.

---

# قائمة جديدة تحتوي على أرقام مكررة
c = [1, 2, 1, 3, 1, 4, 5, 6, 2]

# استخدام count() لحساب عدد مرات ظهور العنصر "1" في القائمة
print(c.count(1))  # 3

# وظيفة count():
# تُرجع عدد مرات ظهور العنصر المحدد في القائمة.

---

# استخدام index() للحصول على موقع أول ظهور لعنصر معين
# print(tecwindow_team.index('perfect'))  # ValueError: 'perfect' is not in list
# print(tecwindow_team.index('ahmed'))  # 3

# وظيفة index():
# تُرجع الموقع (الفهرس) لأول ظهور للعنصر المطلوب.
# ملاحظة: إذا لم يكن العنصر موجودًا، فإنها تُظهر خطأ `ValueError`.

---

# استخدام insert() لإضافة عنصر في موقع معين
tecwindow_team.insert(1, 'perfect')
print(tecwindow_team)  
# ['mahmoud', 'perfect', 'hero', 'qais', 'ahmed', 'zozo']

# وظيفة insert():
# تضيف عنصرًا في موقع معين، وتقوم بإزاحة العناصر الأخرى.

---

# استخدام pop() لحذف العنصر الأخير من القائمة
print(tecwindow_team.pop(-1))  # 'zozo'
print(tecwindow_team)  
# ['mahmoud', 'perfect', 'hero', 'qais', 'ahmed']

# وظيفة pop():
# تُزيل وتُرجع العنصر الموجود في الموقع المحدد (افتراضيًا الأخير).
# إذا كانت القائمة فارغة، فإنها تُظهر خطأ `IndexError`.
