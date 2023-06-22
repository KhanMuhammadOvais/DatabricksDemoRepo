# Databricks notebook source
print ("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello World from sql"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC
# MAGIC text with a **bold** and *italicized* in it.
# MAGIC
# MAGIC Ordered List
# MAGIC 1. once
# MAGIC 2. twice
# MAGIC 3. thrice
# MAGIC
# MAGIC Unordered List
# MAGIC * apples
# MAGIC * oranges
# MAGIC
# MAGIC Images:
# MAGIC ![Google Image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
# MAGIC
# MAGIC Tables
# MAGIC | user_id | user_name |
# MAGIC |---|---|
# MAGIC |1|Adam|
# MAGIC
# MAGIC Link (or Embedded HTML): <a href="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"> Managing notebook documentation </a>
# MAGIC

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print (full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

print(files)

# COMMAND ----------

display(files)
