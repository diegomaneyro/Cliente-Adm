import unittest

if __name__ == '__main__':
    # Descubre y ejecuta todos los tests en el directorio 'tests'
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.TextTestRunner()
    testRunner.run(tests)
