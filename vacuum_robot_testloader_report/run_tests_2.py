import unittest
import HtmlTestRunner

# Create a test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add test cases from the test files
suite.addTests(loader.discover('tests'))

# Run the tests and generate an HTML report
runner = HtmlTestRunner.HTMLTestRunner(output='test_reports', report_name='VacuumRobotTestReport')
runner.run(suite)
