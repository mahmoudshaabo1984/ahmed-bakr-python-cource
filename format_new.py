# تعريف المتغيرات
name = 'MesterPerfect'
age = 25
rank = 10

# التنسيق باستخدام الطريقة القديمة (%)
# طباعة النصوص باستخدام التنسيق القديم (Placeholder Formatting)
print('my name is: %s and my age is: %d and rank is: %f' % (name, age, rank))
# النتيجة: my name is: MesterPerfect and my age is: 25 and rank is: 10.000000
# %s: لتنسيق النصوص.
# %d: لتنسيق الأعداد الصحيحة.
# %f: لتنسيق الأعداد العشرية.

# تحديد عدد الأحرف والكسور عند الطباعة
print('my name is: %.6s and my age is: %d and rank is: %.1f' % (name, age, rank))
# النتيجة: my name is: Mester and my age is: 25 and rank is: 10.0
# %.6s: طباعة أول 6 أحرف من النص.
# %.1f: طباعة العدد العشري مع خانة عشرية واحدة فقط.

# التنسيق باستخدام `format()` (طريقة أحدث)
print('my name is: {} and my age is: {} and my rank is: {}'.format(name, age, rank))
# النتيجة: my name is: MesterPerfect and my age is: 25 and my rank is: 10

# إضافة نوع التنسيق داخل أقواس `format`
print('my name is: {:s} and my age is: {:d} and my rank is: {:f}'.format(name, age, rank))
# النتيجة: my name is: MesterPerfect and my age is: 25 and my rank is: 10.000000

# تحديد عدد الأحرف والكسور
print('my name is: {:.6s} and my age is: {:d} and my rank is: {:.1f}'.format(name, age, rank))
# النتيجة: my name is: Mester and my age is: 25 and my rank is: 10.0

# تغيير ترتيب العناصر أثناء الطباعة
print('my rank is: {} and my name is: {} and my age is: {}'.format(name, age, rank))
# النتيجة: my rank is: MesterPerfect and my name is: 25 and my age is: 10

# استخدام المواقع (Positional Indexing)
print('my rank is: {2} and my name is: {0} and my age is: {1}'.format(name, age, rank))
# النتيجة: my rank is: 10 and my name is: MesterPerfect and my age is: 25

# تحديد نوع التنسيق مع المواقع
print('my rank is: {2:f} and my name is: {0:s} and my age is: {1:d}'.format(name, age, rank))
# النتيجة: my rank is: 10.000000 and my name is: MesterPerfect and my age is: 25

# تحديد عدد الأحرف والكسور مع المواقع
print('my rank is: {2:.2f} and my name is: {0:.6s} and my age is: {1:d}'.format(name, age, rank))
# النتيجة: my rank is: 10.00 and my name is: Mester and my age is: 25

# التنسيق مع الأرقام الكبيرة
test = 56532448786

# استخدام الفواصل بين الأرقام
print('my test num is: {:,d}'.format(test))
# النتيجة: my test num is: 56,532,448,786
# {:,d}: يُضيف فاصلة لكل 3 أرقام.

# محاولة استخدام تنسيق غير صحيح (سيؤدي إلى خطأ)
# print('my test num is: {:$d}'.format(test))
# النتيجة: ValueError: Invalid format specifier '$d' for object of type 'int'

# التنسيق باستخدام `f-strings` (أحدث طريقة)
print(f'name is: {name} and age is: {age} and rank is: {rank}')
# النتيجة: name is: MesterPerfect and age is: 25 and rank is: 10
# f-strings: تُستخدم لإدخال القيم مباشرة داخل النص باستخدام الأقواس `{}`.