from unittest import TestCase, main

import dill

class DillTest(TestCase):

    def test_lambda(self):
        f = lambda filename: open(filename, 'r').close()
        print dill.dumps(f)
        f_dill = dill.loads(dill.dumps(f))
        f_dill("test.txt")

    def test_lambda_cp(self):
        import cloud.serialization.cloudpickle as cp
        f = lambda filename: open(filename, 'r').close()
        f_dill = cp.loads(cp.dumps(f))
        f_dill("test.txt")

if __name__ == '__main__':
    main()
