# PRODIGY_DS_05

## Prodigy InfoTech Data Science Internship – Task 05

### Traffic Accident Data Analysis

---

## 📌 Task Overview

The objective of this task is to analyze traffic accident data to identify patterns related to:

- Road conditions
- Weather conditions
- Time of day
- Accident severity
- Geographic accident density

The analysis is performed using the **US Accidents Dataset (March 2023)**.

---

## 📊 Dataset

**Dataset:** US Accidents (March 2023)

**Source:** Kaggle  
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

The dataset contains millions of traffic accident records collected across the United States.

Because of the large dataset size, the CSV file is **not included in this repository**.

### Dataset Setup

Download:

```text
US_Accidents_March23.csv

from Kaggle and place it inside:

data/US_Accidents_March23.csv

The Python script automatically reads the dataset from this location.

🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
⚙️ Data Processing

Due to the large size of the dataset, the analysis processes the CSV file in chunks of 200,000 records to reduce memory usage.

The analysis uses the following variables:

Severity
Start_Time
Start_Lat
Start_Lng
Weather_Condition
Junction
Crossing
Traffic_Signal
🔍 Analysis Performed
1. Accident Records by Hour

The analysis extracts the hour from the accident start time and calculates the number of accident records for each hour of the day.

2. Weather Condition Analysis

The ten most frequently recorded weather conditions are identified and visualized.

3. Accident Severity by Road Context

The relationship between accident severity and road contexts such as:

Junction
Crossing
Traffic Signal

is analyzed.

4. Geographic Accident Density

A geographic hexbin visualization is created using a random sample of accident locations to show the distribution of reported accident records across the United States.

📈 Key Findings

A total of:

7,728,394 accident records

were processed.

Peak Accident Hour

07:00

with:

525,763 accident records

Most Common Weather Condition

Fair

with:

2,560,802 accident records

These values are generated directly by the analysis script.

📊 Visualizations
Accident Records by Hour & Weather

This visualization shows accident-record counts by hour of the day and the ten most common recorded weather conditions.

Accident Severity by Road Context

This heatmap shows accident severity counts associated with different road contexts.

Geographic Accident Hotspots

This visualization shows the geographic density of sampled accident records across the United States.

Note: The hotspot visualization represents reported-record density. It is not risk-adjusted for traffic volume, population, or exposure. Therefore, a higher record density does not by itself establish a higher accident risk.

📁 Project Structure
PRODIGY_DS_05/
│
├── data/
│   └── .gitkeep
│
├── outputs/
│   ├── accident_hotspots.png
│   ├── road_context_severity.png
│   ├── time_and_weather_patterns.png
│   └── findings.txt
│
├── task05.py
├── README.md
└── requirements.txt

The large US_Accidents_March23.csv dataset is intentionally excluded from the repository.

▶️ How to Run
1. Clone the Repository
git clone https://github.com/Vedanshu-Fegade/PRODIGY_DS_05.git
2. Navigate to the Project
cd PRODIGY_DS_05
3. Install Dependencies
pip install -r requirements.txt
4. Download the Dataset

Download US_Accidents_March23.csv from Kaggle and place it in:

data/US_Accidents_March23.csv
5. Run the Analysis
python task05.py

The script will process the dataset and save the generated visualizations and findings inside the outputs folder.

📄 Output Files
The analysis generates:
outputs/
│
├── accident_hotspots.png
├── road_context_severity.png
├── time_and_weather_patterns.png
└── findings.txt

The Python script creates these outputs automatically.

🎯 Learning Outcomes

Through this task, I practiced:

Large-scale dataset processing
Chunk-based CSV processing
Pandas data analysis
Data aggregation
Time-based analysis
Weather-condition analysis
Accident severity analysis
Geographic data visualization
Heatmap visualization
Hexbin visualization
Matplotlib
Seaborn
Memory-efficient data processing

💼 Internship
Prodigy InfoTech – Data Science Internship
Task 05 – Traffic Accident Data Analysis

👨‍💻 Author
Vedanshu Fegade
