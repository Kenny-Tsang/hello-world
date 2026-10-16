"""Verify the greeting program prints Hello, world!."""

import io
import unittest
from contextlib import redirect_stdout

import hello


class HelloWorldTest(unittest.TestCase):
    def test_greet_returns_hello_world(self) -> None:
        self.assertEqual(hello.greet(), "Hello, world!")

    def test_main_prints_hello_world(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            hello.main()
        output = buffer.getvalue()
        self.assertEqual(output, "Hello, world!\n")
        print(output, end="")


if __name__ == "__main__":
    unittest.main(verbosity=2)
