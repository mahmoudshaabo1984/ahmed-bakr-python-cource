# تعريف كلاس باسم Member
class Member:
    def __init__(self, name, age):
        self.name = name  # متغير عام لحفظ الاسم
        self.age = age    # متغير عام لحفظ العمر

    def say_hello(self, message):
        # دالة تأخذ رسالة وتضيفها كمتغير للكائن ثم ترجع رسالة ترحيب
        self.message = message
        return f"hello {self.name}, {self.message}"

    @property
    def age_in_days(self):
        # هذه الدالة تحسب العمر بالأيام وتُستخدم كخاصية بفضل @property
        return self.age * 365


# إنشاء كائن من الكلاس Member ونعطيه الاسم والعمر
one = Member("ahmed", 25)

# طباعة الاسم مباشرة لأنه متغير عام (public)
print(one.name)  # ahmed

# طباعة العمر مباشرة لأنه أيضًا متغير عام
print(one.age)   # 25

# استدعاء دالة say_hello مع رسالة
print(one.say_hello("i love python"))  
# الناتج: hello ahmed, i love python

# استخدام الخاصية age_in_days كأنها متغير، رغم أنها دالة
print(one.age_in_days)  
# الناتج: 9125 (أي 25 سنة × 365 يوم)
