# 📊 Pandas CSV Data Analysis

A beginner-friendly Python project that demonstrates how to use the **Pandas** library to read, explore, and analyze CSV files.

## 🚀 Features

* Read CSV files using `pd.read_csv()`
* Display the complete dataset
* View the first rows with `head()`
* View the last rows with `tail()`
* Display random rows using `sample()`
* Check the dataset shape (`rows × columns`)
* Explore column names and data types
* Access individual columns
* Find minimum and maximum values
* Filter rows based on conditions
* Perform basic DataFrame exploration

## 🛠 Technologies Used

* Python 3
* Pandas
* Google Colab (Optional)
* VS Code (Optional)

## 📚 Concepts Covered

* Importing the Pandas library
* Reading CSV files
* Creating and working with DataFrames
* Inspecting datasets
* Accessing columns
* Data filtering
* Basic data analysis techniques

## 💻 Example

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.tail())
print(df.sample())
print(df.shape)
print(df.columns)
print(df.dtypes)
```

## 📦 Installation

Install Pandas before running the project:

```bash
pip install pandas
```

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/pandas-csv-data-analysis.git
```

2. Move into the project directory.

```bash
cd pandas-csv-data-analysis
```

3. Place the `data.csv` file inside the project folder.

4. Run the program.

```bash
python Pandas.py
```

You can also run the project in **Google Colab** by uploading the CSV file and updating its path.

## 🎯 Learning Objectives

By completing this project, you will learn how to:

* Read CSV files with Pandas
* Explore and inspect datasets
* Access rows and columns
* Filter data using conditions
* Analyze datasets efficiently
* Work with DataFrames
* Build a strong foundation for data analysis and machine learning

## 📁 Project Structure

```text
├── Pandas.py
├── data.csv
├── README.md
```

## 👨‍💻 Author

Created as a beginner-friendly Python and Pandas practice project for learning data analysis fundamentals.
