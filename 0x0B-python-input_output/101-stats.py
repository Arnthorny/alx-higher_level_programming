#!/usr/bin/python3
"""
Script that reads from stdin line by line and computes metrics
"""
import sys


def compute_prnt_metrics(all_lines):
    """
    This function computes and prints the metrics to stdout

    Args:
        all_lines(list): ALl lines read so far from stdin
    """
    if len(all_lines) == 0:
        return

    dict_status = {'200': 0, '301': 0, '400': 0,
                   '401': 0, '403': 0, '404': 0,
                   '405': 0, '500': 0}

    file_size = 0
    for line in all_lines:
        split_line = line.split(' ')
        file_size += int(split_line[-1])
        dict_status[split_line[-2]] += 1

    print("File size: {}".format(file_size))

    for key in sorted(dict_status.keys()):
        if dict_status[key]:
            print("{}: {}".format(key, dict_status[key]))


def main():
    """
    This program serves as an entry point to the script

    It continually reads lines from stdin and stores them in
    a list then passes that list to the compute function
    when certain requirements are met
    """
    all_lines = []
    for line in sys.stdin:
        try:
            all_lines.append(line)
            if len(all_lines) == 10:
                compute_prnt_metrics(all_lines)
                all_lines = []
        except KeyboardInterrupt:
            compute_prnt_metrics(all_lines)
            all_lines = []


main()
