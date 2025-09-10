# كلاس أساسي يحتوي على متغير محمي
class Person:
    def __init__(self, name):
        self._name = name  # هذا متغير محمي

    def show(self):
        return f"My name is {self._name}"


# كلاس فرعي يرث من Person
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # استدعاء مُهيئ الكلاس الأساسي
        self.student_id = student_id

    def introduce(self):
        # يمكن الوصول للمتغير المحمي _name من داخل الكلاس المشتق
        return f"I am {self._name} and my ID is {self.student_id}"


# إنشاء كائن من الكلاس Student
std = Student("Ahmed", 1234)

# استخدام الدوال التي تعرض معلومات المتغير المحمي
print(std.show())        # من الكلاس الأساسي
print(std.introduce())   # من الكلاس المشتق

# رغم أنه يمكن الوصول للمتغير المحمي من الخارج، يُفضل عدم فعل ذلك مباشرة
print(std._name)  # تقنيًا مسموح، لكن يُعتبر غير مستحب حسب أسلوب كتابة بايثون (convention)
