import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database and fetch data
conn = sqlite3.connect('people_data.db')
query = "SELECT * FROM people"
df = pd.read_sql_query(query, conn)
conn.close()


# Visualization 1: Pie Chart for Education Levels
education_counts = df['education'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(education_counts, labels=education_counts.index,
        autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Education Levels')
plt.show()

# Visualization 2: Bar Chart for Average Salary by Department
avg_salary_department = df.groupby('department')['salary'].mean()
plt.figure(figsize=(10, 6))
avg_salary_department.plot(kind='bar', color='skyblue')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.title('Average Salary by Department')
plt.xticks(rotation=45)
plt.show()

# Visualization 3: Scatter Plot for Age vs. Salary
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['salary'], color='green', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs. Salary')
plt.show()
