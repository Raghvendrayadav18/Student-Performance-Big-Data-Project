# 📊 Student Marks Analysis using Hadoop & Hive

## 📌 Project Overview

This project demonstrates how to analyze student marks data using **Hadoop MapReduce** and **Hive**.
The dataset contains student names, subjects, and marks, and we perform data processing and analysis on it.

---

## 🎯 Objectives

* Understand Hadoop ecosystem (HDFS + MapReduce)
* Perform data processing using Python (Mapper & Reducer)
* Store and query data using Hive
* Generate insights like average, total, max, min, and top performers

---

## 🛠️ Technologies Used

* Hadoop (HDFS + MapReduce)
* Hive
* Python
* Linux (Cloudera VM)

---

## 📂 Dataset

The dataset contains the following fields:

Name, Subject, Marks

Example:
Rahul,Math,85
Priya,English,92

---

## ⚙️ Implementation Steps

### 1️⃣ Data Preparation

* Created dataset file: `cleaned_dataset.csv`
* Stored in HDFS `/input` directory

---

### 2️⃣ MapReduce Implementation

#### Mapper

Processes input data and emits key-value pairs.

#### Reducer

Aggregates values to calculate total marks per subject.

---

### 3️⃣ HDFS Operations

* Created input directory
* Uploaded dataset
* Removed previous outputs

---

### 4️⃣ MapReduce Execution

Command used:

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files Mapper.py,Reducer.py \
-mapper Mapper.py \
-reducer Reducer.py \
-input /input/cleaned_dataset.csv \
-output /output
```

---

### 5️⃣ Output Result

```
English    256
Math       337
Science    226
```

---

### 6️⃣ Hive Implementation

#### Table Creation

```
CREATE TABLE student_marks (
    name STRING,
    subject STRING,
    marks INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

#### Load Data

```
LOAD DATA LOCAL INPATH '/home/cloudera/Desktop/StudentProject/cleaned_dataset.csv'
INTO TABLE student_marks;
```

---

## 📊 Analysis Using Hive Queries

### 🔹 Average Marks

```
SELECT subject, AVG(marks) FROM student_marks GROUP BY subject;
```

### 🔹 Total Marks

```
SELECT subject, SUM(marks) FROM student_marks GROUP BY subject;
```

### 🔹 Top 3 Students

```
SELECT name, marks FROM student_marks ORDER BY marks DESC LIMIT 3;
```

### 🔹 Maximum Marks

```
SELECT subject, MAX(marks) FROM student_marks GROUP BY subject;
```

### 🔹 Minimum Marks

```
SELECT subject, MIN(marks) FROM student_marks GROUP BY subject;
```

### 🔹 Count of Students

```
SELECT subject, COUNT(*) FROM student_marks GROUP BY subject;
```

---

## 📈 Results

| Subject | Total Marks | Average Marks |
| ------- | ----------- | ------------- |
| English | 256         | 85.33         |
| Math    | 337         | 84.25         |
| Science | 226         | 75.33         |

---

## 🧠 Conclusion

This project shows how **Hadoop MapReduce** and **Hive** can efficiently process and analyze structured data.
It helps in understanding big data processing and query optimization techniques.

---


## 👨‍💻 Author

**Raghvendra Pratap Yadav**
BCA (Data Science & AI)
1240258347
---
