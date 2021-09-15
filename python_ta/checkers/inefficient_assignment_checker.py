"""checker for type annotation.
"""

import astroid
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker


class InefficientAssignment(BaseChecker):
    __implements__ = IAstroidChecker

    name = "inefficient_assignment"
    msgs = {
        "W0001": (
            "Returns a non-unique constant.",
            "inefficient_assignment",
            "All constants returned in a function should be unique.",
        ),
    }

    priority = -1

    def __init__(self, linter):
        super().__init__(linter=linter)
        self._inefficient_assignment = []

    def visit_assign(self, node: nodes.Assign):
        if isinstance(node.value, nodes.BinOp):
            if (
                node.value.left.name == node.targets[0].as_string()
                or node.value.right.name == node.targets[0].as_string()
            ):
                self.add_message(
                    "inefficient_assignment",
                    node=node,
                )

    def register(linter):
        linter.register_checker(InefficientAssignment(linter))


if __name__ == "__main__":
    # node = astroid.extract_node("""
    # x = 5
    # y = y + 5
    # """)
    # print(node)
    # print(node.targets[0].as_string())
    # # print(node.targets[0].as_string())
    # print(node.value)
    # print(isinstance(node.value, nodes.BinOp))
    # print(node.value.left.name == node.targets[0].as_string())

    a, b = astroid.extract_node(
        """
        def test(x): #@
            x = x + 5 #@
        """
    )

    print(a)
    print(b)
