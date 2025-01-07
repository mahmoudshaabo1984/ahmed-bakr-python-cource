# تعريف المتغيرات 
# -----------------
# يتم استخدام هذه المتغيرات في جميع الأمثلة لتخصيص الرسائل والخصومات بناءً على بيانات المستخدم
uName = input("Enter Your Name : ")  # اسم المستخدم
uCountry = input("Enter Your Country : ")  # دولة المستخدم
jender = input("Enter Your jender : ")  # جنس المستخدم (ذكر أو أنثى)
cName = "python course"  # اسم الدورة التدريبية
cPrice = 100  # السعر الأساسي للدورة
adminsList = ['ahmed', 'zeinab', 'qais', 'perfect', 'mahmoud']  # قائمة المديرين

# المثال الأول
# -----------------
# خصائص: طباعة رسالة عامة بغض النظر عن الدولة أو الجنس.
print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice}')

# المثال الثاني
# -----------------
# استخدام if الشرطية البسيطة
# خصائص: إذا كانت الدولة هي "egypt"، يتم تطبيق خصم 90 دولارًا.
if uCountry == "egypt":
    print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice - 90}')

# المثال الثالث
# -----------------
# خصائص: إضافة شرط "else" لتحديد السعر الكامل في حالة عدم انطباق الشرط الأول.
if uCountry == "egypt":
    print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice - 90}')
else: 
    print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice}')

# المثال الرابع
# -----------------
# خصائص: تطبيق خصومات مختلفة حسب الدولة باستخدام "elif".
if uCountry == "egypt":
    print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice - 90}')
elif uCountry == "ksa":
    print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice - 50}')
elif uCountry == "usaa":
    print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice - 20}')
else: 
    print(f'hello {uName} Because u r from {uCountry} the course "{cName}" price is: ${cPrice}')

# المثال الخامس
# -----------------
# استخدام if المتداخلة nested if
# خصائص: تخصيص الرسالة بناءً على الدولة والجنس باستخدام "if" و"elif" متداخلة.
if uCountry == "egypt":
    if jender == "male":
        print(f"Hello MR {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')
    elif jender == "female":
        print(f"Hello ms {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')

elif uCountry == "ksa":
    if jender == "male":
        print(f"Hello MR {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')
    elif jender == "female":
        print(f"Hello ms {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')

elif uCountry == "usa":
    if jender == "male":
        print(f"Hello MR {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')
    elif jender == "female":
        print(f"Hello ms {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')

else:
    print(f'Hello {uName} The Course "{cName}" Price is: ${cPrice}')

# المثال السادس
# -----------------
# استخدام Boolean Operators مع nested if 
if uCountry == "egypt":
    if jender == "male" or jender == 'm':
        print(f"Hello MR {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')
    elif jender == "female" or jender == 'f':
        print(f"Hello ms {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')

elif uCountry == "ksa":
    if jender == "male" or jender == 'm':
        print(f"Hello MR {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')
    elif jender == "female" or jender == 'f':
        print(f"Hello ms {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')

elif uCountry == "usa":
    if jender == "male" or jender == 'm':
        print(f"Hello MR {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')
    elif jender == "female" or jender == 'f':
        print(f"Hello ms {uName} Because You Are From {uCountry}")
        print(f'The Course "{cName}" Price Is: ${cPrice - 80}')

else:
    print(f'Hello {uName} The Course "{cName}" Price is: ${cPrice}')

# المثال السابع
# -----------------
# استخدام Membership Operators مع if الشرطية 
if uName in adminsList:
    print(f'Hello Mr. {uName}, you are from the management team.')
else:
    print(f'Hello Mr. {uName}, you are user.')