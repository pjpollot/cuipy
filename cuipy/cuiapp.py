import os

from flask import Flask, request, render_template

from typing import Callable
from sys import argv
from argparse import ArgumentParser, Namespace

from .actions import ActionLists

_cui_command = "--cui"


class CuiApp:
    def __init__(self, function: Callable[[Namespace], None], parser: ArgumentParser) -> None:
        self._action_lists = ActionLists(parser)
        parser.add_argument(_cui_command, action="store_true", help="Launch CuiApp.")
        self._parser = parser
        self._fn = function
    
    def run(self, host: int | None = None, port: int | None = None, debug: bool = False) -> None:
        args = argv[1:]
        # if the cui command is not given, then we do not run the app
        if _cui_command not in args:
            parsed_args = self._parser.parse_args()
            self._fn(parsed_args)
            return
        
        # launch web app
        app = Flask(
            __name__, 
            template_folder=os.path.join(os.path.dirname(__file__), "templates")
        )

        @app.route("/", methods=["GET", "POST"])
        def index():
            command = None
            if request.method == "POST":
                self._action_lists.update_from_web_form(request.form)
                raw_args = self._action_lists.to_args()
                namespace, _ = self._parser.parse_known_args(raw_args)
                self._fn(namespace)
                # print the python command
                raw_args = ["python", self._parser.prog] + raw_args
                command = " ".join(raw_args)
            return render_template(
                "index.html",
                title=self._parser.prog,
                description=self._parser.description, 
                action_lists=self._action_lists,
                command=command,
            )
        
        app.run(host, port, debug)

        
