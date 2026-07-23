from kafka import KafkaProducer
import pandas as pd
import json


def main():
    # Create Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )

    # Load validated records
    valid_books = pd.read_csv("/content/valid_books.csv")

    # Send records to Kafka
    for _, record in valid_books.iterrows():
        producer.send("books", value=record.to_dict())

    producer.flush()
    producer.close()

    print(f"Successfully sent {len(valid_books)} records to the 'books' topic.")


if __name__ == "__main__":
    main()
  Add Kafka producer
