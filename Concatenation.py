# تعريف النصوص لإجراء عمليات عليها
msg ='hello Qais, and AHMED, and mahmoud'

# تحويل النص إلى حروف صغيرة (lowercase)
print(msg.lower())  # النتيجة: "hello qais, and ahmed, and mahmoud"

# تحويل النص إلى حروف كبيرة (uppercase)
print(msg.upper())  # النتيجة: "HELLO QAIS, AND AHMED, AND MAHMOUD"

# حساب طول النص
print(len(msg))  # النتيجة: 32 (عدد الحروف مع الفراغات)

# تعريف نصوص إضافية
one = 'ahmed'
two = 'bakr'
age = 25

# محاولة دمج النصوص باستخدام علامة +
print('hello'+one+two)  # النتيجة: "helloahmedbakr" (بدون مسافات)

# دمج النصوص مع إضافة مسافة واحدة بين hello و one
print('hello '+one+two)  # النتيجة: "hello ahmedbakr" (مسافة بعد hello فقط)

# دمج النصوص مع إضافة مسافات بين الكلمات
print('hello'+' '+one+' '+two)  # النتيجة: "hello ahmed bakr" (مسافات بين الكلمات)

# محاولة دمج نصوص مع عدد (متغير age)
# هذا السطر يحتوي على خطأ لأن المتغير age نوعه int، ولا يمكن دمجه مع نصوص مباشرة باستخدام علامة +
print('hello'+' '+one+' '+two+' your age is: '+ age)  
# النتيجة: 
# TypeError: can only concatenate str (not "int") to str