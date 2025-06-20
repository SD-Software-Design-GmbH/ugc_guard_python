# coding: utf-8

"""
    UGC Guard API

    API for UGC Guard. A tool to help you manage reports on user generated content.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ugc_guard_python.models.mail_template_base import MailTemplateBase

class TestMailTemplateBase(unittest.TestCase):
    """MailTemplateBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MailTemplateBase:
        """Test MailTemplateBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MailTemplateBase`
        """
        model = MailTemplateBase()
        if include_optional:
            return MailTemplateBase(
                subject = '',
                body = '',
                type = 'report_created_admin'
            )
        else:
            return MailTemplateBase(
                type = 'report_created_admin',
        )
        """

    def testMailTemplateBase(self):
        """Test MailTemplateBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
