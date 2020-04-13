from os.path import join, dirname
from jsonschema import validate
import jsonref


def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = _load_json_schema(schema_file)
    print(schema)
    return validate(data, schema)


def _load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join('resources', filename)
    absolute_path = join(dirname(__file__), relative_path)
    
    base_path = dirname(absolute_path)
    base_uri = 'file://{}/'.format(base_path)

    with open(absolute_path) as schema_file:
    	return jsonref.loads(schema_file.read(), base_uri=base_uri, jsonschema=True)

assert_valid_schema("wud_1.json", "schema.json")