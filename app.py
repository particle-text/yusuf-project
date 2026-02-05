# -*- coding: utf-8 -*-
import streamlit as st
import json


# -------------------------
# تحميل قاعدة البيانات
# -------------------------


with open("elements.json", "r", encoding="utf-8") as f:
    elements = json.load(f)


# -------------------------
# دالة تنظيف النص
# -------------------------


def normalize(text):
text = text.strip().lower()
if text.startswith("ال"):
text = text[2:]
return text


# -------------------------
# إعداد الصفحة
# -------------------------


st.set_page_config(
page_title="العناصر الكيميائية",
page_icon="🧪",
layout="centered"
)


# -------------------------
# تنسيق CSS (مصَحَّح)
# -------------------------


st.markdown(
"""
<style>
.center-box {
text-align: center;
margin-top: 120px;
}
</style>
""",
unsafe_allow_html=True
)


# -------------------------
# الواجهة
# -------------------------
t.smarkdown('<div class="center-box">', unsafe_allow_html=True)


st.title("🔬 البحث عن عنصر كيميائي")


query = st.text_input("اكتب اسم العنصر (عربي أو إنجليزي أو الرمز)")


found = None


if query:
q = normalize(query)


for el in elements.values():
names = [
normalize(el["name_en"]),
normalize(el["name_ar"]),
normalize(el["symbol"])
]


if q in names:
found = el
break


# -------------------------
# عرض النتائج
# -------------------------


if query:
if found:
st.success("تم العثور على العنصر ✅")


st.write(f"**الاسم بالعربي:** {found['name_ar']}")
st.write(f"**الاسم بالإنجليزي:** {found['name_en']}")
st.write(f"**الرمز:** {found['symbol']}")
st.write(f"**العدد الذري:** {found['atomic_number']}")
st.write(f"**الكتلة الذرية:** {found['atomic_mass']}")
st.write(f"**التصنيف:** {found['category']}")
st.write(f"**المجموعة:** {found['group']}")
st.write(f"**الدورة:** {found['period']}")
st.write(f"**الشحنة الشائعة:** {found['charge']}")
st.write(f"**الخصائص:** {found['properties']}")
st.write(f"**موقعه في الطبيعة:** {found['nature']}")


else:
st.error("العنصر غير موجود في قاعدة البيانات ❌")


st.markdown('</div>', unsafe_allow_html=True)


# -------------------------
# عرض الجدول الدوري
# -------------------------


st.markdown("---")


if st.button("📊 عرض الجدول الدوري"):
st.image(
"https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Periodic_table_large.svg/1200px-Periodic_table_large.svg.png",
caption="الجدول الدوري للعناصر",
use_container_width=True

)
