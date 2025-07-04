# coding: utf-8

"""
    UGC Guard API

    API for UGC Guard. A tool to help you manage reports on user generated content.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ugc_guard_python.models.organization_groupings import OrganizationGroupings

class TestOrganizationGroupings(unittest.TestCase):
    """OrganizationGroupings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationGroupings:
        """Test OrganizationGroupings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationGroupings`
        """
        model = OrganizationGroupings()
        if include_optional:
            return OrganizationGroupings(
                invites = [
                    ugc_guard_python.models.org_with_membership_state.OrgWithMembershipState(
                        id = '', 
                        name = '', 
                        description = '', 
                        logo_url = '', 
                        enabled_ai_list = [
                            ''
                            ], 
                        enabled_ai = True, 
                        support_email = '', 
                        membership_state = 'invited', )
                    ],
                reviewers = [
                    ugc_guard_python.models.org_with_membership_state.OrgWithMembershipState(
                        id = '', 
                        name = '', 
                        description = '', 
                        logo_url = '', 
                        enabled_ai_list = [
                            ''
                            ], 
                        enabled_ai = True, 
                        support_email = '', 
                        membership_state = 'invited', )
                    ],
                members = [
                    ugc_guard_python.models.org_with_membership_state.OrgWithMembershipState(
                        id = '', 
                        name = '', 
                        description = '', 
                        logo_url = '', 
                        enabled_ai_list = [
                            ''
                            ], 
                        enabled_ai = True, 
                        support_email = '', 
                        membership_state = 'invited', )
                    ],
                admins = [
                    ugc_guard_python.models.org_with_membership_state.OrgWithMembershipState(
                        id = '', 
                        name = '', 
                        description = '', 
                        logo_url = '', 
                        enabled_ai_list = [
                            ''
                            ], 
                        enabled_ai = True, 
                        support_email = '', 
                        membership_state = 'invited', )
                    ]
            )
        else:
            return OrganizationGroupings(
        )
        """

    def testOrganizationGroupings(self):
        """Test OrganizationGroupings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
