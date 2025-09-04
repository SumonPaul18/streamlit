# Streamlit Full Course 🚀

Welcome to the **Streamlit Full Course**! This repository contains a series of hands-on Python scripts (`lecture-*.py`) that guide you step-by-step through building interactive web apps using [Streamlit](https://streamlit.io/), a powerful open-source framework for creating data apps with pure Python.

Each lecture focuses on a specific feature or concept in Streamlit, progressing from basic text display to advanced topics like caching, session state, and real-time updates.

---

## 📁 Lecture Contents
```
.
├── README.md
├── lecture-1.py         # Basics
├── lecture-2.py         # Data display
├── lecture-3.py         # Charts
├── lecture-4.py         # Widgets
├── lecture-5.py         # Advanced inputs
├── lecture-6.py         # File/media inputs
├── lecture-7.py         # Media output
├── lecture-8.py         # Layouts
├── lecture-9.py         # Status indicators
├── lecture-10.py        # Forms & config
├── lecture-11.py        # Dynamic updates
├── lecture-12.py        # Session state
└── lecture-13.py        # ML caching
```

## 📚 Lecture Guide

Below is a detailed breakdown of each lecture: its **topic**, **objective**, **purpose**, and **how to run it**.

---

### 🔹 Lecture 1: Introduction to Streamlit Basics
- **Topic**: Basic elements: text, code, data, plots
- **Objective**: Learn how to display text, code, and simple visualizations.
- **Purpose**: Set up the foundation of Streamlit app structure.
- **What’s Covered**: `st.write`, `st.code`, `st.title`, `st.header`, matplotlib integration.
- **How to Run**:
  ```bash
  streamlit run lecture-1.py
  ```
  > ⚠️ Make sure `some_data.csv` exists at `D:\datum\streamlit\some_data.csv`, or update the path.

---

### 🔹 Lecture 2: Displaying Data & Structured Content
- **Topic**: DataFrames, tables, metrics, JSON
- **Objective**: Show different ways to present structured data.
- **Purpose**: Understand how to format and visualize tabular and hierarchical data.
- **What’s Covered**: `st.dataframe`, `st.table`, `st.metric`, `st.json`.
- **How to Run**:
  ```bash
  streamlit run lecture-2.py
  ```
  > ⚠️ Requires `all_intents_js.json` at `D:\datum\aa_chatbot\simple_chatbot\prac\all_intents_js.json`, or replace with any JSON file.

---

### 🔹 Lecture 3: Data Visualization with Built-in & Matplotlib Charts
- **Topic**: Plotting with Streamlit and Matplotlib
- **Objective**: Visualize data using Streamlit’s built-in charts and custom Matplotlib figures.
- **Purpose**: Enable quick data exploration and mapping.
- **What’s Covered**: `st.line_chart`, `st.area_chart`, `st.bar_chart`, `st.pyplot`, `st.map`.
- **How to Run**:
  ```bash
  streamlit run lecture-3.py
  ```

---

### 🔹 Lecture 4: Interactive Widgets – Buttons, Checkboxes, Selectors
- **Topic**: User input with interactive widgets
- **Objective**: Capture user input via buttons, checkboxes, radio, selectbox, and download buttons.
- **Purpose**: Make apps responsive and interactive.
- **What’s Covered**: `st.button`, `st.checkbox`, `st.radio`, `st.selectbox`, `st.download_button`.
- **How to Run**:
  ```bash
  streamlit run lecture-4.py
  ```
  > ⚠️ Requires `doggo.jpg` in the same directory for image download.

---

### 🔹 Lecture 5: Advanced Input Widgets – Sliders, Text, Number Inputs
- **Topic**: Range inputs, sliders, text/number inputs
- **Objective**: Use advanced widgets for precise user input.
- **Purpose**: Collect flexible input like ranges, passwords, weights, etc.
- **What’s Covered**: `st.multiselect`, `st.slider`, `st.select_slider`, `st.text_input`, `st.number_input`, password masking.
- **How to Run**:
  ```bash
  streamlit run lecture-5.py
  ```

---

### 🔹 Lecture 6: File Upload, Camera, Date/Time, and Color Picker
- **Topic**: Media and temporal inputs
- **Objective**: Handle file uploads, camera input, dates, times, and colors.
- **Purpose**: Support real-world inputs like images, text files, birthdates, and color choices.
- **What’s Covered**: `st.file_uploader`, `st.camera_input`, `st.date_input`, `st.time_input`, `st.color_picker`.
- **How to Run**:
  ```bash
  streamlit run lecture-6.py
  ```
  > ✅ Works out of the box if `Pillow`, `numpy`, and `io` are installed.

---

### 🔹 Lecture 7: Displaying Media – Images, Audio, Video
- **Topic**: Embedding multimedia content
- **Objective**: Display images, audio, and video files.
- **Purpose**: Build rich media apps (e.g., dashboards, galleries).
- **What’s Covered**: `st.image`, `st.audio`, `st.video`, OpenCV compatibility.
- **How to Run**:
  ```bash
  streamlit run lecture-7.py
  ```
  > ⚠️ Requires:
  > - `doggo.jpg`
  > - `audio_file.mp3`
  > - `dog_video.mp4`
  > in the same directory.

---

### 🔹 Lecture 8: Layouts – Sidebar, Columns, Tabs, Expanders, Containers
- **Topic**: Organizing app layout
- **Objective**: Structure your app using layout components.
- **Purpose**: Improve UI/UX with organized, clean, and responsive design.
- **What’s Covered**: `st.sidebar`, `st.columns`, `st.tabs`, `st.expander`, `st.container`.
- **How to Run**:
  ```bash
  streamlit run lecture-8.py
  ```
  > ⚠️ Same media files as Lecture 7 required.

---

### 🔹 Lecture 9: Status & Progress Indicators
- **Topic**: Feedback and loading indicators
- **Objective**: Show progress, spinners, balloons, and exceptions.
- **Purpose**: Enhance user experience during long operations.
- **What’s Covered**: `st.progress`, `st.spinner`, `st.balloons`, `st.snow`, `st.exception`.
- **How to Run**:
  ```bash
  streamlit run lecture-9.py
  ```

---

### 🔹 Lecture 10: Forms, Echo, Help, and Page Configuration
- **Topic**: Forms, code echoing, help, and app settings
- **Objective**: Group inputs, debug code, and configure app appearance.
- **Purpose**: Build professional forms and improve development workflow.
- **What’s Covered**: `st.form`, `st.echo`, `st.help`, `st.set_page_config`.
- **How to Run**:
  ```bash
  streamlit run lecture-10.py
  ```

---

### 🔹 Lecture 11: Dynamic Data Updates & Real-Time Charts
- **Topic**: Updating data and charts in real time
- **Objective**: Simulate live data streaming.
- **Purpose**: Create dashboards that update dynamically.
- **What’s Covered**: `add_rows()` for tables and charts, `time.sleep()` for simulation.
- **How to Run**:
  ```bash
  streamlit run lecture-11.py
  ```

---

### 🔹 Lecture 12: Session State Management
- **Topic**: Persistent user state across reruns
- **Objective**: Store and manipulate user data during app sessions.
- **Purpose**: Maintain state (e.g., login, preferences, form data).
- **What’s Covered**: `st.session_state`, key-value storage, callbacks.
- **How to Run**:
  ```bash
  streamlit run lecture-12.py
  ```

---

### 🔹 Lecture 13: Model Caching and Inference (ML Integration)
- **Topic**: Caching models and predictions
- **Objective**: Efficiently load ML models and cache inference.
- **Purpose**: Speed up apps using PyTorch and Streamlit caching.
- **What’s Covered**: `@st.cache_resource`, `@st.cache_data`, PyTorch model loading.
- **How to Run**:
  ```bash
  streamlit run lecture-13.py
  ```
  > ⚠️ Requires:
  > - `full_model.py` defining `Net()` class
  > - `final_mnist_model.pth` at `D:\datum\streamlit\final_mnist_model.pth`
  > - `torch` installed

---

## 🛠️ How to Run the Entire Course

### 1. **Install Streamlit**
```bash
pip install streamlit
```

### 2. **Install Dependencies**
```bash
pip install pandas numpy matplotlib torch pillow opencv-python
```

### 3. **Run Any Lecture**
Replace `X` with the lecture number:
```bash
streamlit run lecture-X.py
```

> 💡 Tip: Run `streamlit hello` to explore built-in examples.

---

## 🧠 Tips for Learning
- Run one lecture at a time.
- Modify the code to see how outputs change.
- Use `Ctrl+C` in the terminal to stop a running app.
- All scripts are standalone — no need to run them in sequence.

---

## 🙌 Feedback & Contributions
Feel free to open issues or pull requests if you find bugs or want to improve the course!

Happy coding with **Streamlit**! 🎉
```

---
