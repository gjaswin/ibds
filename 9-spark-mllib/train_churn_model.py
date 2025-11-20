
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.sql.functions import col

def main():

    spark = SparkSession.builder.appName("CustomerChurnPrediction").getOrCreate()

    data = spark.read.csv("customer_churn.csv", header=True, inferSchema=True)

    gender_indexer = StringIndexer(inputCol="Gender", outputCol="GenderIndex")
    data = gender_indexer.fit(data).transform(data)

    feature_cols = ["Age", "GenderIndex", "Tenure", "MonthlyCharges"]
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    data = assembler.transform(data)

    final_data = data.select("features", col("Churn").alias("label"))

    train_data, test_data = final_data.randomSplit([0.8, 0.2], seed=42)

    lr = LogisticRegression(featuresCol="features", labelCol="label")
    model = lr.fit(train_data)

    predictions = model.transform(test_data)

    evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction", labelCol="label")
    accuracy = evaluator.evaluate(predictions)

    print(f"Model Accuracy: {accuracy}")

    # Show first 10 rows
    predictions.select("label", "prediction", "probability").show(10)

    spark.stop()

if __name__ == "__main__":
    main()
