import os
import sys
sys.path.append('..')

import lzma
import json

from config import settings
import utils

def get_cases(state,format):
    compressed_file = utils.get_cases_from_bulk(jurisdiction=state, data_format=format)
    
    cases = []
    print("File path:", compressed_file)
    with lzma.open(compressed_file) as infile:
        for line in infile:
            record = json.loads(str(line, 'utf-8'))
            cases.append(record)
    return cases