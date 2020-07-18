from pathlib import Path

import yaml

from app.app import app


def test_spec():
    client = app.test_client()

    oas_file = Path(__file__).parent.parent / 'oas.yaml'

    specification = yaml.safe_load(oas_file.read_text())

    implementation = client.get('/swagger.json').get_json()

    o1 = specification['components']['schemas']['Order']

    o2 = implementation['definitions']['Order']

    import pdb; pdb.set_trace()

    assert specification['components']['schemas']['Order'] == implementation['definitions']['Order']
