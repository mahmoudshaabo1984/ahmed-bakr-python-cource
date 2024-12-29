


#طباعة الكلمة hello python بأستخدام الدالة print
# print('hello python')


#  استخدام  علامة \ لتخطي الأحرف 
# هذه العلامة سوف تقوم بتخطي الحرف الذي بعد هذه العلامة
# سوف يحدث خطئ
# print('ahme\d bakr')


#استخدام Escape Sequence Characters
# طباعة كلامتين بأستخدام علامة \ 
# وظيفة هذه العلامة تخطي علامات التنصيص المنفردة 
# في هذا الكود اذا اردنا طباعة كلمة ثانية نستخدم علمتين 
# \ قبل الكلمة وبعدها 
# print('ahmed bakr \'hello\'')



#استخدام Escape Sequence Characters
# طباعة كلامتين بأستخدام علامة \ 
# وظيفة هذه العلامة تخطي علامات التنصيص المزدوجة 
# تكرار نفس المثال لكن باستخدام علمات التنصيص ""
# في هذا الكود اذا اردنا طباعة كلمة ثانية نستخدم علمتين 
# \ قبل الكلمة وبعدها 
# print("ahmed bakr \"hello\"")



#استخدام Escape Sequence Characters
# هنا نريد أن نكتب علامة \ في الكود 
# فنقوم بكتابة علامة \\ مرتين في الكود لكي يعمل الكود بشكل صحيح 
# print("I like \\")


#استخدام Escape Sequence Characters
# في هذا المثال سوف نستخدم علامة \n لكتابة كل كلمة على صطر
# على سبيل المثاال طباعة كلمتين على صطرين  like , youtube
# print("I like \n youtube")

# print many words each word on a line 
# طباعة عدة كلمات كل كلمة على صطر 
#using \n لفصل الصطور 
# print("I like \n youtube \n and facebook \n and telgram")

# هنا طبع الكود على صطر واحد
# هنا  تخطينا الصطور باستخدام  علامة \ 
# اذا اردنا ان نتفادا الأخطاء في الكود 
# نكتب علامة \ في آخر كل صطر 
# print("I like \
#       facebookand\
#       youtube and\
#       telgram")




# كتابة الكود مرى أخرى للتأكيد الفهم 
# هنا طبع الكود على صطر واحد
# print("I like \
# facebook and\
# youtube and\
# telegram")

# الطريقة الثانية لطباعة الكلامات على عدة صطور كل كلمة في صطر 
#استخدام 3 علامات تنصيص """  
# للطباعة على ثلاثة صطور 
# print("""I like 
# "facebook and"
# "youtube and"
# telgram""")

#مثال للأستخدام  Escape Sequence Characters
# print("hello\b pytho\tn")


 #انشاء متغير جديد  
# user = 'ahmed bakr'
# print(user)


# Slicing and Indexing
# الحصول على  أول حرف
# هنا طبع الحرف الأول a
# user = 'ahmed bakr'
# print(user[0])

# طباعة الحرف الرابع d
# user = 'ahmed bakr'
# print(user[4])


#طباعة الحرف السادس b
# هنا اعتبرنا المسافة حرف لهذا كان الحرف b هو الحرف السادس
# user = 'ahmed bakr'
# print(user[6])

# الحصول على آخر حرف  r
# هنا علامة -1 اطبعت لنا الحرف الأخير r
# user = 'ahmed bakr'
# print(user[-1])


# الحصول على الحرف الثاني h
# user = 'ahmed bakr'
# print(user[1])



# الحصر 
# طباعة الأحرف من 0 الى 5
# باستخدام الحصر 
# سوف يطبع ahmed 
# هنا سوف يطبع indexes من  0 الى 5
# user = 'ahmedbakr'
# print(user[0:5])

#طباعة الأحرف من 0 الى 6 
# سوف يطبع ahmedb
# user = 'ahmedbakr'
# print(user[0:6])



#طباعة من 0 الى -1
# سوف يطبع ahmedbak
# لن يطبع الحرف الأخير r لأنه آخر عنصر غير متضمن في الطباعة 
# user = 'ahmedbakr'
# print(user[0:-1])


#طباعة من 0:يطبعة ahmedbakr
# هنا قام بطباعة النص كامل من بداية الأندكس الى نهايته 
# سوف تكون النتيجة ahmedbakr
# user = 'ahmedbakr'
# print(user[0:])


# طباعة من أول خمسة احرف
# سوف يطبع bakr
# user = 'ahmedbakr'
# print(user[5:])


# طباعة من 0 :61:
#سوف يطبع ahmedb
# user = 'ahmedbakr'
# print(user[0:6:1])


# طباعة من  0:6:2
# سوف يطبع amd
# هنا سوف يتخطى حرفين 
# user = 'ahmedbakr'
# print(user[0:6:2])


# طباعة من 0 : 10:3  تخطي 3 حروف 
# سوف يطبع aea
# هنا تخطينا 3 حروف 
# user = 'ahmedbakr'
# print(user[0:106:3])


# الحصول على النص بالكامل بالعكس (التقطيع بالعكس)
# هنا تم طباعة النص بالمقلوب نص معكوس 
# user = 'ahmedbakr'
# print(user[::-1])



# معرفا عدد الأحرف بأستخدام الدالة len
# هنا عدد الأحرف 34 عرفنها بأستخدام الدالة len
# msg = "hello Qais, and AHMED, and mahmoud"
# print(len(msg))


# تحويل النص إلى حروف صغيرة (lowercase)
# تم تحويل النص الى أحرف صغيرة  بالكامل
# msg = "hello Qais, and AHMED, and mahmoud"
# print(msg.lower())



# تحويل النص إلى حروف كبيرة (uppercase)
# هنا تم تحويل النص الى أحرف كبيرة 
# msg = "hello Qais, and AHMED, and mahmoud"
# print(msg.upper())

# حساب طول النص
# عدد الأحرف 34
# msg = "hello Qais, and AHMED, and mahmoud"
# print(len(msg))


# Concatenation 
# تعريف نصوص إضافية
# دمج النصوص وجمعها 
# هنا تم دمج النص ahmedbakr من دون مسافات 
# one = "ahmed"
# two = "bakr"
# age = 25 
# print(one +two)


# تعريف نصوص إضافية
# دمج النصوص وجمعها 
#هنا سوف  يطبع النص بدون مسافات helloahmedbakrr
# هنا سطبع النص مع رسالة  helloahmedbakr
# one = "ahmed"
# two = "bakr"
# age = 25 
# print("hello"+one+two)


# دمج النصوص مع إضافة مسافة واحدة بين hello و one
# هنا وضعنا مسافة بعد كلمة hello  وقبل علامة التنصيص 
# أصبحت النتيجة كالتالي hello ahmedbakr
# one = "ahmed"
# two = "bakr"
# age = 25 
# print("hello "+one+two)


# دمج النصوص مع إضافة مسافات بين الكلمات
# هنا سوف يطبع hello ahmed bakr مع مسافات بين الكلمات 
# وضعنا المسافات لاننا أستخدمنا بعد كل كلمة +" " وبعدها + والمتغير
# نفذنا أمر الطباعة على الشكل التالي 
# print("hello"+" "+one+" "+two) 
# اصبحت النتيجة على الشكل التالي hello ahmed bakr
# one = "ahmed"
# two = "bakr"
# age = 25 
# print("hello"+" "+one+" "+two)



# محاولة دمج نصوص مع عدد (متغير age)
# هذا السطر يحتوي على خطأ لأن المتغير age نوعه int، ولا يمكن دمجه مع نصوص مباشرة باستخدام علامة +
# TypeError: can only concatenate str (not "int") to str
# هناا سوف نضع تعليق لهذا الكود لأنه لن يعمل 
# لا يمكن دمج str مع  int
# one = "ahmed"
# two = "bakr"
# age = 25 
# print('hello'+' '+one+' '+two+' your age is: '+ age)  

