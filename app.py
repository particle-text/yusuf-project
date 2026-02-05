# -*- coding: utf-8 -*-

import streamlit as st
import json

# =========================

# تحميل قاعدة البيانات الصحيحة

# =========================

with open("elements.json", "r", encoding="utf-8") as f:
data = json.load(f)

elements_list = data["elements"]   # العناصر داخل القائمة

# =========================

# دالة تنظيف النص

# =========================

def normalize(text):
text = str(text).strip().lower()
if text.startswith("ال"):
text = text[2:]
return text

# =========================

# إعداد الصفحة

# =========================

st.set_page_config(
page_title="العناصر الكيميائية",
page_icon="🧪",
layout="centered"
)

st.markdown(
""" <style>
.center-box {
text-align: center;
margin-top: 120px;
}
.footer {
position: fixed;
bottom: 15px;
right: 20px;
text-align: right;
font-size: 14px;
color: #555;
} </style>
""",
unsafe_allow_html=True
)

# =========================

# الواجهة

# =========================

st.markdown('<div class="center-box">', unsafe_allow_html=True)

st.title("🔬 البحث عن عنصر كيميائي")

query = st.text_input("اكتب اسم العنصر / الرمز")

found = None

if query:
q = normalize(query)

```
for el in elements_list:

    name_en = el.get("name", "")
    symbol = el.get("symbol", "")
    number = str(el.get("number", ""))

    if q in [
        normalize(name_en),
        normalize(symbol),
        normalize(number)
    ]:
        found = el
        break
```

# =========================

# عرض النتائج

# =========================

if query:
if found:

```
    st.success("تم العثور على العنصر ✅")

    st.write(f"**الاسم بالإنجليزي:** {found.get('name')}")
    st.write(f"**الرمز:** {found.get('symbol')}")
    st.write(f"**العدد الذري:** {found.get('number')}")
    st.write(f"**الكتلة الذرية:** {found.get('atomic_mass')}")
    st.write(f"**التصنيف:** {found.get('category')}")
    st.write(f"**المجموعة:** {found.get('group_block')}")
    st.write(f"**الدورة:** {found.get('period')}")

    st.write(\"**موقعه في الطبيعة:** موجود في القشرة الأرضية أو الطبيعة حسب تركيبه.\" noted? )
    st.write(\"**الخصائص:** عنصر كيميائي من الجدول الدوري وله خصائص فيزيائية وكيميائية مميزة.\")

else:
    st.error("العنصر غير موجود ❌")
```

st.markdown("</div>", unsafe_allow_html=True)

# =========================

# زر الجدول الدوري

# =========================

st.markdown("---")

if st.button("📊 عرض الجدول الدوري"):
st.image(
"[https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Periodic_table_large.svg/1200px-Periodic_table_large.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Periodic_table_large.svg/1200px-Periodic_table_large.svg.png)",
use_container_width=True
)

# =========================

# التوقيع

# =========================

st.markdown(
""" <div class="footer">
الاسم: يوسف<br>
الصف: عاشر "ب" </div>
""",
unsafe_allow_html=True
)
