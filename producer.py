from kafka import KafkaProducer
import json
import sys
import uuid



file_path = sys.argv[1]
file = open(file_path, 'r')
message = file.read()
msg_dict = json.loads(message)

def to_headers_list(headers):
    headers_list = []
    if headers is None:
        return []
    for header in headers:
        header_val = headers[header].encode('utf-8')
        headers_list.append((header, header_val))
    return headers_list
    

def get_required(key):
    if key not in msg_dict:
        print(key + ' is not presented')
        exit()
    else:
        return msg_dict[key]

def get_opt(key):
    if key not in msg_dict:
       print('empty ' + key)
       return None
    else:
       return msg_dict[key]


if len(sys.argv) < 2:
    print('path to msg is not specified')
    exit()


headers = get_opt('headers')
payload = get_required('payload')
topic = get_required('topic')

key = str(uuid.uuid4()) if 'key' not in msg_dict else msg_dict['key']

producer = KafkaProducer(
    bootstrap_servers = 'localhost:29092',
    security_protocol = 'PLAINTEXT',
    value_serializer = lambda val: json.dumps(val).encode('utf-8'),
    key_serializer = lambda s: s.encode('utf-8')
    )

print(topic)

producer.send(
    topic = topic,
    value = payload,
    key = key,
    headers = to_headers_list(headers)
)
producer.flush()
print('sent')
