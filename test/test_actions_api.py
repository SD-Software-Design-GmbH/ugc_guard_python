# coding: utf-8

"""
    UGC Guard API

    API for UGC Guard. A tool to help you manage reports on user generated content.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ugc_guard_python.api.actions_api import ActionsApi


class TestActionsApi(unittest.TestCase):
    """ActionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActionsApi()

    def tearDown(self) -> None:
        pass

    def test_create_action(self) -> None:
        """Test case for create_action

        Create Action
        """
        pass

    def test_delete_action(self) -> None:
        """Test case for delete_action

        Delete Action
        """
        pass

    def test_get_action_by_id(self) -> None:
        """Test case for get_action_by_id

        Get Action By Id
        """
        pass

    def test_get_all_actions_of_type(self) -> None:
        """Test case for get_all_actions_of_type

        Get All Actions Of Type
        """
        pass

    def test_get_user_type_action_by_id(self) -> None:
        """Test case for get_user_type_action_by_id

        Get User Type Action By Id
        """
        pass

    def test_perform_action(self) -> None:
        """Test case for perform_action

        Perform Action
        """
        pass

    def test_update_action(self) -> None:
        """Test case for update_action

        Update Action
        """
        pass


if __name__ == '__main__':
    unittest.main()
