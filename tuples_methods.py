# تعريف مجموعة من النصوص بدون أقواس (تُعتبر Tuple)
a = 'ahmed', 'ahmed', 'bakr'
print(a)  # النتيجة: ('ahmed', 'ahmed', 'bakr')
print(type(a))  # النتيجة: <class 'tuple'>

---

# تعريف Tuple باستخدام الأقواس العادية
b = ('ahmed', 'ahmed', 'bakr')
print(b)  # النتيجة: ('ahmed', 'ahmed', 'bakr')
print(type(b))  # النتيجة: <class 'tuple'>

---

# تعريف Tuple بعنصر واحد مع فاصلة
c = 'ahmed',
print(c)  # النتيجة: ('ahmed',)
print(type(c))  # النتيجة: <class 'tuple'>
print(len(c))  # النتيجة: 1 (طول الـ Tuple)

---

# الوصول إلى العناصر باستخدام الفهرسة والتقطيع
a = 'a', 'b', 'c', 'd', 'f'
print(a[1])  # النتيجة: 'b' (العنصر في الموقع 1)
print(a[-1])  # النتيجة: 'f' (العنصر الأخير)
print(a[0:3])  # النتيجة: ('a', 'b', 'c') (عناصر من الموقع 0 إلى 2)

---

# محاولة تعديل عنصر داخل Tuple
a = 'a', 'b', 'c', 'd', 'f'
a[0] = '1'  # TypeError: 'tuple' object does not support item assignment
print(a)
# المجموعات Tuple غير قابلة للتغيير (Immutable)، لذا لا يمكن تعديل عناصرها.

---

# تكرار النصوص والقوائم والـ Tuple
my_str = 'ahmedbakr'
my_list = ['ahmed', 'bakr']
my_tuple = ('ahmed', 'bakr')

print(my_str * 5)  # تكرار النص 5 مرات
print(my_list * 5)  # تكرار عناصر القائمة 5 مرات
print(my_tuple * 5)  # تكرار عناصر الـ Tuple 5 مرات

---

# تفكيك الـ Tuple إلى متغيرات
a, b, c = 'ahmed', 'bakr', 'perfect'
print(a)  # النتيجة: 'ahmed'
print(b)  # النتيجة: 'bakr'
print(c)  # النتيجة: 'perfect'

---

# محاولة تفكيك Tuple تحتوي على عناصر أكثر من المتغيرات المعرّفة
a, b, c = ('ahmed', 'bakr', 'perfect', 'qais')  # ValueError: too many values to unpack (expected 3)
print(a)
print(b)
print(c)

---

# استخدام `_` لتجاهل عنصر أثناء التفكيك
a, b, _, c = ('ahmed', 'bakr', 'perfect', 'qais')
print(a)  # النتيجة: 'ahmed'
print(b)  # النتيجة: 'bakr'
print(c)  # النتيجة: 'qais'

# الرمز `_` يُستخدم لتجاهل القيم التي لا نحتاج إليها.