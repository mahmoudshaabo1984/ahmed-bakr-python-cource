# تعريف نص يحتوي على كلمات مفصولة بمسافات
a = 'i love python and php and mySQL'

# طباعة النص كما هو
print(a)  # النتيجة: i love python and php and mySQL

# تقسيم النص إلى قائمة بناءً على المسافات الافتراضية
print(a.split())  # النتيجة: ['i', 'love', 'python', 'and', 'php', 'and', 'mySQL']

# طباعة نوع البيانات الناتجة عن تقسيم النص
print(type(a.split()))  # النتيجة: <class 'list'>

---

# تعريف نص مشابه للنص الأول
b = 'i love python and php and mySQL'

# تقسيم النص إلى ثلاثة أجزاء فقط باستخدام العدد 2 كحد أقصى
print(b.split(' ', 2))  # النتيجة: ['i', 'love', 'python and php and mySQL']

---

# تعريف نص يحتوي على كلمات مفصولة بشرطة "-"
c = 'i-love-python-and php-and mySQL'

# تقسيم النص إلى قائمة بناءً على الشرطة "-"
print(c.split('-'))  # النتيجة: ['i', 'love', 'python', 'and php', 'and mySQL']

# محاولة تقسيم النص باستخدام rsplit مع حد معين (سيؤدي إلى خطأ بسبب وجود إشارة غير صحيحة)
# print(c.rsplit('-, 2'))  # ستسبب خطأ SyntaxError بسبب كتابة السطر بشكل غير صحيح.

# محاولة إزالة أحرف محددة من البداية باستخدام lstrip
# print(c.lstrip('-, 2'))  # ستقوم بإزالة الأحرف المحددة ('-', ' ', '2') من بداية النص.

---

# تعريف نص جديد
d = 'MesterPerfect'

# ضبط النص في منتصف سطر طوله 25 مع استخدام المسافات
print(d.center(25))  # النتيجة: "       MesterPerfect       "

# ضبط النص في منتصف سطر طوله 25 مع استخدام الرمز "#"
print(d.center(25, '#'))  # النتيجة: "#######MesterPerfect#######"

---

# نص يحتوي على كلمة مكررة
e = 'i love python, python is Very easy'

# حساب عدد مرات ظهور كلمة "python" في النص بالكامل
print(e.count('python'))  # النتيجة: 2

# حساب عدد مرات ظهور كلمة "python" في نطاق معين من النص
print(e.count('python', 1, 19))  # النتيجة: 1

---

# نص للتحويل بين الأحرف الكبيرة والصغيرة
f = 'i love python, python is Very easy'

# تبديل حالة الأحرف: الحروف الصغيرة تصبح كبيرة والعكس صحيح
print(f.swapcase())  # النتيجة: "I LOVE PYTHON, PYTHON IS vERY EASY"

---

# نص مشابه للتبديل بين الحالات
g = 'I loVe python, pythoN is Very easy'

# تبديل حالة الأحرف للنص الجديد
print(g.swapcase())  # النتيجة: "i LOvE PYTHON, PYTHOn IS vERY EASY"

---

# نص للتحقق من بداية النصوص
h = 'i love python, python is Very easy'

# التحقق مما إذا كان النص يبدأ بـ 'i   ' (يأخذ المسافات بعين الاعتبار)
print(h.startswith('i   '))  # النتيجة: False

# التحقق مما إذا كان النص يبدأ بـ 'p'
print(h.startswith('p'))  # النتيجة: False

# التحقق مما إذا كانت الأحرف بين المواقع 7 و15 تبدأ بـ 'p'
print(h.startswith('p', 7, 15))  # النتيجة: True

---

# نص للتحقق من نهاية النصوص
i = 'i love python, python is Very easy'

# التحقق مما إذا كان النص ينتهي بحرف 'y'
print(i.endswith('y'))  # النتيجة: True

# التحقق مما إذا كان النص ينتهي بحرف 'p'
print(i.endswith('p'))  # النتيجة: False

# التحقق مما إذا كانت الأحرف بين المواقع 1 و6 تنتهي بـ 'e'
print(i.endswith('e', 1, 6))  # النتيجة: True
