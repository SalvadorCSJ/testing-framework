import tests
import Test_Framework as TF

def main():
    
    loader = TF.TestLoader()
    suite = loader.make_suite(tests.TestLoaderTest)

    runner = TF.TestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
