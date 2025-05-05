import tests

def main():
    test = tests.MyTest('test_a')
    test.run()

    test = tests.MyTest('test_b')
    test.run()

    test = tests.MyTest('test_c')
    test.run()

if __name__ == '__main__':
    main()
