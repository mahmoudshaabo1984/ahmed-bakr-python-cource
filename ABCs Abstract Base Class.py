
# استيراد المكتبات الضرورية
from abc import ABC, abstractmethod  # لاستعمال الكلاسات المجردة (Abstract Classes)

# تعريف كلاس مجرد يمثل لغة برمجة (Programming Language)
class APCLanguage(ABC):
    def __init__(self, name):
        self.name = name  # اسم اللغة

    @abstractmethod
    def has_oop(self):
        # هل تدعم البرمجة الكائنية (OOP)?
        pass

    @abstractmethod
    def is_interpreted(self):
        # هل هي لغة مفسر (Interpreted)?
        pass

    @abstractmethod
    def is_compiled(self):
        # هل هي لغة مترجم (Compiled)?
        pass


# تعريف كلاس يمثل لغة Python
class Python(APCLanguage):
    def __init__(self):
        super().__init__("Python")  # استدعاء المُهيئ من الكلاس الأب

    def has_oop(self):
        return True  # بايثون تدعم OOP

    def is_interpreted(self):
        return True  # بايثون لغة مفسّرة

    def is_compiled(self):
        return False  # بايثون ليست مترجمة


# تعريف كلاس يمثل لغة Dart
class Dart(APCLanguage):
    def __init__(self):
        super().__init__("Dart")  # استدعاء المُهيئ من الكلاس الأب

    def has_oop(self):
        return True  # تدعم OOP

    def is_interpreted(self):
        return False  # ليست مفسّرة

    def is_compiled(self):
        return True  # مترجمة


# تعريف كلاس يمثل لغة PHP
class PHP(APCLanguage):
    def __init__(self):
        super().__init__("PHP")  # استدعاء المُهيئ من الكلاس الأب

    def has_oop(self):
        return True  # تدعم OOP

    def is_interpreted(self):
        return False  # ليست مفسّرة

    def is_compiled(self):
        return True  # مترجمة


# إنشاء قائمة من اللغات
langs = [Python(), Dart(), PHP()]

# عرض خصائص كل لغة
for lang in langs:
    print(f"Language: {lang.name}")
    print(f"  Has OOP: {lang.has_oop()}")           # هل تدعم OOP
    print(f"  Is Interpreted: {lang.is_interpreted()}")  # هل مفسّرة
    print(f"  Is Compiled: {lang.is_compiled()}")        # هل مترجمة
    print("-" * 30)  # فاصل بين اللغات
