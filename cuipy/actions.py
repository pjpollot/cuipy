from werkzeug.datastructures import ImmutableMultiDict
from typing import Any
from dataclasses import dataclass
from argparse import (
    ArgumentParser,
    Namespace,  
    Action,
    _StoreAction, 
    _StoreConstAction,
    _AppendAction,
    _AppendConstAction,
    _CountAction,
    _StoreTrueAction,
    _HelpAction,
    ArgumentError,
)


class ActionLists:
    def __init__(self, parser: ArgumentParser) -> None:
        self._store = {}
        self._store_const = {}
        self._append = {} # TODO
        self._append_const = {} # TODO
        self._count = {} # TODO
        for action in parser._actions:
            if isinstance(action, _StoreAction):
                self._store[action.dest] = {
                    "option_strings": action.option_strings,
                    "type": action.type,
                    "value": action.default,
                    "required": action.required,
                    "help": action.help,
                }
            elif isinstance(action, _StoreConstAction):
                self.store_const[action.dest] = {
                    "option_strings": action.option_strings,
                    "const": action.const,
                    "triggered": action.const == action.default,
                    "help": action.help,
                }
            elif not isinstance(action, _HelpAction):
                raise ArgumentError(action, f"Argument {action.dest} is encapsulated in the class {type(action)} that is not yet handled by CuiPy.")


    def update_from_web_form(self, form: ImmutableMultiDict) -> None:
        # reset first the constant actions
        for action_dict in self._store_const.values():
            action_dict["triggered"] = False
        # then explore the form
        for full_dest, value in form.items():
            group, dest = full_dest.split("::")
            action_dict = getattr(self, group)[dest]
            if group == "store":
                action_dict["value"] = value if action_dict["type"] is None else action_dict["type"](value)
            elif group == "store_const":
                action_dict["triggered"] = True
            # TODO: the rest of the actions
            else:
                raise ValueError(f"Invalid group ({group}) or invalid argument ({dest}) inside the CuiApp form.")
            
    
    def to_namespace(self) -> Namespace:
        namespace = Namespace()
        for dest, action_dict in self._store.items():
            setattr(namespace, dest, action_dict["value"])
        for dest, action_dict in self._store_const.items():
            setattr(namespace, dest, action_dict["const"]) if action_dict["triggered"] else setattr(namespace, dest, None)
        # TODO: the rest of the actions
        return namespace
    

    def to_args(self) -> list[str]:
        args = []
        for action_dict in self._store.values():
            if len(action_dict["option_strings"]) > 0 and action_dict["value"] is not None:
                args += [action_dict["option_strings"][0], str(action_dict["value"])]
            elif len(action_dict["option_strings"]) == 0 and action_dict["value"] is not None:
                args += [str(action_dict["value"])]
        for action_dict in self._store_const.values():
            if action_dict["triggered"]:
                args += [action_dict["option_strings"][0]]
        # TODO: the rest of the actions
        return args
    

    @property
    def store(self) -> dict:
        return self._store
    
    @property
    def store_const(self) -> dict:
        return self._store_const
