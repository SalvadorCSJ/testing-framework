import tests
import Test_Framework as TF

def main():
    
    result = TF.TestResult()

    test = tests.MyTest('test_a')
    test.run(result)

    test = tests.MyTest('test_b')
    test.run(result)

    test = tests.MyTest('test_c')
    test.run(result)

    print(result.summary())

if __name__ == '__main__':
    main()
