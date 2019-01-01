import sys
import unittest


class GeneralTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skip("test not run")
    def test_not_run(self):
        pass

    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")
    def test_linux_support(self):
        # linux specific testing code
        pass

    @unittest.skipUnless(sys.platform.startswith("macOS"), "requires macOS")
    def test_macOS_support(self):
        # macOS specific testing code
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")