# تعريف كلاس يسمى Member
class Member:
    def __init__(self, name):
        self.__name = name  # تعريف متغير خاص (private) لا يمكن الوصول له مباشرة من خارج الكلاس

    def hello(self):
        # دالة ترجع رسالة ترحيب باستخدام الاسم الخاص
        return f"hello {self.__name}"

    def get_name(self):  # getter
        # هذه الدالة تُستخدم للوصول إلى قيمة المتغير الخاص __name
        return self.__name

    def set_name(self, new_name):  # setter
        # هذه الدالة تُستخدم لتغيير قيمة المتغير الخاص __name
        self.__name = new_name


# إنشاء كائن من الكلاس وإعطاؤه اسم "ahmed"
one = Member("ahmed")

# طباعة الاسم باستخدام الدالة getter
print(one.get_name())  # الناتج: ahmed

# تغيير الاسم باستخدام الدالة setter
one.set_name("MesterPerfect)")
print(one.get_name())  # الناتج: MesterPerfect)

# يمكننا أيضًا استخدام دالة hello التي ترجع رسالة
# print(one.hello())  # سترجع: hello MesterPerfect)
