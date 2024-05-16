#!/usr/bin/python3
"""
Log parsing script
"""

import sys
import re
from typing import Dict, Union

def print_log(log: Dict[str, Union[int, Dict[str, int]]]) -> None:
    """
    Helper function to print log
    """
    print(f"File size: {log['file_size']}")
    sorted_codes = sorted(log["code_frequency"].keys())
    for code in sorted_codes:
        if log["code_frequency"][code]:
            print(f"{code}: {log['code_frequency'][code]}")


if __name__ == "__main__":
    """main"""
    regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
        }
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(regex, line)
            if match:
                line_count += 1
                status_code, file_size = match.groups()
                file_size = int(file_size)
                log["file_size"] += file_size
                log["code_frequency"][status_code] += 1
            if line_count % 10 == 0:
                print_log(log)

    finally:
        print_log(log)
