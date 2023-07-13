#!/usr/bin/python3
"""
Script that reads from stdin line by line and computes metrics
"""
import sys
import datetime


def verify_line(line):
    """
    This function verifies that the input format of the
    lines are correct before computing metrics

    Args:
        line(str): String containg the line input to be verified

    Returns:
        True if line is valid else False
    """

    l_a = line.split(" ")

    if len(l_a) != 9:
        return False

    stat_codes = ("200", "301", "400", "401", "403", "404", "405", "500")
    get_str = '"GET /projects/260 HTTP/1.1"'
    c_ip = l_a[0].split('.')
    if len(c_ip) != 4 and all(x.isdigit() for x in c_ip):
        return False
    elif l_a[1] != '-':
        return False
    try:
        datetime.datetime.fromisoformat(((f"{l_a[2]} {l_a[3]}")[1:-1]))
    except ValueError:
        return False

    if f"{l_a[4]} {l_a[5]} {l_a[6]}" != get_str:
        return False
    elif l_a[7] not in stat_codes or not l_a[8].rstrip('\n').isdigit():
        return False

    return True


def compute_prnt_metrics(all_lines):
    """
    This function computes and prints the metrics to stdout

    Args:
        all_lines(list): ALl lines read so far from stdin
    """
    dict_status = {'200': 0, '301': 0, '400': 0,
                   '401': 0, '403': 0, '404': 0,
                   '405': 0, '500': 0}
    file_size = 0
    tmp_str = ""

    for line in all_lines:
        if not verify_line(line):
            continue
        split_line = line.split(' ')
        file_size += int(split_line[-1][0:-1])
        dict_status[split_line[-2]] += 1

    for key in sorted(dict_status.keys()):
        if dict_status[key]:
            tmp_str += "{}: {}\n".format(key, dict_status[key])

    sys.stdout.write("File size: {}\n".format(file_size))
    sys.stdout.write(tmp_str)


def main():
    """
    This program serves as an entry point to the script

    It continually reads lines from stdin and stores them in
    a list then passes that list to the compute function
    when certain requirements are met
    """
    all_lines = []
    try:
        for line in sys.stdin:
            all_lines.append(line)
            if len(all_lines) and len(all_lines) % 10 == 0:
                compute_prnt_metrics(all_lines)
                continue
        compute_prnt_metrics(all_lines)
    except KeyboardInterrupt as e:
        compute_prnt_metrics(all_lines)
        raise e


main()
