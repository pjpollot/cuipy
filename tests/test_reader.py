import os

from cuipy.script_reader import get_script_info

def test_script_reader():
    script_path = os.path.join(os.path.dirname(__file__), "example_script.py")
    true_usage = "example_script.py [-h] [-a ARGUMENT_1] [-b]"
    true_arguments = {
        "-a": ["ARGUMENT_1"],
        "-b": [],
        "-h": [],
    }
    script_info = get_script_info(script_path)
    assert script_info.usage == true_usage
    for argname, elements in script_info.arguments.items():
        assert true_arguments[argname] is not None
        for element in elements:
            assert element in true_arguments[argname]
    