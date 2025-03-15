"""
مفهوم البرمجة الكائنية التوجه (OOP) في بايثون

البرمجة الكائنية التوجه (OOP - Object Oriented Programming) هي نموذج برمجي يُستخدم لتنظيم الكود بشكل يعتمد على الكائنات (Objects). 
كل كائن يحتوي على بيانات (تُعرف بالمتغيرات أو الخصائص) وسلوكيات (تُعرف بالدوال أو الوظائف).

1. **الفئات (Classes)**:
   - الفئة هي القالب أو المخطط الذي نُنشئ منه الكائنات.
   - يتم تعريف الفئات باستخدام الكلمة المفتاحية `class`.

2. **الكائنات (Objects)**:
   - الكائن هو نسخة (Instance) من الفئة، يتم إنشاؤه باستخدام المُنشئ `__init__`.
   - يمكن أن يحتوي على بيانات خاصة به ويستدعي الوظائف المحددة داخل الفئة.

3. **المُنشئ (Constructor)**:
   - هو دالة تُسمى `__init__` تُستخدم لتهيئة الكائنات عند إنشائها.

4. **الخصائص (Attributes)**:
   - هي البيانات المخزنة داخل الكائن، مثل الاسم الأول، الاسم الأوسط، اللقب والجنس.

5. **الوظائف (Methods)**:
   - هي السلوكيات التي يمكن للكائن تنفيذها، مثل إرجاع الاسم الكامل أو تحية المستخدم.

6. **القيم الافتراضية (Default Values)**:
   - يمكن تحديد قيم افتراضية للخصائص في حال لم يتم تمريرها عند إنشاء الكائن.

7. **استخدام الفئة في الحياة العملية**:
   - تُستخدم الفئات لإنشاء برامج قابلة لإعادة الاستخدام.
   - يُفضل استخدامها لتنظيم البيانات والتعامل مع المستخدمين بشكل أكثر كفاءة.
"""

class SiteMembers:
    """
    فئة تمثل أعضاء الموقع، تحتوي على الاسم الأول، الاسم الأوسط، اللقب والجنس.
    """
    def __init__(self, fname, mname, lname, gender="unknown"):
        """
        المُنشئ (Constructor): يهيئ البيانات الخاصة بكل كائن جديد من الفئة.
        - fname: الاسم الأول
        - mname: الاسم الأوسط
        - lname: اللقب
        - gender: الجنس (male أو female أو unknown كافتراضي)
        """
        self.firstName = fname
        self.middleName = mname
        self.lastName = lname
        self.gender = gender.lower()  # جعل القيمة غير حساسة لحالة الأحرف

    def FullName(self):
        """
        دالة تعيد الاسم الكامل للمستخدم.
        """
        return f"{self.firstName} {self.middleName} {self.lastName}"

    def HelloUser(self):
        """
        دالة ترحب بالمستخدم بناءً على جنسه.
        """
        if self.gender == "male":
            return f"أهلا بك يا أستاذ: {self.firstName}"
        elif self.gender == "female":
            return f"أهلا بكِ يا أستاذة: {self.firstName}"
        else:
            return f"Hello {self.firstName}"

    def GetFullInfo(self):
        """
        دالة تعرض معلومات كاملة عن المستخدم.
        """
        return f'{self.HelloUser()} اسمك الثلاثي هو {self.FullName()}'

# إنشاء الكائنات
member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
member4 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
member2 = SiteMembers('يوسف', 'بكر', 'محمد')  # يستخدم القيمة الافتراضية لـ gender
member3 = SiteMembers('منذر', 'بكر', 'محمد')  # يستخدم القيمة الافتراضية لـ gender

# طباعة نتائج الترحيب
print(member1.HelloUser())  # أهلا بك يا أستاذ: أحمد
print(member4.HelloUser())  # أهلا بكِ يا أستاذة: زينب

# طباعة المعلومات الكاملة
print(member1.GetFullInfo())  # أهلا بك يا أستاذ: أحمد اسمك الثلاثي هو أحمد بكر محمد
print(member4.GetFullInfo())  # أهلا بكِ يا أستاذة: زينب اسمك الثلاثي هو زينب محمد بهاء
