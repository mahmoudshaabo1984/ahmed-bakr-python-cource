# تعريف الكلاس الأب "bakr"
class bakr:
    def __init__(self, name, age):
        self.name = name  # تخزين الاسم كخاصية في الكائن
        self.age = age  # تخزين العمر كخاصية في الكائن
        print(f'تم إنشاء كائن من الكلاس الأب bakr')
        print(f'إسمي هو: {self.name}، وعمري هو: {self.age} عاما')

    # دالة لطباعة رسالة خاصة بالكلاس الأب
    def fullName(self):
        print('أهلا بكم في دالة الكلاس الأب')


# تعريف الكلاس الابن "ahmed" الذي يرث من الكلاس "bakr"
class ahmed(bakr):
    def __init__(self, name, age, website):
        # استدعاء المُنشئ الخاص بالكلاس الأب لتوريث "name" و "age"
        super().__init__(name, age)  
        
        # إضافة خاصية جديدة خاصة بالكلاس الابن
        self.web = website  
        
        print(f'تم إنشاء كائن من الكلاس الابن ahmed')
        print(f'إسمي هو: {self.name}، وعمري هو: {self.age} عاما. وموقعي الشخصي هو {self.web}')

    # إعادة تعريف دالة "fullName" الموجودة في الكلاس الأب (Method Overriding)
    def fullName(self):
        print('أهلا بكم في دالة الكلاس الابن')


# إنشاء كائن من الكلاس الأب "bakr"
name1 = bakr('بكر', '61')

# إنشاء كائن من الكلاس الابن "ahmed"
name2 = ahmed('أحمد', '25', 'https://tecwindow.net')

# استدعاء الدالة "fullName" من كل كائن
name1.fullName()  # سيتم تنفيذ الدالة من الكلاس الأب
name2.fullName()  # سيتم تنفيذ الدالة من الكلاس الابن بسبب إعادة التعريف (Overriding)
