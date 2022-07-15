# my_scripts

# producer.py
  Script requires path to file that contains json description for kafka message
  {
  "topic": "topic name",
  "headers"(Optional) : {
    "key": "value",
    "key1": "value1"
    }
  "key"(Optional) : "any string"
  "payload": {
    }
  }
  Script produces messages into localhost:29092 
