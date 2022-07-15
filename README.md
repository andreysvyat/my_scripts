# my_scripts

## producer.py
Script produces message configured with file <br/>
> -f path/to/file - required, set path to message configuration file <br/>
> -h host:port - option, default localhost:29092, set host where is hosted kafka <br/>

### message configuration file example <br/>
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

