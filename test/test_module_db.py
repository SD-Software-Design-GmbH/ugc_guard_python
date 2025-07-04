# coding: utf-8

"""
    UGC Guard API

    API for UGC Guard. A tool to help you manage reports on user generated content.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ugc_guard_python.models.module_db import ModuleDB

class TestModuleDB(unittest.TestCase):
    """ModuleDB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleDB:
        """Test ModuleDB
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleDB`
        """
        model = ModuleDB()
        if include_optional:
            return ModuleDB(
                send_mail_on_report = True,
                send_mail_on_report_to_user = True,
                send_mail_on_resolved_report_to_user = True,
                id = '',
                logo_url = '',
                name = '',
                description = '',
                organization_id = '',
                auto_ai_validation = True,
                secret = ''
            )
        else:
            return ModuleDB(
                name = '',
                organization_id = '',
        )
        """

    def testModuleDB(self):
        """Test ModuleDB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
