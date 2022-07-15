# my_scripts

## producer.py
Script requires path to file as first parameter that contains json description for kafka message
```
{
	"topic": "topic name",
	"headers": {
		"key": "value",
		"key1": "value1"
		},
	"key": "string value",
	"payload": {}
}
```
Script produces messages into localhost:29092 
