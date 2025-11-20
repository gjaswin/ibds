#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    for word in re.findall(r"\w+", line.lower()):
        if word:
            print(f"{word}\t1")
