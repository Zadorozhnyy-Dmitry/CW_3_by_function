from pathlib import Path

ROOT_PATH = Path(__file__).parent
OPERATIONS_DATA_PATH = ROOT_PATH.joinpath('data', 'operations.json')
TEST_OPERATIONS_PART = ROOT_PATH.joinpath('tests', 'test_data', 'test_operations.json')
NUMBER_OPERATIONS = 5
