"""checker for inefficient assignment.
"""

from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class InefficientAssignment(BaseChecker):
    __implements__ = IAstroidChecker

    name = "inefficient_assignment"
    msgs = {
        "CUSTOM": (
            "Inefficient assignment has been made.",
            "inefficient_assignment",
            "Binary operation with a constant and an existing varialbe should be efficient.",
        ),
    }

    priority = -1

    def __init__(self, linter):
        super().__init__(linter=linter)

    def visit_assign(self, node: nodes.Assign):
        if isinstance(node.value, nodes.BinOp):
            if node.value.left.name == node.targets[0].as_string() and isinstance(
                node.value.right, nodes.Const
            ):
                self.add_message(
                    "inefficient_assignment",
                    node=node,
                )

    def register(linter):
        linter.register_checker(InefficientAssignment(linter))
