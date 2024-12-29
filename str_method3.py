# نص يحتوي على كلمة "python" مكررة
a = 'i love python, because python is very easy'

# العثور على موقع أول حرف 'p' في النص
print(a.index('p'))  # النتيجة: 7

# العثور على موقع 'p' بين الموقعين 4 و10
print(a.index('p', 4, 10))  # النتيجة: 7

# محاولة العثور على 'p' بين الموقعين 8 و10 (لا يوجد)
# هذا السطر سيؤدي إلى خطأ لأنه لا توجد 'p' في هذا النطاق.
# print(a.index('p', 8, 10))  
# النتيجة: 
# ValueError: substring not found

---

# نص مشابه للنص الأول
b = 'i love python, because python is very easy'

# العثور على موقع أول حرف 'p' باستخدام find
print(b.find('p'))  # النتيجة: 7

# العثور على موقع 'p' بين الموقعين 4 و10
print(b.find('p', 4, 10))  # النتيجة: 7

# محاولة العثور على 'p' بين الموقعين 8 و10
# إذا لم توجد الكلمة، فإن find تُرجع -1 بدلاً من رفع خطأ.
print(b.find('p', 8, 10))  # النتيجة: -1

---

# نص لاختبار المحاذاة إلى اليسار
c = 'MesterPerfect'

# محاذاة النص إلى اليسار ضمن مساحة طولها 25 وإضافة مسافات في النهاية
print(c.ljust(25))  # النتيجة: "MesterPerfect            "

# محاذاة النص إلى اليسار ضمن مساحة طولها 25 وإضافة '@' بدلاً من المسافات
print(c.ljust(25, '@'))  # النتيجة: "MesterPerfect@@@@@@@@@@@"

---

# نص لاختبار المحاذاة إلى اليمين
d = 'MesterPerfect'

# محاذاة النص إلى اليمين ضمن مساحة طولها 25 وإضافة مسافات في البداية
print(d.rjust(25))  # النتيجة: "            MesterPerfect"

# محاذاة النص إلى اليمين ضمن مساحة طولها 25 وإضافة '#' بدلاً من المسافات
print(d.rjust(25, '#'))  # النتيجة: "############MesterPerfect"

---

# نص يحتوي على كلمة "one" مكررة
f = 'hello one two one for one'

# استبدال جميع الكلمات "one" بـ "1"
print(f.replace('one', '1'))  # النتيجة: "hello 1 two 1 for 1"

# استبدال أول ظهور فقط لـ "one" بـ "1"
print(f.replace('one', '1', 1))  # النتيجة: "hello 1 two one for one"

---

# قائمة بأسماء أعضاء فريق TecWindow
tecwindow_team = ['zozo', 'ahmed', 'qais', 'mahmoud', 'hero']

# دمج القائمة باستخدام الشرطة "-"
print('-'.join(tecwindow_team))  # النتيجة: "zozo-ahmed-qais-mahmoud-hero"

# دمج القائمة باستخدام مسافة " "
print(' '.join(tecwindow_team))  # النتيجة: "zozo ahmed qais mahmoud hero"
