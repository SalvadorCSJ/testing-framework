import tests
import Test_Framework as TF

def main():
    
    result = TF.TestResult()
    suite = TF.TestSuite()

    suite.add_test(tests.TestCaseTest('test_result_success_run'))
    suite.add_test(tests.TestCaseTest('test_result_failure_run'))
    suite.add_test(tests.TestCaseTest('test_result_error_run'))
    suite.add_test(tests.TestCaseTest('test_result_multiple_run'))
    suite.add_test(tests.TestCaseTest('test_was_set_up'))
    suite.add_test(tests.TestCaseTest('test_was_run'))
    suite.add_test(tests.TestCaseTest('test_was_tear_down'))
    suite.add_test(tests.TestCaseTest('test_template_method'))

    suite.add_test(tests.TestSuiteTest('test_suite_size'))
    suite.add_test(tests.TestSuiteTest('test_suite_success_run'))
    suite.add_test(tests.TestSuiteTest('test_suite_multiple_run'))

    suite.run(result)
    print(result.summary())

if __name__ == '__main__':
    main()
