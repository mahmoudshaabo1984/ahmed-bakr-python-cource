# تعريف مجموعتين a و b
a = {'a', 'b', 'c', 'd', 'f', True}  # المجموعة a تحتوي على حروف وقيمة منطقية True
b = {'a', 'b', 'c'}                 # المجموعة b تحتوي على مجموعة فرعية من a

# استخدام difference() لإيجاد الفرق بين المجموعتين
print(a.difference(b))  # النتيجة: {'f', 'd'}
# الفرق بين a و b: العناصر الموجودة في a ولكن ليست في b.

# استخدام الطرح المباشر (-) لإيجاد الفرق بين المجموعتين
print(a - b)  # النتيجة: {'f', 'd'}
# الفرق يتم حسابه بنفس طريقة difference().

# ---

# استخدام difference_update() لتحديث المجموعة a بإزالة العناصر المشتركة مع b
a = {'a', 'b', 'c', 'd', 'f', True}
b = {'a', 'b', 'c'}
print(a)  # قبل التحديث: {'a', 'b', 'c', 'd', 'f', True}
a.difference_update(b)
print(a)  # بعد التحديث: {'f', 'd'}
# وظيفة difference_update():
# تُزيل العناصر الموجودة في b من a وتحدث a مباشرة.

# ---

# استخدام intersection() لإيجاد العناصر المشتركة بين المجموعتين
a = {'a', 'b', 'c', 'd', 'f', True}
b = {'a', 'b', 'c'}
print(a)  # المجموعة a قبل العملية
print(a.intersection(b))  # النتيجة: {'a', 'b', 'c'}
# العناصر المشتركة بين a و b هي {'a', 'b', 'c'}.
print(a)  # المجموعة a لم تتغير لأن intersection() لا تعدّلها مباشرة.

# ---

# استخدام intersection_update() لتحديث a بالعناصر المشتركة مع b
a = {'a', 'b', 'c', 'd', 'f', True}
b = {'a', 'b', 'c'}
print(a)  # قبل التحديث: {'a', 'b', 'c', 'd', 'f', True}
a.intersection_update(b)
print(a)  # بعد التحديث: {'a', 'b', 'c'}
# وظيفة intersection_update():
# تُبقي فقط العناصر المشتركة بين a و b داخل a.

# ---

# استخدام symmetric_difference() لإيجاد العناصر غير المشتركة بين المجموعتين
a = {'a', 'b', 'c', 'd', 'f', True}
b = {'a', 'b', 'c'}
print(a)  # المجموعة a قبل العملية
print(a.symmetric_difference(b))  # النتيجة: {'d', 'f'}
# العناصر غير المشتركة بين a و b هي {'d', 'f'}.
print(a)  # المجموعة a لم تتغير لأن symmetric_difference() لا تعدّلها مباشرة.

# ---

# استخدام symmetric_difference_update() لتحديث a بالعناصر غير المشتركة مع b
a = {'a', 'b', 'c', 'd', 'f', True}
b = {'a', 'b', 'c'}
print(a)  # قبل التحديث: {'a', 'b', 'c', 'd', 'f', True}
a.symmetric_difference_update(b)
print(a)  # بعد التحديث: {'d', 'f'}
# وظيفة symmetric_difference_update():
# تُبقي فقط العناصر غير المشتركة بين a و b داخل a.
