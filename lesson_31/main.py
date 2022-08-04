#!/usr/bin/python3

from solution_01 import solution_01
from lib.std.utils import test
import base64


def xor_cipher(text: str, key: str) -> str:
    result = ""
    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return result


if __name__ == "__main__":
    test = "Очень длинный текст для проверки программы"
    key = "test"

    string = xor_cipher(test, key)

    message_bytes = string.encode("utf-8")
    base64_bytes = base64.b64encode(message_bytes)

    print(base64_bytes.decode("ascii"))

    old_dict = {"1": "Alex", "22": "Olga", "333": "Roma"}

    new_dict = {
        key: value
        for key, value in old_dict.items()
        if len(value) > 3
    }
