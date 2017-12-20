# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class Subscription(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, max_external_accounts=None, max_users=None, max_custom_signatures=None, max_custom_standards=None, organization=None, organization_id=None, plan=None, plan_id=None):
        """
        Subscription - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'max_external_accounts': 'int',
            'max_users': 'str',
            'max_custom_signatures': 'int',
            'max_custom_standards': 'int',
            'organization': 'Organization',
            'organization_id': 'int',
            'plan': 'Plan',
            'plan_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'max_external_accounts': 'max_external_accounts',
            'max_users': 'max_users',
            'max_custom_signatures': 'max_custom_signatures',
            'max_custom_standards': 'max_custom_standards',
            'organization': 'organization',
            'organization_id': 'organization_id',
            'plan': 'plan',
            'plan_id': 'plan_id'
        }

        self._id = id
        self._max_external_accounts = max_external_accounts
        self._max_users = max_users
        self._max_custom_signatures = max_custom_signatures
        self._max_custom_standards = max_custom_standards
        self._organization = organization
        self._organization_id = organization_id
        self._plan = plan
        self._plan_id = plan_id

    @property
    def id(self):
        """
        Gets the id of this Subscription.
        Unique ID

        :return: The id of this Subscription.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subscription.
        Unique ID

        :param id: The id of this Subscription.
        :type: int
        """

        self._id = id

    @property
    def max_external_accounts(self):
        """
        Gets the max_external_accounts of this Subscription.
        Number of External Accounts the customer is allowed under this subscription

        :return: The max_external_accounts of this Subscription.
        :rtype: int
        """
        return self._max_external_accounts

    @max_external_accounts.setter
    def max_external_accounts(self, max_external_accounts):
        """
        Sets the max_external_accounts of this Subscription.
        Number of External Accounts the customer is allowed under this subscription

        :param max_external_accounts: The max_external_accounts of this Subscription.
        :type: int
        """

        self._max_external_accounts = max_external_accounts

    @property
    def max_users(self):
        """
        Gets the max_users of this Subscription.
        Number of users the customer is allowed under this subscription

        :return: The max_users of this Subscription.
        :rtype: str
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """
        Sets the max_users of this Subscription.
        Number of users the customer is allowed under this subscription

        :param max_users: The max_users of this Subscription.
        :type: str
        """

        self._max_users = max_users

    @property
    def max_custom_signatures(self):
        """
        Gets the max_custom_signatures of this Subscription.
        Number of Custom Signatures the customer is allowed under this subscription

        :return: The max_custom_signatures of this Subscription.
        :rtype: int
        """
        return self._max_custom_signatures

    @max_custom_signatures.setter
    def max_custom_signatures(self, max_custom_signatures):
        """
        Sets the max_custom_signatures of this Subscription.
        Number of Custom Signatures the customer is allowed under this subscription

        :param max_custom_signatures: The max_custom_signatures of this Subscription.
        :type: int
        """

        self._max_custom_signatures = max_custom_signatures

    @property
    def max_custom_standards(self):
        """
        Gets the max_custom_standards of this Subscription.
        Number of Custom Compliance Standards the customer is allowed under this subscription

        :return: The max_custom_standards of this Subscription.
        :rtype: int
        """
        return self._max_custom_standards

    @max_custom_standards.setter
    def max_custom_standards(self, max_custom_standards):
        """
        Sets the max_custom_standards of this Subscription.
        Number of Custom Compliance Standards the customer is allowed under this subscription

        :param max_custom_standards: The max_custom_standards of this Subscription.
        :type: int
        """

        self._max_custom_standards = max_custom_standards

    @property
    def organization(self):
        """
        Gets the organization of this Subscription.
        Associated Organization

        :return: The organization of this Subscription.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this Subscription.
        Associated Organization

        :param organization: The organization of this Subscription.
        :type: Organization
        """

        self._organization = organization

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Subscription.
        Associated Organization ID

        :return: The organization_id of this Subscription.
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Subscription.
        Associated Organization ID

        :param organization_id: The organization_id of this Subscription.
        :type: int
        """

        self._organization_id = organization_id

    @property
    def plan(self):
        """
        Gets the plan of this Subscription.
        Associated Plan

        :return: The plan of this Subscription.
        :rtype: Plan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """
        Sets the plan of this Subscription.
        Associated Plan

        :param plan: The plan of this Subscription.
        :type: Plan
        """

        self._plan = plan

    @property
    def plan_id(self):
        """
        Gets the plan_id of this Subscription.
        Associated Plan ID

        :return: The plan_id of this Subscription.
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this Subscription.
        Associated Plan ID

        :param plan_id: The plan_id of this Subscription.
        :type: int
        """

        self._plan_id = plan_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
