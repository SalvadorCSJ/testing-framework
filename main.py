import tests
import Test_Framework as TF

def main():
    
    loader = TF.TestLoader()
    test_case_suite = loader.make_suite(tests.TestCaseTest)
    test_suite_suite = loader.make_suite(tests.TestSuiteTest)
    test_load_suite = loader.make_suite(tests.TestLoaderTest)

    suite = TF.TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TF.TestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
