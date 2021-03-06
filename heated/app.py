import sys
from typing import Type

from .command import Command
from .compiler import compile_command
from .context import Context
from .parser import Parser


class RemainingArguments(Exception):
    def __init__(self, remaining_args: list[str]):
        self.remaining_args = remaining_args
        super().__init__(f"Unconsumed parameters: {remaining_args}")


class App:
    def __init__(self, entry_command: Type = None, context: Context = None):
        self.entry_command = entry_command
        self.context = context or Context()

    def run(self):
        # Instantiate the entry command, passing the context
        # Compile the command
        # Return value will be remaining parsed arguments, next Command
        # Call the entry Command's invoke method
        # If there's a next Command, loop at Command instantiation

        context = self.context or Context()
        next_command = self.entry_command
        remaining_args = sys.argv[1:]

        while next_command is not None:
            command: Command = next_command(context=context)
            compiled_command = compile_command(command)
            next_command, remaining_args = Parser.parse_args(compiled_command, remaining_args)
            command.invoke()

        if remaining_args:
            raise RemainingArguments(remaining_args)

        sys.exit(context.exit_code)
