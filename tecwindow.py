




# هذا الكود يستورد مكتبة random لاستخدام وظائف توليد الأرقام العشوائية
# الدالة say_hello تأخذ اسمًا وتطبع ترحيبًا بسيطًا باستخدام ذلك الاسم
# الدالة say_hi تأخذ اسمًا وتطبع تحية رسمية مع كلمة "mr" قبل الاسم
# الدالة show_random_num تطبع عددًا عشَواءيًا بين 0 و 1 باستخدام random.random()

import random

def say_hello(name):
    print(f"hello {name}")

def say_hi(name):
    print(f"hi mr {name}")

def show_random_num():
    print(random.random())
    print(random.randint(10, 600))
