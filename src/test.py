#!/usr/bin/env python3

# Test script to check that I know how nohup and & work

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
args = parser.parse_args()

import time
from datetime import datetime

print(f"started {args.input}")
time.sleep(10)
now = datetime.now()
print(f"finished {args.input} at {now}")

