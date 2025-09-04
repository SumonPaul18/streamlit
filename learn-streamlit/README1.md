# ✅ সম্পূর্ণ ও সহজ গাইডলাইন: **Python Streamlit ফ্রেমওয়ার্ক শেখা**  

> 🎯 এই রিপোজিটরি হলো **Streamlit** এর উপর একটি **সম্পূর্ণ প্র্যাকটিক্যাল কোর্স** – যা আপনাকে শূন্য থেকে শীর্ষ পর্যন্ত Streamlit শেখাবে। প্রতিটি লেকচার সহজ, সাজানো এবং বাস্তব উদাহরণ দিয়ে তৈরি।

---

## 🔰 Streamlit কি ?

**Streamlit** হলো একটি **ওপেন-সোর্স পাইথন লাইব্রেরি**, যা ব্যবহার করে আপনি খুব সহজেই **ডেটা সায়েন্স, মেশিন লার্নিং বা ডেটা ভিজ্যুয়ালাইজেশন অ্যাপ** তৈরি করতে পারবেন – শুধুমাত্র পাইথন স্ক্রিপ্ট লিখে।

- কোনো HTML/CSS/JS জানার দরকার নেই।
- শুধু পাইথন লিখুন, আর Streamlit অটোমেটিক ওয়েব ইন্টারফেস বানাবে।
- দ্রুত প্রোটোটাইপ তৈরি করা যায়।
- ডেটা সায়েন্টিস্ট, ডেভেলপার, শিক্ষার্থীদের জন্য আদর্শ।

---

## 🚀 কেন Streamlit ব্যবহার করবেন?

| কারণ | ব্যাখ্যা |
|------|---------|
| ⏱️ দ্রুত ডেভেলপমেন্ট | মাত্র 5-10 লাইন কোডে একটি ফাংশনাল ওয়েব অ্যাপ তৈরি করা যায়। |
| 🧠 ডেটা সায়েন্সের সাথে সহজ ইন্টিগ্রেশন | Pandas, Matplotlib, Scikit-learn, PyTorch ইত্যাদির সাথে সহজে কাজ করে। |
| 🖥️ রিয়েল-টাইম আপডেট | কোড সেভ করলেই অ্যাপ অটো-রিলোড হয়। |
| ☁️ ডেপ্লয়মেন্ট সহজ | Streamlit Community Cloud, Heroku, AWS ইত্যাদিতে এক ক্লিকে ডেপ্লয় করা যায়। |

---

## 📚 কখন Streamlit ব্যবহার করবেন?

- মেশিন লার্নিং মডেল ডেমো তৈরি করতে
- ডেটা ভিজ্যুয়ালাইজেশন ড্যাশবোর্ড বানাতে
- টিমের সাথে শেয়ার করার জন্য প্রোটোটাইপ তৈরি করতে
- শিক্ষামূলক প্রজেক্ট বা ক্লাস রুম ডেমো তৈরি করতে

---

## 🧰 কি কি ইন্সটল করতে হবে?

### 1. প্রয়োজনীয় সফটওয়্যার
- [Python 3.8 বা তার উপরে](https://www.python.org/downloads/)
- `pip` (পাইথন ইনস্টল করলে অটো থাকে)

### 2. প্রয়োজনীয় পাইথন প্যাকেজ
```bash
pip install streamlit pandas numpy matplotlib seaborn plotly scikit-learn torch pillow opencv-python
```

### 3. ভার্চুয়াল এনভায়রনমেন্ট (অপশনাল কিন্তু রিকমেন্ডেড)
```bash
python -m venv streamlit_env
source streamlit_env/bin/activate   # Linux/Mac
# বা
streamlit_env\Scripts\activate      # Windows
```

---

## 🛠️ কিভাবে শুরু করবেন?

### ধাপ ১: একটি টেস্ট অ্যাপ তৈরি করুন
ফাইল তৈরি করুন: `app.py`
```python
import streamlit as st

st.title("Hello, Streamlit!")
st.write("এটি আমার প্রথম Streamlit অ্যাপ!")
```

### ধাপ ২: অ্যাপ রান করুন
```bash
streamlit run app.py
```
ব্রাউজারে `http://localhost:8501` ওপেন হবে।

---

## 📁 রিপোজিটরি স্ট্রাকচার (উন্নত ও সাজানো)

```
streamlit_full_course/
│
├── README.md                     ← আপনি এখন এখানে আছেন!
├── requirements.txt              ← সব প্যাকেজের তালিকা
├── data/                         ← CSV, JSON, ইমেজ ইত্যাদি
│   ├── some_data.csv
│   ├── doggo.jpg
│   ├── audio_file.mp3
│   └── dog_video.mp4
├── models/
│   └── final_mnist_model.pth     ← ML মডেল
├── utils/
│   └── full_model.py             ← কাস্টম মডেল ক্লাস
│
├── lectures/
│   ├── 01_basics.py
│   ├── 02_display_data.py
│   ├── 03_charts.py
│   ├── 04_widgets.py
│   ├── 05_input_widgets.py
│   ├── 06_advanced_input.py
│   ├── 07_media.py
│   ├── 08_layouts.py
│   ├── 09_status.py
│   ├── 10_forms_and_session.py
│   ├── 11_dynamic_updates.py
│   ├── 12_session_state.py
│   └── 13_caching.py
│
└── app.py                        ← মেইন ড্যাশবোর্ড (optional)
```

---

## 📘 লেকচার গুলো কিভাবে প্র্যাকটিস করবেন?

প্রতিটি লেকচার একটি নির্দিষ্ট ধারণা নিয়ে তৈরি। নিচের নিয়মে প্র্যাকটিস করুন:

### ✅ ধাপে ধাপে গাইডলাইন:

1. **প্রতিটি `.py` ফাইল একটি নির্দিষ্ট টপিক কভার করে**  
   - উদাহরণ: `lecture-1.py` → বেসিক আউটপুট, `lecture-4.py` → বাটন, ডাউনলোড ইত্যাদি।

2. **ফাইলটি রান করুন**
   ```bash
   streamlit run lecture-1.py
   ```

3. **আউটপুট দেখুন, কোড পড়ুন, পরিবর্তন করুন**

4. **নিজে নতুন কিছু যোগ করুন**  
   - যেমন: নতুন কলাম যোগ করুন, নতুন চার্ট বানান।

5. **পরবর্তী লেকচারে যান**

---

## 🧹 উন্নত করা হয়েছে: আপডেটেড লেকচার ফাইল (নমুনা)

### ✅ `lectures/01_basics.py` (উন্নত সংস্করণ)

```python
import streamlit as st

st.title("Lecture 1: Basics of Streamlit")

# Text
st.write("This is **bold** and *italic* text.")
st.text("This is plain text.")

# Code
code = '''
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
'''
st.code(code, language='python')

# Title & Header
st.header("Header")
st.subheader("Subheader")

# Success, Warning, Error
st.success("Success!")
st.warning("Warning: Enter email.")
st.error("Error occurred.")
```

---

## 🔁 প্রতিটি লেকচারের সংক্ষিপ্ত বিবরণ

| লেকচার | টপিক | উদাহরণ |
|--------|------|--------|
| 01 | বেসিক আউটপুট | `st.write`, `st.title`, `st.code` |
| 02 | ডেটা ডিসপ্লে | `st.dataframe`, `st.table`, `st.json` |
| 03 | চার্ট | `st.line_chart`, `st.map`, `matplotlib` |
| 04 | ইন্টারঅ্যাকটিভ উইজেট | বাটন, চেকবক্স, ডাউনলোড বাটন |
| 05 | ইনপুট উইজেট | স্লাইডার, মাল্টিসিলেক্ট, টেক্সট ইনপুট |
| 06 | এডভান্সড ইনপুট | ফাইল আপলোড, ক্যামেরা, কালার পিকার |
| 07 | মিডিয়া | ইমেজ, অডিও, ভিডিও ডিসপ্লে |
| 08 | লেআউট | সাইডবার, কলাম, ট্যাব, কনটেইনার |
| 09 | স্ট্যাটাস মেসেজ | প্রগ্রেস বার, স্পিনার, বেলুন |
| 10 | ফর্ম ও সেশন | ফর্ম সাবমিশন, `st.session_state` বেসিক |
| 11 | ডাইনামিক আপডেট | `add_rows()`, রিয়েল-টাইম চার্ট |
| 12 | সেশন স্টেট | ডেটা সংরক্ষণ, কলব্যাক ফাংশন |
| 13 | ক্যাশিং | `@st.cache_resource`, `@st.cache_data` |

---

## 🧩 অতিরিক্ত যুক্তি (আপনার জন্য)

### ✅ `requirements.txt`
```txt
streamlit==1.29.0
pandas==2.1.0
numpy==1.24.0
matplotlib==3.7.0
pillow==10.0.0
torch==2.1.0
opencv-python==4.8.0
```

### ✅ `app.py` (মেইন ড্যাশবোর্ড - optional)
```python
import streamlit as st

st.title("🚀 Streamlit Full Course Dashboard")
st.write("Select a lecture from the sidebar to explore.")

lectures = {
    "Lecture 1: Basics": "lectures/01_basics.py",
    "Lecture 2: Display Data": "lectures/02_display_data.py",
    # ... add all
}

choice = st.sidebar.selectbox("Choose Lecture", list(lectures.keys()))

st.code(f"Run: streamlit run {lectures[choice]}")
```

---

## 🌐 ডেপ্লয় করবেন কিভাবে?

1. **Streamlit Community Cloud (ফ্রি)**
   - GitHub রিপোজিটরি ক্লোন করুন
   - [https://streamlit.io/cloud](https://streamlit.io/cloud) এ লগ ইন করুন
   - রিপোজিটরি যুক্ত করুন
   - ডেপ্লয়!

2. **Heroku / VPS**
   - `Procfile` তৈরি করুন
   - `gunicorn` ব্যবহার করুন

---

## 📢 টিপস

- কোড লেখার সময় `st.write()` দিয়ে ডিবাগ করুন
- ডেটা বড় হলে `@st.cache_data` ব্যবহার করুন
- মডেল লোড হলে `@st.cache_resource` ব্যবহার করুন
- সেশন স্টেট ব্যবহার করে ইউজার ইনপুট মনে রাখুন

---

## 📚 রেফারেন্স

- [Streamlit অফিসিয়াল ডকুমেন্টেশন](https://docs.streamlit.io/)
- [Streamlit গিটহাব](https://github.com/streamlit/streamlit)
- [Streamlit কমিউনিটি ফোরাম](https://discuss.streamlit.io/)

---

## 🙏 শেষ কথা

> আপনি যদি পাইথন জানেন, তবে **Streamlit আপনার জন্য**। এটি শুধু একটি টুল নয়, এটি আপনার ডেটা স্টোরি বলার একটি মাধ্যম।

🎯 প্রতিদিন একটি লেকচার করুন, প্র্যাকটিস করুন, নিজের কিছু যোগ করুন – এক মাসের মধ্যে আপনি **Streamlit মাস্টার**!

---

✅ **Happy Coding with Streamlit!**  
👨‍💻 যদি কোনো প্রশ্ন থাকে, গিটহাব ইস্যুতে জানান।  
⭐ রিপোজিটরি যদি ভালো লাগে, তাহলে **Star** দিন!

--- 
