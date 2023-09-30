#!/usr/bin/env python3 
# coding: utf-8

# **********************************************************************************************************************
#  Copyright 2023 Vikky Masih, MFS-DSAI, IIT Guwahati, India.
#  License: Simplified BSD License
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
# disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# **********************************************************************************************************************


import re
import os
import random

files = [
    x
    for x in os.listdir(".")
    if (
        os.path.isfile(os.path.join(".", x))
        and (x.lower().endswith(".c") 
             or x.lower().endswith(".cpp") 
             or x.lower().endswith(".h")
             )
        and not (x.lower().endswith("_.c") 
                 or x.lower().endswith("_.cpp")
                 )
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
