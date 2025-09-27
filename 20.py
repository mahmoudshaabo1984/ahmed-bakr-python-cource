





# import random
# print(random)
# هنا استدعينا كل ميزات هذه المكتبة 
# print(dir(random))



# هنا نستخدم دالة الطباعة  في هذه المكتبة 
# وهي بنفس اسم المكتبة 
# import random
# print(random.random())


# هنا نستخدم دالة لطباعة الأرقام الصحيحة 
# import random
# print(random.randint(50, 50))
# print(random.randint(10, 600))



# هذا الصطر الأول يقوم باستيراد دالتين هما random و randint من مكتبة random في بايثون.
# السطر الثاني يستخدم الدالة random() لإرجاع عدد عشـوائي بين 0 و 1.
# السطر الثالث يستخدم الدالة randint() لتوليد عدد صحيح عشـوائي بين 10 و 600.

# from random import random, randint

# print(random())
# print(randint(10, 600))





# في السطر الأول: نقوم باستيراد مكتبة random لكن باستخدام اسم مختصر لها هو rm ليسهل استخدام دوال المكتبة لاحقاً.
# في السطر الثاني: نستدعي الدالة random() من المكتبة rm لإعطاء رقم عشـوائي من 0 إلى أقل من 1 ونقوم بطباعته.
# في السطر الثالث: نستدعي الدالة randint() من المكتبة rm لإعطاء رقم صحيح عشـوائي بين 10 و 600 ونقوم بطباعته.

# import random as rm

# print(rm.random())
# print(rm.randint(10, 600))



# هذا موقع لتنزيل المكتبات في لغة البرمجة python 
# يحتوي الموقع على كثير من المكتبات 
# https://pypi.org/


# هذا الأمر يستخدم لتثبيت مكتبة webscout في بيئة البايثون الافتراضية باستخدام مدير الحزم pip
# يجب تنفيذ هذا الأمر في موجّه الأوامر (cmd أو terminal) وليس ضمن ملف كود بايثون

# pip install webscout

# الأمر الصحيح لترقية أداة pip يجب أن يكون بهذا الشكل باستخدام وحدة (module) بايثون 'python -m':
# في السطر الأول: نكتب تعليق يشرح أن هذا الأمر يستخدم لترقية pip إلى آخر إصدار.
# يجب تنفيذ هذا الأمر في موجّه الأوامر (Command Prompt أو terminal) وليس في كود بايثون داخل ملف .py

# python -m pip install --upgrade pip


# لحذف مكتبة  webscout نستخدم الأمر التالي 
# pip uninstall webscout



# هذا الكود يقوم باستيراد مكتبة tecwindow ثم:
# 1. يطبع كائن المكتبة نفسه لعرض معلومات عامة عنها.
# 2. يطبع قائمة بالسمات والدوال الموجودة داخل المكتبة باستخدام dir().

# import tecwindow
# print(tecwindow)
# print(dir(tecwindow))



# هذا الكود يقوم باستيراد مكتبة tecwindow ثم يستدعي الدالة say_hello من المكتبة لعرض رسالة ترحيب بالاسم الممرر إليها
# import tecwindow
# tecwindow.say_hello("ahmed ")



# هذا الكود يقوم باستيراد مكتبة tecwindow ثم يستدعي الدالة say_hi من المكتبة لطباعة تحية رسمية مع الكلمة "mr" والاسم الممرر إليها
# import tecwindow
# tecwindow.say_hi("mr ahmed")


# السطر الأول: نقوم باستيراد مكتبة tecwindow التي تحتوي على دوال جاهزة لتنفيذ عمليات مختلفة
# السطر الثاني: نستدعي الدالة show_random_num من المكتبة لعرض رقم عشَواءي عشَرِي بين 0 و1 ورقم صحيح عشَواءي بين 10 و600
# import tecwindow
# tecwindow.show_random_num()


# السطر الأول: نستورد مكتبة tecwindow ونسميها اختصارًا tw لتسهيل استدعاء دوالها
# السطر الثاني: نستدعي الدالة say_hello من المكتبة tw لعرض رسالة ترحيب بالاسم "ahmed"
# السطر الثالث: نستدعي الدالة say_hi من المكتبة tw لعرض تحية رسمية بالاسم "ahmed"
# السطر الرابع: نستدعي الدالة show_random_num من المكتبة tw لعرض أرقام عشوائية (عشري وصحيح)

# import tecwindow as tw

# tw.say_hello("ahmed")
# tw.say_hi("ahmed")
# tw.show_random_num()
