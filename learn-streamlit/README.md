## 📚 Course Overview

This course is designed to teach **Streamlit**, a powerful Python library for building interactive web applications for data science and machine learning. The course progresses from basic UI elements to advanced concepts like caching, session state, forms, and real-time updates.

Each lecture builds upon the previous one, allowing you to gradually build complex and dynamic apps.

---

## 🗂️ Repository Structure

```
├── README.md                    ← You are here
├── lecture-1.py                 ← Introduction & Basic Output
├── lecture-2.py                 ← Displaying Data: Tables, Metrics, JSON
├── lecture-3.py                 ← Charts and Maps
├── lecture-4.py                 ← Interactive Widgets: Buttons, Downloads, Checkboxes, etc.
├── lecture-5.py                 ← Input Widgets: Sliders, Selectors, Text Inputs
├── lecture-6.py                 ← Advanced Inputs: File Upload, Camera, Color Picker
├── lecture-7.py                 ← Media: Images, Audio, Video
├── lecture-8.py                 ← Layouts: Sidebar, Columns, Tabs, Expanders
├── lecture-9.py                 ← Status & Feedback: Progress, Spinners, Animations
├── lecture-10.py                ← Forms, Echo, Help, Page Config
├── lecture-11.py                ← Dynamic Updates & Real-Time Charts
├── lecture-12.py                ← Session State Management
└── lecture-13.py                ← Caching for Performance (Model Loading)
```

> 💡 All scripts are standalone and can be run as:  
> ```bash
> streamlit run lecture-1.py
> ```

---

## 🎯 Learning Goals by Lecture

### 🔹 **Lecture 1: Getting Started with Streamlit**
**Goal**: Understand basic syntax and output methods.
- Use `st.write()`, `st.code()`, `st.title()`, etc.
- Display Python objects, code, and basic text formatting.
- Learn how Streamlit auto-renders data.

✅ **Practice Tip**: Replace the hardcoded CSV path with a sample DataFrame using `pd.DataFrame()` to avoid file dependency.

---

### 🔹 **Lecture 2: Displaying Data Structures**
**Goal**: Present data clearly using tables, metrics, and JSON viewers.
- `st.dataframe()` – scrollable, styled tables.
- `st.table()` – static table snapshot.
- `st.metric()` – show KPIs with deltas.
- `st.json()` – inspect nested data (e.g., APIs, configs).

✅ **Practice Tip**: Try loading your own JSON or CSV file. Use `.head()` to limit rows.

---

### 🔹 **Lecture 3: Visualizing Data with Charts**
**Goal**: Visualize data using built-in and Matplotlib charts.
- Line, area, bar charts with `st.line_chart()`, etc.
- Use `matplotlib` with `st.pyplot()`.
- Plot geographic data using `st.map()`.

✅ **Practice Tip**: Add titles and labels to your Matplotlib plots. Try different datasets.

---

### 🔹 **Lecture 4: Interactive Widgets – Part 1**
**Goal**: Add interactivity with buttons, downloads, and selection widgets.
- `st.button()` with callbacks.
- `st.download_button()` for files (CSV, text, images).
- `st.checkbox()`, `st.radio()`, `st.selectbox()` for user input.

✅ **Practice Tip**: Create a mini-form that lets users choose an option and download a custom message.

---

### 🔹 **Lecture 5: Input Widgets – Part 2**
**Goal**: Handle numeric, textual, and ranged inputs.
- `st.slider()` – single and range values.
- `st.select_slider()` – choose from ordered options.
- `st.text_input()` and `st.number_input()` – validate user input.
- `st.time_input()` and `st.date_input()` – for scheduling.

✅ **Practice Tip**: Combine a slider and number input to control the same value dynamically.

---

### 🔹 **Lecture 6: Advanced Inputs**
**Goal**: Work with user-uploaded content.
- `st.file_uploader()` – handle images, text, and binary files.
- `st.camera_input()` – capture photos via webcam.
- `st.color_picker()` – select colors visually.

✅ **Practice Tip**: Build a simple image metadata viewer that shows shape, mode, and size.

---

### 🔹 **Lecture 7: Displaying Media**
**Goal**: Embed audio, video, and images.
- `st.image()` – support PIL/OpenCV images with captions.
- `st.audio()` and `st.video()` – play media files.
- Handle BGR/RGB channel differences.

✅ **Practice Tip**: Allow users to upload an image and display it with a custom caption.

---

### 🔹 **Lecture 8: App Layout & Organization**
**Goal**: Structure your app for better UX.
- `st.sidebar` – place navigation and filters.
- `st.columns()` – side-by-side content.
- `st.tabs()` – organize sections.
- `st.expander()` – hide/show detailed content.
- `st.container()` – group elements logically.

✅ **Practice Tip**: Rebuild a dashboard layout using tabs for "Data", "Charts", and "Settings".

---

### 🔹 **Lecture 9: Status Indicators & Feedback**
**Goal**: Provide user feedback during long operations.
- `st.progress()` – show progress bars.
- `st.spinner()` – indicate loading.
- `st.balloons()` / `st.snow()` – fun success animations.
- `st.exception()` – debug errors gracefully.

✅ **Practice Tip**: Simulate a model training loop with a progress bar and spinner.

---

### 🔹 **Lecture 10: Forms, Echo, and Utilities**
**Goal**: Group inputs and manage app settings.
- `st.form()` – batch input submission.
- `st.set_page_config()` – set title, layout (`wide`), icon.
- `st.echo()` – show code as it executes.
- `st.help()` – inspect functions inline.

✅ **Practice Tip**: Create a registration form with name, age, birthday, and submit button.

---

### 🔹 **Lecture 11: Real-Time & Dynamic Updates**
**Goal**: Update charts and tables in real time.
- Use `.add_rows()` to stream new data.
- Simulate live data with `time.sleep()` and loops.
- Update charts dynamically (great for monitoring).

✅ **Practice Tip**: Turn this into a stock ticker simulator with random price updates.

---

### 🔹 **Lecture 12: Session State Management**
**Goal**: Persist user input across reruns.
- Initialize, modify, and delete `st.session_state`.
- Use widget keys to bind inputs to session state.
- Callback functions with `on_click`.

✅ **Practice Tip**: Build a counter app that remembers the count after button clicks.

---

### 🔹 **Lecture 13: Performance Optimization with Caching**
**Goal**: Speed up app loading using caching.
- `@st.cache_resource` – cache heavy objects (models, DB connections).
- `@st.cache_data` – cache computed results (e.g., predictions).
- Load PyTorch model efficiently.

> ⚠️ Fix: The original code has a bug — `model` is used before being defined in `inference()`.

🔧 **Corrected Version**:
```python
@st.cache_data
def inference(data):
    st.write("inference time", time.time())
    return model(torch.Tensor(data)).detach().numpy()
```

✅ **Practice Tip**: Replace the model with a simple scikit-learn model or cached DataFrame transform.

---

## 🛠️ Setup Instructions

### 1. Install Dependencies
```bash
pip install streamlit pandas numpy matplotlib torch pillow opencv-python
```

### 2. Run Any Lecture
```bash
streamlit run lecture-1.py
```

> 🔁 Refresh the browser to see changes (or enable auto-reload in Streamlit).

---

## 🧪 Best Practices for Learning

| Tip | Description |
|-----|-------------|
| ✅ **Modify & Experiment** | Change values, add widgets, break things! |
| ✅ **Build Mini-Apps** | After each 3 lectures, combine concepts into a small project. |
| ✅ **Use Sample Data** | Avoid hardcoded paths. Use `pd.util.testing.makeDataFrame()` for portability. |
| ✅ **Check Docs** | Refer to [Streamlit API Reference](https://docs.streamlit.io/) often. |
| ✅ **Deploy Later** | Once confident, deploy your app using Streamlit Community Cloud. |

---

## 🎓 Final Project Suggestion

Build a **"Data Explorer App"** that:
- Uploads a CSV.
- Shows summary stats and charts.
- Filters data using sliders and selectors.
- Exports cleaned data.
- Uses caching and session state.

---

## 🙌 Contributing

Feel free to:
- Report bugs.
- Suggest new lectures (e.g., authentication, database integration).
- Add exercises or quizzes.

---

## 📄 License

MIT License – Use freely for learning and teaching.

---

🚀 **Happy Coding with Streamlit!**  
Turn your scripts into beautiful, interactive apps in minutes.