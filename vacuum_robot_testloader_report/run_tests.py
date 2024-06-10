import unittest
import os
import io
import sys

# Create a test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add test cases from the 'tests' directory
suite.addTests(loader.discover('tests'))

# Create a StringIO object to capture the output
output_buffer = io.StringIO()

# Run the tests and generate a report
runner = unittest.TextTestRunner(stream=output_buffer,verbosity=2)  #stream=f, or none
result = runner.run(suite)

# Get the output from the StringIO object
output = output_buffer.getvalue()

print(output)

# save the output to a file
if not os.path.exists(r'test_reports'):
    os.mkdir(r'test_reports')
with open("test_reports/test_report.txt", "w") as f:
    f.write(output)
