#!/usr/bin/env python3 
# coding: utf-8

import re
import os
import random

files = [
    x
    for x in os.listdir(".")
    if (
        os.path.isfile(os.path.join(".", x))
        and x.endswith(".c")
        and not x.lower().endswith("_.c")
    )
]
regexpr = re.compile(r"\bmain[\s]?\(")
for k in files:
    with open(os.path.join(".", k), "r") as file:
        content = file.read().strip()
    output = regexpr.subn(f"main_{random.randint(10000,99999)}(", content)
    if output[1] > 0:
        with open(os.path.join(".", k), "w") as file:
            file.write(output[0])
