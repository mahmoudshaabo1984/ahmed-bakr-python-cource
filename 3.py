"""محاضرة 3: مقدمة عملية للتعامل مع النصوص والأنواع في بايثون.

هذا الملف يُقسِّم الأفكار إلى أقسام صغيرة ليسهل على الطالب مراجعتها خطوة بخطوة.
"""


def section_variables() -> tuple[str, int, float]:
    """تعريف متغيرات أساسية وطباعتها."""
    # نبدأ بتعريف قيم من أنواع مختلفة (نصي، عددي، عشري) حتى نراها مطبوعة أمامنا.
    first_name: str = "Ahmed"
    age: int = 25
    pi_approximation: float = 3.1415

    print("\n[1] عرض المتغيرات الأساسية:")
    print("- الاسم الأول:", first_name)
    print("- العمر:", age)
    print("- تقريب قيمة باي:", pi_approximation)

    return first_name, age, pi_approximation


def section_quotes() -> None:
    """عرض طرق استخدام علامات التنصيص داخل النص."""
    # نستعرض كيف نكتب الجمل التي تحتوي على علامات تنصيص مختلفة دون الوقوع في أخطاء تركيبية.
    quote_with_double: str = 'قال أحمد: "مرحباً بالعالم"'
    quote_with_single: str = "ردَّت سارة: 'أهلاً بك!'"
    escaped_quotes: str = "بايثون تقول: \"التنصيص سهل إذا فهمت القاعدة\""

    print("\n[2] التعامل مع علامات التنصيص:")
    print("- مثال باستخدام علامات مزدوجة داخل مفردة:", quote_with_double)
    print("- مثال باستخدام علامات مفردة داخل مزدوجة:", quote_with_single)
    print("- مثال باستخدام محرف الهروب:", escaped_quotes)


def section_types(*values: object) -> None:
    """التحقق من نوع القيم باستخدام الدالة type."""
    print("\n[3] فحص نوع المتغيرات:")
    for index, value in enumerate(values, start=1):
        print(f"- القيمة رقم {index}: {value!r} → النوع: {type(value)}")


def section_casting_examples() -> None:
    """أمثلة إضافية توضّح الفرق بين النصوص والأرقام."""
    number_value: int = 50
    string_value: str = "50"
    float_value: float = 18.5

    print("\n[4] مقارنة بين القيم العددية والنصية:")
    print("- العدد الصحيح:", number_value, "→", type(number_value))
    print("- النص الذي يمثل رقماً:", string_value, "→", type(string_value))
    print("- العدد العشري:", float_value, "→", type(float_value))


def section_student_activity() -> None:
    """تشجيع الطالب على تجربة قيم خاصة به."""
    # يمكن تعديل القيمة التالية لتجربة أنواع أخرى (مثل الأعداد، القوائم، أو حتى القيم المنطقية).
    user_input: object = "Python"

    print("\n[5] جرّب بنفسك:")
    print(
        "غيّر قيمة المتغير user_input ثم أعد تشغيل الملف لملاحظة الفرق في النوع والناتج."
    )
    print(f"القيمة الحالية هي {user_input!r} والنوع هو {type(user_input)}")


if __name__ == "__main__":
    # نستدعي الأقسام بالترتيب حتى يسهل متابعة المحاضرة أثناء التشغيل.
    first_name_value, age_value, pi_value = section_variables()
    section_quotes()
    section_types(first_name_value, age_value, pi_value)
    section_casting_examples()
    section_student_activity()
