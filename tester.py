# -*- coding: UTF-8 -*-
"""Run a lightweight test set on specific students."""
import subprocess
import os
from codeHelpers import Timeout

LOCAL = os.path.dirname(os.path.realpath(__file__))
week_number = 2

repos = ["pennypangCODE"]
results = []
for name in repos:
    with Timeout(5):  # should catch any rogue ∞ loops
        subprocess.call(['python',
                         './test_shim.py',
                         "week{}.tests".format(week_number),
                         "../code1161StudentRepos/{}".format(name)])

        temp_results = open(os.path.join(LOCAL, 'temp_results.json'), 'r')
        results.append(temp_results.read())
        temp_results.close()

print results
