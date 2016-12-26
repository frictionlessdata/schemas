import io
import os
import json
import unittest
import urllib.request

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..'
    )
)
REGISTRY_PATH = os.path.join(BASE_PATH, 'registry.json')


class TestRegistryJson(unittest.TestCase):
    def test_registry_has_the_expected_headers(self):
        expected_headers = (
            'title',
            'schema',
            'schema_path',
            'specification',
        )
        registry = json.load(io.open(REGISTRY_PATH, encoding='utf-8'))
        for id, item in registry.items():
            self.assertEqual(sorted(item.keys()), sorted(expected_headers))

    def test_registry_schemas_have_the_required_attributes(self):
        required_attributes = (
            'title',
            'schema',
            'schema_path',
            'specification',
        )
        registry = json.load(io.open(REGISTRY_PATH, encoding='utf-8'))
        for id, item in registry.items():
            for attr in required_attributes:
                self.assertTrue(attr in item)

    def test_registry_schemas_have_unique_ids(self):
        ids = []
        registry = json.load(io.open(REGISTRY_PATH, encoding='utf-8'))
        for id, item in registry.items():
            self.assertNotIn(id, ids)
            ids.append(id)

    def test_schema_paths_exist_and_are_files(self):
        registry = json.load(io.open(REGISTRY_PATH, encoding='utf-8'))
        for id, item in registry.items():
            schema_path = item['schema_path']
            msg = "schema_path '{0}' of schema '{1}' isn't a file"
            msg = msg.format(schema_path, id)
            path = os.path.join(BASE_PATH, schema_path)
            assert os.path.isfile(path), msg

    def test_schema_urls_exist(self):
        is_successful = lambda req: req.status >= 200 and req.status < 400
        is_redirect = lambda req: req.status >= 300 and req.status < 400
        registry = json.load(io.open(REGISTRY_PATH, encoding='utf-8'))
        for id, item in registry.items():
            url = item['schema']
            res = self._make_head_request(url)
            msg = "Error fetching schema_url '{0}' of schema '{1}'"
            msg = msg.format(url, id)
            assert (is_successful(res) or is_redirect(res)), msg

    def test_specification_urls_exist(self):
        is_successful = lambda req: req.status >= 200 and req.status < 400
        is_redirect = lambda req: req.status >= 300 and req.status < 400
        registry = json.load(io.open(REGISTRY_PATH, encoding='utf-8'))
        for id, item in registry.items():
            url = item['schema']
            res = self._make_head_request(url)
            msg = "Error fetching specification '{0}' of schema '{1}'"
            msg = msg.format(url, id)
            assert (is_successful(res) or is_redirect(res)), msg

    def test_main_schemas_present(self):
        registry = json.load(io.open(REGISTRY_PATH, encoding='utf-8'))
        ids = list(registry.keys())
        self.assertIn('datapackage', ids)
        self.assertIn('tabular-datapackage', ids)
        self.assertIn('fiscal-datapackage', ids)

    def _make_head_request(self, url):
        req = urllib.request.Request(url, method='HEAD')
        return urllib.request.urlopen(req)
