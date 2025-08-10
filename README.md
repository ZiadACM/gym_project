# 🏋️ Gym Member Exercise Tracking Analysis (Power BI Project)

## 📌 Project Overview

This project performs a comprehensive analysis on gym members’ exercise tracking data. The goal is to extract meaningful insights into **member demographics**, **workout habits**, and **performance metrics**, laying the groundwork for personalized fitness recommendations and strategic gym management.

---

## 🎯 Problem Statement / Objectives

Transform raw exercise data into actionable insights by:

* Understanding member demographics and health metrics.
* Analyzing workout types and their impact on calories burned and session durations.
* Investigating correlations between health indicators (e.g., fat percentage, BMI) and workout behavior.
* Preparing for the development of a **Power BI** dashboard for dynamic exploration.

---

## 📂 Data Source

* **Dataset:** [Gym Members Exercise Tracking Dataset (Kaggle)](https://www.kaggle.com)
* **Format:** CSV file
* **Filename:** `gym_members_exercise_tracking.csv`

**Key Columns:**
`Age`, `Gender`, `Weight (kg)`, `Height (m)`, `Max_BPM`, `Avg_BPM`, `Resting_BPM`, `Session_Duration (hours)`, `Calories_Burned`, `Workout_Type`, `Fat_Percentage`, `Water_Intake (liters)`, `Workout_Frequency (days/week)`, `Experience_Level`, `BMI`

---

## 🛠️ Tools & Technologies

| Purpose                     | Tools/Technologies                    |
| --------------------------- | ------------------------------------- |
| Data Manipulation & Storage | Python (pandas), SQLite               |
| EDA & Visualization         | Jupyter Notebook, matplotlib, seaborn |
| Dashboarding                | Power BI (planned for future phase)   |
| Version Control             | Git, GitHub                           |
| Documentation               | Markdown                              |

---

## 📁 Project Structure

```bash
your-powerbi-gym-project/
├── data/
│   ├── raw/
│   │   └── gym_members_exercise_tracking.csv         # Original dataset
│   └── processed/
│       ├── gym_data.db                                # SQLite DB (generated)
│       └── cleaned_gym_members_data.csv               # Cleaned data (generated)
├── notebooks/
│   └── eda_gym_members.ipynb                          # Python EDA notebook
├── sql/
│   ├── create_table.sql                               # Optional schema script
│   └── queries.sql                                    # SQL queries
├── powerbi/                                           # Power BI (future phase)
│   ├── gym_dashboard.pbix
│   └── dashboard_screenshots/
├── setup_gym_db.py                                    # Database setup script
├── .gitignore                                         # Files to ignore in Git
└── README.md                                          # This documentation file
```

---

## ✅ Phase 1: Setup & Key Questions

**Objectives Defined**
Set up project goals, prepare dataset, and define guiding questions:

### I. Demographics & Health Metrics

* What's the age and gender distribution?
* What are the average BMI, weight, and fat percentage?

### II. Workout Habits & Performance

* Most common workout types?
* Avg. session duration and calories burned?
* Heart rate trends (Max, Avg, Resting)?

### III. Key Relationships (Hypotheses)

* Does experience level correlate with lower fat percentage?
* Relationship between session duration and calories burned?
* Workout type vs. efficiency (calories/session)?
* Differences across gender and age?
* Water intake vs. performance?
* BMI vs. fat percentage?

---

## 📄 Phase 2: Data Acquisition & Storage (SQL)

### 💾 SQLite Workflow

* **Connect**: Create `gym_data.db` using `sqlite3`.
* **Schema**: Define `gym_members` table with proper data types.
* **Load Data**: Use `pandas.to_sql()` to insert CSV data.
* **Verify**: Run `SELECT * LIMIT 5` to confirm import.

### ✅ Error Handling:

Handled `FileNotFoundError`, DB errors, and used `try-except-finally` for robust execution in `setup_gym_db.py`.

### 🔑 SQL Operations Demonstrated:

* `CREATE TABLE`
* `INSERT`, `SELECT`
* `GROUP BY`, `ORDER BY`, `LIMIT`
* Aggregations: `AVG()`, `SUM()`, `COUNT()`

---

## 📊 Phase 3: Exploratory Data Analysis (Python)

### 🔍 EDA Steps

1. **Load & Inspect**

   * `pd.read_csv()`, `.info()`, `.describe()`, `.unique()`

2. **Cleaning**

   * Removed duplicates
   * Confirmed no missing values
   * Converted data types

3. **Feature Engineering**

   * `Age_Group` using `pd.cut()`
   * `Weight_Class` from BMI
   * `BPM_Zone` (Low, Moderate, High) from `Avg_BPM`

4. **Visual Analysis**

   * Histograms, bar plots, scatterplots, heatmaps

### 📈 Sample Insights

* **Age** peaks: early 20s & late 40s.
* **Workout Type vs. Calories**: Some types burn significantly more.
* **Experience Level vs. Fat %**: More experienced = lower fat %.
* **Strong Correlations**:

  * `Calories_Burned` ↔ `Session_Duration` (0.91)
  * `Workout_Frequency` ↔ `Experience_Level` (0.84)
  * `Fat_Percentage` ↔ Workout metrics (negative)

---

## ▶️ How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-powerbi-gym-project.git
cd your-powerbi-gym-project
```

### 2. Add the Dataset

Place `gym_members_exercise_tracking.csv` inside `data/raw/`.

### 3. Install Dependencies

```bash
pip install pandas matplotlib seaborn jupyter
```

### 4. Set Up SQLite Database

```bash
python setup_gym_db.py
```

This creates the SQLite DB: `data/processed/gym_data.db`.

### 5. Perform EDA in Jupyter

```bash
jupyter notebook
```

Run all cells in `notebooks/eda_gym_members.ipynb` to clean, analyze, and generate `cleaned_gym_members_data.csv`.

---

## 📊 Next Phase: Power BI Dashboard

* Import the cleaned CSV into Power BI
* Define relationships, DAX measures
* Build interactive visuals for:

  * Member segmentation
  * Workout performance
  * Health trends & KPIs

---

## 📌 Credits & License

* **Dataset**: Provided by [Kaggle](https://www.kaggle.com)
