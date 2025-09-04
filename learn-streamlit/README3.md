# 🎯 **Complete Beginner’s Guide to Python Streamlit**  

> 📌 This guide is made for **absolute beginners**.  
> You’ll learn **Streamlit from zero to expert**, one lecture at a time.  
> Each lecture has its own **`.md` file** with full explanation and practice guide.

---

## 📁 Final Folder Structure (Organized & Easy to Learn)

We will restructure your course like this:

```
streamlit_course/
│
├── README.md
├── requirements.txt
├── data/
│   ├── some_data.csv
│   ├── doggo.jpg
│   ├── audio_file.mp3
│   └── dog_video.mp4
├── models/
│   └── final_mnist_model.pth
├── utils/
│   └── full_model.py
│
├── lectures/
│   ├── 01_basics.py
│   ├── 02_display_data.py
│   ├── 03_charts_and_maps.py
│   ├── 04_buttons_widgets.py
│   ├── 05_input_widgets.py
│   ├── 06_file_camera.py
│   ├── 07_media.py
│   ├── 08_layouts.py
│   ├── 09_status.py
│   ├── 10_forms_session.py
│   ├── 11_dynamic_updates.py
│   ├── 12_session_state.py
│   └── 13_caching.py
│
├── guides/
│   ├── lecture_01_basics.md
│   ├── lecture_02_display_data.md
│   ├── lecture_03_charts_and_maps.md
│   ├── lecture_04_buttons_widgets.md
│   ├── lecture_05_input_widgets.md
│   ├── lecture_06_file_camera.md
│   ├── lecture_07_media.md
│   ├── lecture_08_layouts.md
│   ├── lecture_09_status.md
│   ├── lecture_10_forms_session.md
│   ├── lecture_11_dynamic_updates.md
│   ├── lecture_12_session_state.md
│   └── lecture_13_caching.md
│
└── app.py
```

---

## 🧰 What You Need to Install (Step by Step – For Linux Beginners)

Let’s start from zero.

---

### ✅ Step 1: Install Python on Linux (Ubuntu/Debian)

Most Linux systems have Python, but let's make sure.

Open **Terminal** and run:
```bash
python3 --version
```

👉 If you see `Python 3.8`, `3.9`, or higher → **Good!**

👉 If not, install it:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

✅ Check again:
```bash
python3 --version
```

---

### ✅ Step 2: Install `pip` (Package Installer for Python)

`pip` helps you install libraries.

Check:
```bash
pip3 --version
```

If missing, install:
```bash
sudo apt install python3-pip -y
```

---

### ✅ Step 3: Install Required Libraries

Run this command:
```bash
pip3 install streamlit pandas numpy matplotlib seaborn pillow opencv-python torch
```

💡 This installs:
- `streamlit` → to build web apps
- `pandas`, `numpy` → for data
- `matplotlib`, `seaborn` → for charts
- `pillow`, `opencv` → for images
- `torch` → for AI models (used in lecture 13)

---

### ✅ Step 4: Test Streamlit

Create a file called `hello.py`:
```python
import streamlit as st

st.title("Hello, Streamlit!")
st.write("My first app is working!")
```

Save it, then run:
```bash
streamlit run hello.py
```

👉 A web browser will open at `http://localhost:8501`  
👉 You’ll see your app!

✅ Success! Press `Ctrl + C` in terminal to stop.

---

### ✅ Step 5: Create `requirements.txt`

This helps others install the same packages.

**File: `requirements.txt`**
```txt
streamlit==1.29.0
pandas==2.1.0
numpy==1.24.0
matplotlib==3.7.0
pillow==10.0.0
opencv-python==4.8.0
torch==2.1.0
```

To install later:
```bash
pip3 install -r requirements.txt
```

---

## 📘 How to Practice Each Lecture (Step-by-Step)

After setting up, follow this process for **each lecture**:

1. Go to the `lectures/` folder
2. Run: `streamlit run 01_basics.py`
3. Read the `.md` guide in `guides/`
4. Try changing the code
5. Add your own features
6. Move to the next lecture

---

## 📚 Lecture-wise Guide Files (Each Has Its Own `.md`)

Below are the **13 detailed `.md` files** you asked for — one for each lecture.

---

### ✅ `guides/lecture_01_basics.md`

# 📘 Lecture 1: Basics of Streamlit

## 🎯 What You’ll Learn
- How to show text, titles, and code
- Use `st.write()`, `st.title()`, `st.code()`
- Display dictionaries and plots

## 🔍 Code Breakdown
```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Show code with syntax highlighting
code = '''def func():
    print(np.arange(10))'''
st.code(code, language="python")
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.title("text")` | Big heading |
| `st.header()` / `st.subheader()` | Smaller headings |
| `st.write()` | Show anything (text, dict, df) |
| `st.text()` | Plain text |
| `st.code()` | Show code block |

## ✅ How to Practice
1. Run: `streamlit run 01_basics.py`
2. Change the code string to your own function
3. Add: `st.write("Hello, I am [Your Name]")`
4. Try showing a dictionary: `st.write({"city": "Dhaka", "age": 25})`

---

### ✅ `guides/lecture_02_display_data.md`

# 📘 Lecture 2: Display Data

## 🎯 What You’ll Learn
- Show tables and dataframes
- Display JSON and metrics

## 🔍 Code Breakdown
```python
df = pd.DataFrame(np.random.randn(50, 20), columns=[f"cols{i}" for i in range(20)])
st.dataframe(df)  # Scrollable table
st.table(df)      # Static table
st.json(dt)       # Pretty JSON
st.metric("Stock", "3220.70", "19.10")  # KPI
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.dataframe(df)` | Interactive table |
| `st.table(df)` | Simple static table |
| `st.json(data)` | View JSON nicely |
| `st.metric(label, value, delta)` | Show performance metric |

## ✅ How to Practice
1. Create a CSV file: `data/products.csv`
   ```
   Product,Price
   Laptop,800
   Mouse,20
   ```
2. Load it: `pd.read_csv("data/products.csv")`
3. Show with `st.dataframe()`

---

### ✅ `guides/lecture_03_charts_and_maps.md`

# 📘 Lecture 3: Charts & Maps

## 🎯 What You’ll Learn
- Draw line, bar, area charts
- Use `matplotlib`
- Show locations on map

## 🔍 Code Breakdown
```python
df = pd.DataFrame(np.random.randn(10, 2), columns=["prices", "diff"])
st.line_chart(df)
st.bar_chart(df)
st.map(places)  # Show lat-long points
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.line_chart(df)` | Line chart |
| `st.bar_chart(df)` | Bar chart |
| `st.area_chart(df)` | Area chart |
| `st.pyplot(fig)` | Custom Matplotlib plot |
| `st.map(df)` | Show points on map |

## ✅ How to Practice
1. Make a line chart of student scores
2. Use `matplotlib` to draw a histogram
3. Add your city to `places` DataFrame and show on map

---

### ✅ `guides/lecture_04_buttons_widgets.md`

# 📘 Lecture 4: Buttons & Widgets

## 🎯 What You’ll Learn
- Use buttons, checkboxes, radio, selectbox
- Download files

## 🔍 Code Breakdown
```python
if st.button("Show Time"):
    st.write(time.time())

st.checkbox("I agree")
st.radio("Choose food", ["Pizza", "Burger"])
st.selectbox("City", ["Moscow", "NY"])
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.button()` | Click to trigger action |
| `st.checkbox()` | True/False input |
| `st.radio()` | Choose one option |
| `st.selectbox()` | Dropdown menu |
| `st.download_button()` | Let user download file |

## ✅ How to Practice
1. Make a button that shows "Hello"
2. Build a survey: ask name, favorite food
3. Let user download a CSV file

---

### ✅ `guides/lecture_05_input_widgets.md`

# 📘 Lecture 5: Input Widgets

## 🎯 What You’ll Learn
- Get user input with sliders, text, numbers

## 🔍 Code Breakdown
```python
age = st.slider("Age", 18, 120, 20)
email = st.text_input("Email", max_chars=20)
weight = st.number_input("Weight", 40, 120, 65)
color = st.select_slider("Color", options=["Red", "Blue"])
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.slider()` | Choose number in range |
| `st.text_input()` | Type text |
| `st.number_input()` | Type number |
| `st.multiselect()` | Pick multiple items |
| `st.select_slider()` | Slider with labels |

## ✅ How to Practice
1. Make a BMI calculator: input height & weight
2. Ask user for favorite colors using `multiselect`

---

### ✅ `guides/lecture_06_file_camera.md`

# 📘 Lecture 6: File Upload & Camera

## 🎯 What You’ll Learn
- Upload files (text, image)
- Take photo from webcam
- Pick color

## 🔍 Code Breakdown
```python
fl = st.file_uploader("Upload")
if fl:
    if "image" in fl.type:
        img = Image.open(fl)
        st.image(img)

pic = st.camera_input("Take photo")
color = st.color_picker("Pick color")
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.file_uploader()` | Upload any file |
| `st.camera_input()` | Take photo |
| `st.color_picker()` | Choose color |

## ✅ How to Practice
1. Upload a `.txt` file and show its content
2. Take a photo and display it
3. Print selected color

---

### ✅ `guides/lecture_07_media.md`

# 📘 Lecture 7: Media (Image, Audio, Video)

## 🎯 What You’ll Learn
- Show images, play audio/video

## 🔍 Code Breakdown
```python
st.image("doggo.jpg", caption="Dog", width=800)
st.audio("audio.mp3")
st.video("video.mp4")
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.image()` | Show image |
| `st.audio()` | Play audio |
| `st.video()` | Play video |

## ✅ How to Practice
1. Add your favorite song
2. Play a YouTube video (use URL)
3. Show multiple images in a row

---

### ✅ `guides/lecture_08_layouts.md`

# 📘 Lecture 8: Layouts (Sidebar, Columns, Tabs)

## 🎯 What You’ll Learn
- Organize your app layout

## 🔍 Code Breakdown
```python
with st.sidebar:  # Sidebar
    st.radio("Option", ["audio", "video"])

col1, col2 = st.columns(2)  # Side by side
tab1, tab2 = st.tabs(["Audio", "Video"])  # Tabs
exp = st.expander("See more")  # Hidden section
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.sidebar` | Put widgets on side |
| `st.columns()` | Split layout |
| `st.tabs()` | Switch between views |
| `st.expander()` | Hide/show content |
| `st.container()` | Group elements |

## ✅ How to Practice
1. Put a slider in the sidebar
2. Show image and text side by side
3. Create two tabs: “About” and “Data”

---

### ✅ `guides/lecture_09_status.md`

# 📘 Lecture 9: Status & Effects

## 🎯 What You’ll Learn
- Show progress, loading, fun effects

## 🔍 Code Breakdown
```python
my_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    my_bar.progress(i+1)

with st.spinner("Wait..."):
    time.sleep(5)
st.balloons()
st.snow()
```

## 🧩 Key Functions
| Function | Purpose |
|--------|--------|
| `st.progress()` | Progress bar |
| `st.spinner()` | Loading message |
| `st.balloons()` / `st.snow()` | Fun effects |
| `st.error()` / `st.success()` | Status messages |

## ✅ How to Practice
1. Simulate a 10-second task with progress bar
2. Show "Success!" after completion
3. Add `st.balloons()` at the end

---

### ✅ `guides/lecture_10_forms_session.md`

# 📘 Lecture 10: Forms & Session Basics

## 🎯 What You’ll Learn
- Group inputs in a form
- Use `st.echo()` and `st.help()`
- Set page config

## 🔍 Code Breakdown
```python
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.slider("Age")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(name, age)
```

Also:
```python
st.set_page_config(layout="wide", page_title="My App")
with st.echo():  # Shows code as output
    x = 10
st.help(datetime.time)  # Shows doc
```

## ✅ How to Practice
1. Make a registration form
2. Use `st.echo()` to show your function
3. Set page to wide mode

---

### ✅ `guides/lecture_11_dynamic_updates.md`

# 📘 Lecture 11: Dynamic Updates

## 🎯 What You’ll Learn
- Update charts in real time

## 🔍 Code Breakdown
```python
chart = st.line_chart(df1)
for i in range(5):
    time.sleep(1)
    new_data = pd.DataFrame(np.random.randn(1, 2))
    chart.add_rows(new_data)
```

## 🧩 Key Idea
- `add_rows()` adds new data to existing chart
- Great for live data (stock, sensor)

## ✅ How to Practice
1. Simulate temperature rising
2. Update a bar chart every second
3. Show live random numbers

---

### ✅ `guides/lecture_12_session_state.md`

# 📘 Lecture 12: Session State

## 🎯 What You’ll Learn
- Remember values across reruns

## 🔍 Code Breakdown
```python
if "key" not in st.session_state:
    st.session_state.key = 1

st.session_state.key = 2
del st.session_state.key

# Widget with key
st.text_input("Name", key="name")
st.write(st.session_state.name)
```

Callback:
```python
def form_callback():
    st.write(st.session_state.my_slider)

st.slider("Slider", key="my_slider", on_click=form_callback)
```

## ✅ How to Practice
1. Make a counter app
2. Save user name even after input changes
3. Use callback to show slider value

---

### ✅ `guides/lecture_13_caching.md`

# 📘 Lecture 13: Caching

## 🎯 What You’ll Learn
- Speed up app with caching

## 🔍 Code Breakdown
```python
@st.cache_resource
def load_model():
    model = Net()
    model.load_state_dict(torch.load("model.pth"))
    return model

@st.cache_data
def inference(data):
    return model(torch.Tensor(data))
```

## 🧩 Key Rules
- `@st.cache_resource`: For heavy objects (models, DB connections)
- `@st.cache_data`: For function results (data processing)

## ✅ How to Practice
1. Cache a large CSV file
2. Cache a slow function (use `time.sleep(5)`)
3. See how fast it runs second time

---

## 🚀 Final Tips for Success

1. 🔁 **Run each lecture one by one**
2. ✍️ **Type code yourself** (don’t copy-paste)
3. 🧪 **Break it, fix it, improve it**
4. 🌐 **Deploy on [Streamlit Community Cloud](https://share.streamlit.io/)**

---

## 📚 Resources

| Link | Purpose |
|------|--------|
| [docs.streamlit.io](https://docs.streamlit.io/) | Official Docs |
| [Streamlit Gallery](https://streamlit.io/gallery) | See real apps |
| [GitHub Repo](#) | Your course repo |

---

## 🙏 You Can Do It!

> Every expert was once a beginner.  
> Just start. Build small. Learn fast.  
> **You’ve got this!**

✅ Now go run your first lecture:
```bash
streamlit run lectures/01_basics.py
```

⭐ **If you like this course, give your repo a Star!**  
👨‍💻 Happy Coding! 🚀