import ast
import astunparse

# Original code with white spaces and excess empty lines
code_with_spaces_and_empty_lines = """#!/usr/bin/python3

# 6-max_integer_test.py

"""Unittests for max_integer([..])."""


import unittest

max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):

    """Define unittests for max_integer([..])."""


    def test_ordered_list(self):

        """Test an ordered list of integers."""

        ordered = [1, 2, 3, 4]

        self.assertEqual(max_integer(ordered), 4)


    def test_unordered_list(self):

        """Test an unordered list of integers."""

        unordered = [1, 2, 4, 3]

        self.assertEqual(max_integer(unordered), 4)


    def test_max_at_begginning(self):

        """Test a list with a beginning max value."""

        max_at_beginning = [4, 3, 2, 1]

        self.assertEqual(max_integer(max_at_beginning), 4)


    def test_empty_list(self):

        """Test an empty list."""

        empty = []

        self.assertEqual(max_integer(empty), None)


    def test_one_element_list(self):

        """Test a list with a single element."""

        one_element = [7]

        self.assertEqual(max_integer(one_element), 7)


    def test_floats(self):

        """Test a list of floats."""

        floats = [1.53, 6.33, -9.123, 15.2, 6.0]

        self.assertEqual(max_integer(floats), 15.2)


    def test_ints_and_floats(self):

        """Test a list of ints and floats."""

        ints_and_floats = [1.53, 15.5, -9, 15, 6]

        self.assertEqual(max_integer(ints_and_floats), 15.5)


    def test_string(self):

        """Test a string."""

        string = "Brennan"

        self.assertEqual(max_integer(string), 'r')


    def test_list_of_strings(self):

        """Test a list of strings."""

        strings = ["Brennan", "is", "my", "name"]

        self.assertEqual(max_integer(strings), "name")


    def test_empty_string(self):

        """Test an empty string."""

        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':

    unittest.main()
"""

# Parse the code into an Abstract Syntax Tree (AST)
parsed_code = ast.parse(code_with_spaces_and_empty_lines)


# Define a visitor class to remove white spaces and excess empty lines
class CodeCleaner(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        # Remove white spaces and excess empty lines within functions
        if node.body:
            new_body = []
            for stmt in node.body:
                if not isinstance(stmt, (ast.FunctionDef, ast.ClassDef)):
                    # Preserve non-function and non-class statements
                    if isinstance(stmt, ast.Expr):
                        # Remove multiple empty lines within expressions
                        new_body.append(ast.Expr(ast.Str("")))
                    else:
                        new_body.append(stmt)
            node.body = new_body
        return node

    def visit(self, node):
        if not isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            # Remove spaces from other parts of the code
            ast.fix_missing_locations(node)
            return node
        return self.generic_visit(node)


# Apply the visitor to remove white spaces and excess empty lines
cleaned_code = CodeCleaner().visit(parsed_code)

# Convert the modified AST back to code
code_without_spaces_and_empty_lines = astunparse.unparse(cleaned_code)

# Print the code without white spaces and excess empty lines
print(code_without_spaces_and_empty_lines)
