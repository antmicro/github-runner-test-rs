#!/usr/bin/python

import argparse
import json
import os
import os.path
part_of_tests = sorted(["a", "b", "c"])

print(json.dumps([f"{node}" for node in part_of_tests]))
