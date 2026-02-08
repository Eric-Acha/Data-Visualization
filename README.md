#Data Visualization Project

## Overview

This project demonstrates how to analyze and visualize sales performance data using **Excel (Pivot Tables & Charts)** and **Python (Matplotlib)**. The goal is to extract actionable business insights such as top-performing products, regional performance, and sales trends.

The project is beginner-friendly, portfolio-ready, and designed to mirror real-world data analysis workflows used by data analysts and database professionals.

---

## Objectives

* Analyze sales performance data
* Identify **top-performing products and regions**
* Apply **sorting and Top 10 filtering** techniques
* Recreate Excel insights programmatically using Python
* Visualize results using clean, professional charts

---

## Dataset

* **File:** `Sales_Performance_100_Rows.xlsx`
* **Records:** 100 sales transactions
* **Key Fields:**

  * Order ID
  * Product
  * Region
  * Sales Amount
  * Quantity Sold
  * Order Date

The dataset simulates a small-to-medium business sales environment.

---

## Tools & Technologies

### Excel

* Pivot Tables
* Pivot Charts
* Sort (Largest → Smallest)
* Top 10 Filters

### Python

* Python 3.x
* Pandas
* Matplotlib

---

## Analysis Performed

### 1️⃣ Excel Analysis

Using Pivot Tables, the following insights were generated:

* Total sales by **Product**
* Total sales by **Region**
* Sorted results from **largest to smallest**
* Applied **Top 10 filters** to highlight best performers
* Created column and bar charts for quick comparison

### 2️⃣ Python Visualization

The same insights were rebuilt using Python:

* Loaded Excel data with Pandas
* Aggregated sales by product and region
* Sorted results programmatically
* Visualized data using Matplotlib bar charts

This demonstrates how Excel-based insights can scale into automated analytics workflows.

---

## Sample Visualizations

* 📦 Top Products by Sales
* 🌍 Sales by Region
* 📈 Comparative Bar Charts

(All charts generated using Matplotlib with default styling for clarity.)

---

## Project Structure

```
Data Visualization/
│
├── Sales_Performance_100_Rows.xlsx
├── sales_dashboard.py
├── README.md
```

---

## How to Run the Python Script

1. Navigate to the project folder:

```bash
cd "Data Visualization"
```

2. Install dependencies:

```bash
pip install pandas matplotlib
```

3. Run the script:

```bash
python sales_visualization.py
```

---

## Key Takeaways

* Excel Pivot Tables are powerful for quick insights
* Python provides automation, scalability, and reproducibility
* Sorting and Top-N analysis are essential business intelligence skills
* Visual storytelling improves decision-making

---

## Future Improvements

* Add time-series sales trend analysis
* Export charts automatically to image files
* Integrate SQL for database-driven analytics
* Build an interactive dashboard (Streamlit or Power BI)

---

## Author

**Eric Acha**
Database & Data Analytics Professional

📌 *This project is part of my data analytics and visualization portfolio.*

---

⭐ If you found this project helpful, feel free to star the repository and connect with me on GitHub!



