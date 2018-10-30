"""
Loki init
2018/10/30: example to replace \r and \n with a space in Loki logging
"""

import json

STDOUT_CSV = 0
STDOUT_LINE = 1
FILE_CSV = 2
FILE_LINE = 3
SYSLOG_LINE = 4
FORCE_JSON = True


def Escape(data):
    return data.replace('\n', '').replace('\r', '').replace(',', '')


def LokiCustomFormatter(filetype, format, *args):
    if FORCE_JSON and filetype not in (STDOUT_LINE, STDOUT_CSV):
        return json.dumps({"timestamp": args[0],
                           "hostname": args[1],
                           "message_type": args[2],
                           "module": args[3],
                           "message": Escape(args[4])}) + args[5]
    if filetype in (FILE_CSV, FILE_LINE):
        args = args[0:4] + (Escape(args[4]),) + args[5:]
    return format.format(*args)
