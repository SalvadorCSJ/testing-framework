import tests
import Test_Framework as TF

def main():
    
    result = TF.TestResult()

    test = tests.TestCaseTest('test_result_success_run')
    test.run(result)

    test = tests.TestCaseTest('test_result_failure_run')
    test.run(result)

    test = tests.TestCaseTest('test_result_error_run')
    test.run(result)

    test = tests.TestCaseTest('test_result_multiple_run')
    test.run(result)

    test = tests.TestCaseTest('test_was_set_up')
    test.run(result)

    test = tests.TestCaseTest('test_was_run')
    test.run(result)

    test = tests.TestCaseTest('test_was_tear_down')
    test.run(result)

    test = tests.TestCaseTest('test_template_method')
    test.run(result)


    print(result.summary())

if __name__ == '__main__':
    main()
