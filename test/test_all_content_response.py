# coding: utf-8

"""
    UGC Guard API

    API for UGC Guard. A tool to help you manage reports on user generated content.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ugc_guard_python.models.all_content_response import AllContentResponse

class TestAllContentResponse(unittest.TestCase):
    """AllContentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllContentResponse:
        """Test AllContentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllContentResponse`
        """
        model = AllContentResponse()
        if include_optional:
            return AllContentResponse(
                main_content = ugc_guard_python.models.content_public.ContentPublic(
                    body_type = 'text', 
                    body = '', 
                    media_identifiers = [
                        ''
                        ], 
                    extra_data = {
                        'key' : null
                        }, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    unique_partner_id = '', 
                    ip = '', 
                    creator_id = '', 
                    id = '', 
                    creator = ugc_guard_python.models.person.Person(
                        id = '', 
                        module_id = '', 
                        unique_partner_id = '', 
                        name = '', 
                        email = '', 
                        phone = '', 
                        extra_data = {
                            'key' : null
                            }, ), ),
                context = [
                    ugc_guard_python.models.content_public.ContentPublic(
                        body_type = 'text', 
                        body = '', 
                        media_identifiers = [
                            ''
                            ], 
                        extra_data = {
                            'key' : null
                            }, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        unique_partner_id = '', 
                        ip = '', 
                        creator_id = '', 
                        id = '', 
                        creator = ugc_guard_python.models.person.Person(
                            id = '', 
                            module_id = '', 
                            unique_partner_id = '', 
                            name = '', 
                            email = '', 
                            phone = '', 
                            extra_data = {
                                'key' : null
                                }, ), )
                    ]
            )
        else:
            return AllContentResponse(
                context = [
                    ugc_guard_python.models.content_public.ContentPublic(
                        body_type = 'text', 
                        body = '', 
                        media_identifiers = [
                            ''
                            ], 
                        extra_data = {
                            'key' : null
                            }, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        unique_partner_id = '', 
                        ip = '', 
                        creator_id = '', 
                        id = '', 
                        creator = ugc_guard_python.models.person.Person(
                            id = '', 
                            module_id = '', 
                            unique_partner_id = '', 
                            name = '', 
                            email = '', 
                            phone = '', 
                            extra_data = {
                                'key' : null
                                }, ), )
                    ],
        )
        """

    def testAllContentResponse(self):
        """Test AllContentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
