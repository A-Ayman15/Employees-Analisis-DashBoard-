# Employee Analytics: End-to-End Data Pipeline & Dashboard

![Dashboard Header](Employees%20analisis%20Dashboard.jpeg)

## 📌 Project Overview
This repository contains a comprehensive HR analytics project designed to track workforce performance, salary distributions, and regional demographics. The project demonstrates a full data lifecycle: from raw data cleaning using **Python** to interactive storytelling via **Tableau**.

## 📂 Repository Structure
* `employees_company.py`: Python script for data wrangling and preprocessing.
* `Cleaned_Employee_Data.csv`: The final processed dataset ready for analysis.
* `Employees Analysis Dashboard.twb`: Tableau Workbook containing the visualizations.
* `Employees analisis Dashboard.jpeg`: High-resolution export of the final dashboard.

## 🛠️ Technical Implementation

### 1. Data Cleaning (Python/Pandas)
The raw dataset required significant cleaning to ensure "Single Source of Truth" reporting. Key transformations included:
* **Missing Value Imputation:** Filled missing experience and salary data using statistical measures (mean/mode).
* **Feature Engineering:** * Created `Full Name` by merging name components.
    * Developed a `total Monthly salary` metric: 
      `Monthly Salary + (Overtime Hours * (Monthly Salary / 240 hours))`
* **Outlier Removal:** Applied the IQR (Interquartile Range) method to remove noise from financial and experience data.

### 2. Data Visualization (Tableau)
The dashboard provides an interactive overview of the workforce across the MENA region (Egypt, UAE, Saudi Arabia, etc.).

**Key Metrics Tracked:**
* **Headcount Dynamics:** Employee distribution by Gender and Department.
* **Financial Oversight:** Total monthly salary expenditure and average Job Rates.
* **Work-Life Balance:** Analysis of Overtime Hours vs. Sick/Unpaid Leaves.
* **Experience Profiles:** Seniority distribution (0 to 13+ years).

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Pandas & NumPy libraries
* Tableau Desktop or Tableau Public

  ## 🤝 Connect with Me
* **LinkedIn:** (https://www.linkedin.com/in/ahmedayman5000/)
* **Email:** 5000ahmedayman5000@gmail.com

### Installation
1. Clone the repository:
   ```bash
   git clone :  https://github.com/A-Ayman15/Employees-Analisis-DashBoard-
