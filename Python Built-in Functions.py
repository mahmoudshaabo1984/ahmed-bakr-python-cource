# تعريف قائمة تحتوي على صفر وقائمة فارغة
num = [0, []]

# الدالة all() تعود True فقط إذا كانت كل العناصر قيمتها True
if all(num):
    print("All elements are True")
else:
    print("All elements are not True")  # هذا الشرط سيتحقق لأن 0 والقائمة الفارغة تعتبر False

# الدالة any() تعود True إذا كان هناك على الأقل عنصر واحد قيمته True
if any(num):
    print("لديك عنصر واحد صحيح على الأقل")  # ستتم طباعة هذا لأن القائمة الفارغة ليست False تمامًا
else:
    print("All elements are not True")

# تحويل الأرقام إلى النظام الثنائي باستخدام bin()
print(bin(1))  # 0b1
print(bin(100))  # 0b1100100

# استخدام id() للحصول على عنوان الذاكرة لمتغيرين
a = 20
b = 30
print(id(a))  # طباعة عنوان المتغير a في الذاكرة
print(id(b))  # طباعة عنوان المتغير b في الذاكرة

# إنشاء قائمة باستخدام range()
print(list(range(10)))  # إنشاء قائمة من 0 إلى 9
print(list(range(5, 20, 3)))  # إنشاء قائمة تبدأ من 5 حتى أقل من 20 بزيادة 3 في كل مرة

# استخدام معامل end في print لمنع الانتقال لسطر جديد
print('hello ahmed', 'how r u', end='#######')
print('hello ahmed', 'how r u')  # سيظهر النص في نفس السطر بسبب end

# حساب مجموع الأرقام في قائمة
# تحتوي القائمة على أرقام ونص، مما سيؤدي إلى خطأ عند محاولة جمعها
#a = [5, 8, 11, 14, 17, 'ahmed']
#print(sum(a))  # هذا سيؤدي إلى خطأ لأن النص لا يمكن جمعه مع الأرقام
#print(sum(a, 45))  # هذا أيضًا سيؤدي إلى خطأ لنفس السبب

# العمليات الرياضية باستخدام ** و pow()
print(2 ** 5)  # 32 - رفع 2 للقوة 5
print(pow(2, 5))  # 32 - نفس النتيجة باستخدام pow()
print(pow(2, 5, 3))  # 2 - نفس العملية ولكن مع باقي القسمة على 3

# إيجاد الحد الأدنى والأقصى في القوائم
a = [1, 50, 60, 70, 100, 1000, 200]
b = ['bakr', 'a', 'b', 'z', 'ي']
print(min(a))  # أصغر عدد في القائمة a
print(min(b))  # أصغر قيمة في القائمة b حسب الترتيب الأبجدي
print(max(a))  # أكبر عدد في القائمة a
print(max(b))  # أكبر قيمة في القائمة b حسب الترتيب الأبجدي

# استخدام map() لتنسيق النصوص

def textFormat(text):
    return f'# {text.capitalize()} #'

tecwindowTeam = ['mahmoud', 'qais', 'ahmed', 'hero']
myData = map(textFormat, tecwindowTeam)
for name in myData:
    print(name)  # طباعة الأسماء بعد تنسيقها

# استخدام filter() لتصفية البيانات

def myNum(num):
    return num == 100  # ترجع True فقط إذا كان الرقم 100

data = [10, 50, 7, 4, 3, 70, 90, 60, 100]
myNumData = filter(myNum, data)
for x in myNumData:
    print(x)  # سيطبع فقط الرقم 100 لأنه الوحيد الذي يحقق الشرط

# تصفية الأسماء التي تبدأ بحرف 'a'

def myStr(data):
    return data.startswith('a')

names = ['Ahmed', 'ali', 'amer']
myStrData = filter(myStr, names)
for x in myStrData:
    print(x)  # سيطبع الأسماء التي تبدأ بحرف 'a'

# تصفية الأرقام التي تساوي 10 فقط

def myData(data):
    return data == 10

myNum = [1, 5, 6, 2, 10, 100, 200]
dataNum = filter(myData, myNum)
for x in dataNum:
    print(x)  # سيطبع فقط الرقم 10 لأنه الوحيد الذي يحقق الشرط
