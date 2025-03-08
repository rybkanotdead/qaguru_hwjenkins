import os
import tests_test.tests


def file_path(file_name):
    return os.path.abspath(
        os.path.join(
            os.path.dirname(tests_test.tests.__file__), f'../tests_test/image/{file_name}'
        )
    )