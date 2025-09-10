# public - الأعضاء العامة يمكن الوصول إليها من خارج الكلاس
# private - الأعضاء الخاصة لا يمكن الوصول إليها أو رؤيتها من خارج الكلاس مباشرة
# protected - الأعضاء المحمية لا يمكن الوصول إليها من خارج الكلاس، 
#             لكن يمكن الوصول إليها من الكلاسات المشتقة (التي ترث من هذا الكلاس)

# ------------------------
# مثال على public

class Member:
    def __init__(self, name):
        self.name = name  # هذا العضو public

one = Member("ahmed")
print(one.name)  # يمكن الوصول مباشرة إلى الاسم

one.name = "perfect"  # يمكن تغييره أيضًا
print(one.name)

# ------------------------
# مثال على protected

class Member:
    def __init__(self, name):
        self._name = name  # ملاحظة: الشرطة السفلية الواحدة تعني protected

one = Member("ahmed")
print(one._name)  # يمكن الوصول له، لكن من الأفضل عدم استخدامه خارج الكلاس حسب الاتفاق

one._name = "perfect"
print(one._name)

# ------------------------
# مثال على private

class Member:
    def __init__(self, name):
        self.__name = name  # شرطتان سفليتان تعني أن العضو private

    def hello(self):
        return f"hello {self.__name}"  # يمكن الوصول للعضو من داخل الكلاس فقط

one = Member("ahmed")
print(one.hello())  # يتم الوصول للاسم عبر دالة داخل الكلاس

# print(one.__name)  # هذا السطر يعطي خطأ لأنه لا يمكن الوصول للاسم مباشرة من الخارج
