import astroid
import pylint.testutils
from astroid import nodes

from python_ta.checkers.inefficient_assignment_checker import InefficientAssignment


class TestUniqueReturnChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = InefficientAssignment

    def setUp(self):
        self.setup_method()

    def test_ignores_unique_ints(self):
        return_node_a = astroid.extract_node(
            """
        def test(x):
            x = x + 5 #@
        """
        )
        with self.assertAddsMessages(
            pylint.testutils.Message(msg_id="inefficient_assignment", node=return_node_a)
        ):
            self.checker.visit_assign(return_node_a)


if __name__ == "__main__":
    a = TestUniqueReturnChecker()
    a.setUp()
    a.test_ignores_unique_ints()
