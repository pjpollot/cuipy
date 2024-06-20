import os
from io import StringIO

from sys import executable

from dataclasses import dataclass

@dataclass
class ScriptInfo:
    usage: str
    arguments: dict[str, list[str]]


_usage_line_header = "usage: "


def get_script_info(script_path: str) -> ScriptInfo:
    info = os.popen(f"{executable} {script_path} -h").read()
    # get usage string
    with StringIO(info) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines) and not lines[i].startswith(_usage_line_header):
            i += 1
        usage = lines[i].split(_usage_line_header)[1]
    usage = usage.split("\n")[0]
    # fetch arg substrings 
    arguments = {}
    for substring in usage.split("[")[1:]:
        arg_substring = substring.split("]")[0]
        arg_parse = arg_substring.split(" ")
        arguments[arg_parse[0]] = []
        if len(arg_parse) > 1:
            for sub_argument in arg_parse[1:]:
                arguments[arg_parse[0]].append(sub_argument)
    return ScriptInfo(usage, arguments)
