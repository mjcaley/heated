from heated.parameters import Flag, Parameters, Argument, Option
from heated.command import Command
from heated.app import App


class BranchParams(Parameters):
    branch = Argument("BRANCH_NAME")
    list: bool = Flag("--list", "-l")


class Branch(Command):
    params: BranchParams

    def invoke(self):
        if self.params.list:
            print("git branch list")
        else:
            print("git branch default option")


class CheckoutParams(Parameters):
    branch = Argument("BRANCH")
    new_branch: bool = Flag("-b")


class Checkout(Command):
    params: CheckoutParams

    def invoke(self):
        if self.params.new_branch:
            print(f"Creating new branch {self.params.branch}")
        else:
            print(f"Checking out existing branch {self.params.branch}")


class CommitParams(Parameters):
    message: str = Option("-m")
    amend: bool = Flag("--amend")
    squash: bool = Flag("--squash")


class Commit(Command):
    params: CommitParams

    def invoke(self):
        if self.params.squash:
            print(f"commit squash with message: {self.params.message}")
        elif self.params.amend:
            print(f"commit amend with message: {self.params.message}")
        else:
            print(f"commit with message {self.params.message}")


class Main(Command):
    commit: Commit
    branch: Branch
    checkout: Checkout


app = App(Main)
app.run()
