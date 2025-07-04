# coding: utf-8

"""
    UGC Guard API

    API for UGC Guard. A tool to help you manage reports on user generated content.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ugc_guard_python.models.module_stats import ModuleStats

class TestModuleStats(unittest.TestCase):
    """ModuleStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleStats:
        """Test ModuleStats
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleStats`
        """
        model = ModuleStats()
        if include_optional:
            return ModuleStats(
                module_id = '',
                total_reports = 56,
                total_files = 56,
                total_reporters = 56,
                total_actions = 56,
                total_types = 56,
                total_open_reports = 56
            )
        else:
            return ModuleStats(
                module_id = '',
        )
        """

    def testModuleStats(self):
        """Test ModuleStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
