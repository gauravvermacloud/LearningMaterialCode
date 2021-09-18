from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DoubleType
from pyspark.sql.functions import lit
from pyspark.sql.functions import when
from pyspark.sql.functions import col

from pyspark.sql.functions import udf


spark = SparkSession.builder.master(
    "spark://laptop:7077").appName("SparkDF").getOrCreate()


schema = StructType() \
    .add("Id", IntegerType(), False)   \
    .add("Name", StringType(), False)   \
    .add("DesignationId", IntegerType(), True)   \
    .add("DOB", StringType(), True) \
    .add("DepartmentId", IntegerType(), True) \
    .add("Salary", DoubleType(), False)   \
    .add("ManagerId", IntegerType(), True)


data_frame = spark.read.options(header='True').schema(schema).csv(
    '/home/gaurav/Documents/LearningMaterial/LearningMaterialCode/code/spark/dataframe_basics/df_code/Employees.csv')
data_frame.show()

# select a column
df_select_Name = data_frame.select("Name")
df_select_Name.show()

df_select_Name = data_frame.select("Name", "Id")
df_select_Name.show()

data_frame.filter((data_frame.Id > 4) & (data_frame.Salary > 500.00)).show()

# select first two rows
print(data_frame.head(2))

df_salary_sum = data_frame.groupby('DesignationId').agg(
    {'Salary': 'sum'})
df_salary_sum.show()


# Selecting columns from a data frame
data_frame.select("Id", "Name").show()
data_frame.select(data_frame.Id, data_frame.Name).show()

# Use of withColumn
data_frame.withColumn('new_salary', data_frame.Salary * 2).show()
data_frame.withColumn('new_salary', lit(1010)).show()

data_frame.withColumn("new_salary", when(
    data_frame.DesignationId == 1, data_frame.Salary*1)
    .when(((data_frame.DesignationId > 1) & (data_frame.DesignationId <= 2)), data_frame.Salary*1.5)
    .otherwise(data_frame.Salary*2)
).show()


# We can also use a function for this work
def new_salary(designation, salary):
    if(designation == 1):
        return salary * 1.0

    if(designation > 1 and designation <= 2):
        return salary * 1.5

    return salary * 3


# The problem is that when we call a function, it doesnt give single values but entire data frame column
# not just one value, so we loop over it with this inline loop
new_salary_lambda = udf(lambda x, y: new_salary(x, y), DoubleType())


# register a function (lambda)
spark.udf.register("new_salary_lambda", new_salary_lambda)

# and call it
data_frame.withColumn("new_salary", new_salary_lambda(
    data_frame.DesignationId, data_frame.Salary)).show()
