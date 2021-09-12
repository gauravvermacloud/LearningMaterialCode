from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DoubleType


spark = SparkSession.builder.master(
    "spark://laptop:7077").appName("SparkDF").getOrCreate()

data_frame = spark.read.csv(
    '/home/gaurav/Documents/LearningMaterial/LearningMaterialCode/code/spark/dataframe_basics/df_code/Employees.csv')

data_frame.show()


data_frame = spark.read.option("header", True).csv(
    '/home/gaurav/Documents/LearningMaterial/LearningMaterialCode/code/spark/dataframe_basics/df_code/Employees.csv')

data_frame.show()

data_frame = spark.read.options(header='True').csv(
    '/home/gaurav/Documents/LearningMaterial/LearningMaterialCode/code/spark/dataframe_basics/df_code/Employees.csv')

data_frame.show()


data_frame.show()

data_frame = spark.read.options(header='True', inferSchema='True').csv(
    '/home/gaurav/Documents/LearningMaterial/LearningMaterialCode/code/spark/dataframe_basics/df_code/Employees.csv')
data_frame.printSchema()
data_frame.show()


schema = StructType() \
    .add("Id", IntegerType(), False)   \
    .add("Name", StringType(), False)   \
    .add("DesignationId", IntegerType(), True)   \
    .add("DOB", DateType(), True) \
    .add("DepartmentId", IntegerType(), True) \
    .add("Salary", DoubleType(), False)   \
    .add("ManagerId", IntegerType(), True)


data_frame = spark.read.options(header='True').schema(schema).csv(
    '/home/gaurav/Documents/LearningMaterial/LearningMaterialCode/code/spark/dataframe_basics/df_code/Employees.csv')
data_frame.printSchema()
data_frame.show()

print(data_frame.columns)

print(data_frame.describe().show())
