from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Step 1: Initialize Spark Session
spark = SparkSession.builder.appName("StudentAnalysis").getOrCreate()

# Step 2: Load CSV file
df = spark.read.csv("data/student.csv", header=True, inferSchema=True)

# Step 3: Show schema and data
df.printSchema()
df.show()

# Step 4: Filter students with marks > 60
filtered_df = df.filter(df.Marks > 60)
filtered_df.show()

# Step 5: Average marks by Department
avg_marks = df.groupBy("Department").agg(avg("Marks").alias("Average_Marks"))
avg_marks.show()

# Step 6: Stop Spark
spark.stop()

File : data/student.csv

Name,Department,Marks
Asha,CSE,78
Ravi,IT,58
Kiran,CSE,82
Divya,ECE,45
Rahul,IT,65
Sneha,ECE,71

Output:

|Name |Department|Marks|

|Asha  |CSE              |78   |
|Ravi   |IT                 |58   |
|Kiran|CSE               |82   |
|Divya|ECE               |45   |
|Rahul|IT                   |65   |
|Sneha|ECE               |71   |














Filtered (Marks > 60):

|Name |Department|Marks|

|Asha |CSE               |78   |
|Kiran|CSE              |82   |
|Rahul|IT                 |65   |
|Sneha|ECE             |71   |
 
Average Marks by Department:

|Department|Average_Marks|

|CSE              |80.0         |
|IT                  |61.5         |
|ECE              |58.0         |















