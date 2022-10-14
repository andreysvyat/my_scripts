from kafka import KafkaProducer
import json
import sys
import uuid

COMMANDS = ['-h', '-f']


def get_value(command, default=None):
    command_id = sys.argv.index(command)
    if command_id > 0:
        return sys.argv[command_id + 1]
    else:
        if default is not None:
            return default
        else:
            print(command + " is not presented")
            exit(-1)


host = get_value('-h', 'localhost:29092')
file_path = get_value('-f')

file = open(file_path, 'r')
message = file.read()
file.close()
msg_dict = json.loads(message)


def to_headers_list(headers_map):
    headers_list = []
    if headers_map is None:
        return []
    for header in headers_map:
        header_val = headers_map[header].encode('utf-8')
        headers_list.append((header, header_val))
    return headers_list


def get_required(field):
    if field not in msg_dict:
        print(field + ' is not presented')
        exit(-1)
    else:
        return msg_dict[field]


def get_opt(field):
    if field not in msg_dict:
        print('empty ' + field)
        return None
    else:
        return msg_dict[field]


if len(sys.argv) < 2:
    print('path to msg is not specified')
    exit(-1)

headers = get_opt('headers')
payload = get_required('payload')
topic = get_required('topic')

key = str(uuid.uuid4()) if 'key' not in msg_dict else msg_dict['key']

producer = KafkaProducer(
    bootstrap_servers=host,
    security_protocol='PLAINTEXT',
    value_serializer=lambda val: json.dumps(val).encode('utf-8'),
    key_serializer=lambda s: s.encode('utf-8')
)

print(topic)

producer.send(
    topic=topic,
    value=payload,
    key=key,
    headers=to_headers_list(headers)
)
producer.flush()
producer.close()
