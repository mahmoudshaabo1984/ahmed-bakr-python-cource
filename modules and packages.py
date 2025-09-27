# استخدام الموديول المدمج random بطرق مختلفة

# استيراد الموديول بالكامل
import random
print(random.random())        # بيرجع رقم عشـوائي بين 0 و 1
print(random.randint(10, 600))# بيرجع رقم صحيح عشـوائي بين 10 و 600

# استيراد دوال معينة فقط من الموديول
from random import random as rand_func, randint
print(rand_func())            # رقم عشـوائي بين 0 و 1 بدون اسم الموديول
print(randint(10, 600))       # رقم عشـوائي بين 10 و 600

# استيراد الموديول باسم مختصر
import random as rm
print(rm.random())            # رقم عشـوائي بين 0 و 1
print(rm.randint(10, 600))    # رقم عشـوائي بين 10 و 600

# استخدام موديول مخصص بإسم tecwindow
import tecwindow

tecwindow.say_hello("ahmed")     # Hello, ahmed
tecwindow.say_hi("ahmed")        # Hi, ahmed
tecwindow.show_random_num()      # يطبع رقم عشـوائي

# يمكن استخدام alias عند الحاجة (هنا داخل نفس الملف)
import tecwindow as tw
print("--- استخدام alias ---")
tw.say_hello("ahmed")
tw.say_hi("ahmed")
tw.show_random_num()
