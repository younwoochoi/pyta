import astroid
import pylint.testutils

from python_ta.checkers.inefficient_assignment_checker import InefficientAssignment


class TestUniqueReturnChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = InefficientAssignment

    def setUp(self):
        self.setup_method()

    def test_inefficient_assignment(self):
        assign_node_a = astroid.extract_node(
            """
        def test(x):
            x = x + 5 #@
        """
        )
        with self.assertAddsMessages(
            pylint.testutils.Message(msg_id="inefficient_assignment", node=assign_node_a)
        ):
            self.checker.visit_assign(assign_node_a)

    def test_efficient_assignment(self):
        assign_node_a = astroid.extract_node(
            """
        def test(x):
            x += 5 #@
        """
        )
        with self.assertNoMessages():
            self.checker.visit_assign(assign_node_a)


if __name__ == "__main__":
    import pytest

    pytest.main(["tests/test_custom_checkers/test_inefficient_assignment_checker.py"])
