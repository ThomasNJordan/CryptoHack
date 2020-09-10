from pwn import *
import Crypto.Util.number
import json
import base64
import codecs

list_str = []
i = 0

conn = remote('socket.cryptohack.org', 13377)

while i < 101:
    print(i)
    decode_json = json.loads(conn.recvline())

    if 'type' not in decode_json:
        print(decode_json)
        break

    print(decode_json)
    if decode_json['type'] == 'hex':
        hex_string = bytes.fromhex(decode_json["encoded"])
        print(hex_string)
        encoded_str = hex_string.decode("utf-8")
        hex_json = json.dumps({"type":"hex","decoded":encoded_str})

        print("hex json is " + json.dumps(hex_json))
        conn.send(hex_json)
    elif decode_json['type'] == 'utf-8':
        json_list = decode_json['encoded']
        list_str = []
        for s in json_list:
            list_str.append(chr(s))
        new_list = ''.join(list_str)
        ascii_json = json.dumps({"type":"utf-8","decoded":new_list})

        print("ascii json is " + json.dumps(ascii_json))
        conn.send(ascii_json)
    elif decode_json['type'] == 'bigint':
        big_num = decode_json['encoded']
        print(big_num)
        num = Crypto.Util.number.long_to_bytes(int(big_num, 0))
        bigint_json = json.dumps({"type":"bigint","decoded":num.decode("utf-8")})

        print("big int json is " + bigint_json)
        conn.send(bigint_json)
    elif decode_json['type'] == 'base64':
        base64_string = decode_json['encoded']
        print(base64_string)
        encoded_bytes = base64.b64decode(base64_string)
        encoded_str = encoded_bytes.decode("utf-8")
        base64_json = json.dumps({"type":"base64","decoded":encoded_str})

        print("base64 json is " + json.dumps(base64_json))
        conn.send(base64_json)
    elif decode_json['type'] == 'rot13':
        decoded = codecs.decode(decode_json['encoded'], 'rot13')
        print(decoded)
        rot13_json = json.dumps({"type":"rot13","decoded":decoded})

        print("rot13 json is " + rot13_json)
        conn.send(rot13_json)
    else:
        print(decode_json)
    i += 1