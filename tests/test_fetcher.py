import unittest

class TestFetcher(unittest.TestCase):
    def test_fetcher(self):
        from app.fetcher import fetch_jobs
        self.assertIsNotNone(fetch_jobs)

if __name__ == '__main__':
    unittest.main()

# This code is a simple unit test for the fetcher module.
# It checks if the fetcher function can be imported without errors.