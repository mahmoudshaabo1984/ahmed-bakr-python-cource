# تعريف الكلاس الأول (الأب الأول)
class One:
    def __init__(self):
        print('أهلا بك في Class 1')

    def function_one(self):
        print('hello one من الكلاس الرئيسي')


# تعريف الكلاس الثاني (الأب الثاني)
class Two(One):  # يرث من "One"
    def __init__(self):
        super().__init__()  # استدعاء المُنشئ الخاص بالكلاس الأب "One"
        print('أهلا بك في Class 2')

    def function_two(self):
        print('hello two بعد أن تم التوريث من الكلاس الأول')


# تعريف الكلاس الابن "Ahmed" الذي يرث من "Two"
class Ahmed(Two):
    def __init__(self):
        super().__init__()  # استدعاء المُنشئ الخاص بالكلاس الأب "Two"
        print('أهلا بك في Class 3 (Ahmed)')

    # إعادة تعريف الدالة function_one من "One"
    def function_one(self):
        print('hello one تم إعادة تعريفها في الكلاس Ahmed')


# إنشاء كائن من الكلاس الابن "Ahmed"
name = Ahmed()

# استدعاء الدوال من الكائن
name.function_one()  # ستعمل النسخة المعاد تعريفها من Ahmed
name.function_two()  # ستعمل من "Two"

# طباعة ترتيب البحث عن الدوال (Method Resolution Order)
print(Ahmed.mro())  
