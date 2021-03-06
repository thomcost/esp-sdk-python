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


class Alert(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, status=None, risk_level=None, resource=None, ended_reason=None, replaced_by_id=None, replaced_by_status=None, updated_at=None, started_at=None, ended_at=None, external_account=None, external_account_id=None, region=None, region_id=None, signature=None, signature_id=None, custom_signature=None, custom_signature_id=None, suppression=None, suppression_id=None, metadata=None, attribution=None, tags=None, compliance_controls=None, custom_compliance_controls=None):
        """
        Alert - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'created_at': 'datetime',
            'status': 'str',
            'risk_level': 'str',
            'resource': 'str',
            'ended_reason': 'str',
            'replaced_by_id': 'int',
            'replaced_by_status': 'str',
            'updated_at': 'datetime',
            'started_at': 'datetime',
            'ended_at': 'datetime',
            'external_account': 'ExternalAccount',
            'external_account_id': 'int',
            'region': 'Region',
            'region_id': 'int',
            'signature': 'Signature',
            'signature_id': 'int',
            'custom_signature': 'CustomSignature',
            'custom_signature_id': 'int',
            'suppression': 'Suppression',
            'suppression_id': 'int',
            'metadata': 'Metadata',
            'attribution': 'Attribution',
            'tags': 'list[Tag]',
            'compliance_controls': 'list[ComplianceControl]',
            'custom_compliance_controls': 'list[CustomComplianceControl]'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'status': 'status',
            'risk_level': 'risk_level',
            'resource': 'resource',
            'ended_reason': 'ended_reason',
            'replaced_by_id': 'replaced_by_id',
            'replaced_by_status': 'replaced_by_status',
            'updated_at': 'updated_at',
            'started_at': 'started_at',
            'ended_at': 'ended_at',
            'external_account': 'external_account',
            'external_account_id': 'external_account_id',
            'region': 'region',
            'region_id': 'region_id',
            'signature': 'signature',
            'signature_id': 'signature_id',
            'custom_signature': 'custom_signature',
            'custom_signature_id': 'custom_signature_id',
            'suppression': 'suppression',
            'suppression_id': 'suppression_id',
            'metadata': 'metadata',
            'attribution': 'attribution',
            'tags': 'tags',
            'compliance_controls': 'compliance_controls',
            'custom_compliance_controls': 'custom_compliance_controls'
        }

        self._id = id
        self._created_at = created_at
        self._status = status
        self._risk_level = risk_level
        self._resource = resource
        self._ended_reason = ended_reason
        self._replaced_by_id = replaced_by_id
        self._replaced_by_status = replaced_by_status
        self._updated_at = updated_at
        self._started_at = started_at
        self._ended_at = ended_at
        self._external_account = external_account
        self._external_account_id = external_account_id
        self._region = region
        self._region_id = region_id
        self._signature = signature
        self._signature_id = signature_id
        self._custom_signature = custom_signature
        self._custom_signature_id = custom_signature_id
        self._suppression = suppression
        self._suppression_id = suppression_id
        self._metadata = metadata
        self._attribution = attribution
        self._tags = tags
        self._compliance_controls = compliance_controls
        self._custom_compliance_controls = custom_compliance_controls

    @property
    def id(self):
        """
        Gets the id of this Alert.
        Unique ID

        :return: The id of this Alert.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Alert.
        Unique ID

        :param id: The id of this Alert.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Alert.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Alert.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Alert.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Alert.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def status(self):
        """
        Gets the status of this Alert.
        Status of the alert. Valid values are fail, warn, error, pass, info

        :return: The status of this Alert.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Alert.
        Status of the alert. Valid values are fail, warn, error, pass, info

        :param status: The status of this Alert.
        :type: str
        """

        self._status = status

    @property
    def risk_level(self):
        """
        Gets the risk_level of this Alert.
        The risk-level of the problem identified by the signature or custom signature. Valid values are low, medium, high

        :return: The risk_level of this Alert.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this Alert.
        The risk-level of the problem identified by the signature or custom signature. Valid values are low, medium, high

        :param risk_level: The risk_level of this Alert.
        :type: str
        """

        self._risk_level = risk_level

    @property
    def resource(self):
        """
        Gets the resource of this Alert.
        Resource identifier in Amazon

        :return: The resource of this Alert.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this Alert.
        Resource identifier in Amazon

        :param resource: The resource of this Alert.
        :type: str
        """

        self._resource = resource

    @property
    def ended_reason(self):
        """
        Gets the ended_reason of this Alert.
        The reason this alert ended. Valid values are from_api, new_alert, from_scan, not_present_after_scan, signature_deleted, custom_signature_deleted, suppression_created, suppression_deactivated, custom_risk_level_created, custom_risk_level_deleted

        :return: The ended_reason of this Alert.
        :rtype: str
        """
        return self._ended_reason

    @ended_reason.setter
    def ended_reason(self, ended_reason):
        """
        Sets the ended_reason of this Alert.
        The reason this alert ended. Valid values are from_api, new_alert, from_scan, not_present_after_scan, signature_deleted, custom_signature_deleted, suppression_created, suppression_deactivated, custom_risk_level_created, custom_risk_level_deleted

        :param ended_reason: The ended_reason of this Alert.
        :type: str
        """

        self._ended_reason = ended_reason

    @property
    def replaced_by_id(self):
        """
        Gets the replaced_by_id of this Alert.
        The ID of the alert that replaced this alert

        :return: The replaced_by_id of this Alert.
        :rtype: int
        """
        return self._replaced_by_id

    @replaced_by_id.setter
    def replaced_by_id(self, replaced_by_id):
        """
        Sets the replaced_by_id of this Alert.
        The ID of the alert that replaced this alert

        :param replaced_by_id: The replaced_by_id of this Alert.
        :type: int
        """

        self._replaced_by_id = replaced_by_id

    @property
    def replaced_by_status(self):
        """
        Gets the replaced_by_status of this Alert.
        The status of the alert that replaced this alert

        :return: The replaced_by_status of this Alert.
        :rtype: str
        """
        return self._replaced_by_status

    @replaced_by_status.setter
    def replaced_by_status(self, replaced_by_status):
        """
        Sets the replaced_by_status of this Alert.
        The status of the alert that replaced this alert

        :param replaced_by_status: The replaced_by_status of this Alert.
        :type: str
        """

        self._replaced_by_status = replaced_by_status

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Alert.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this Alert.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Alert.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this Alert.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def started_at(self):
        """
        Gets the started_at of this Alert.
        ISO 8601 timestamp when the alert started being active

        :return: The started_at of this Alert.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this Alert.
        ISO 8601 timestamp when the alert started being active

        :param started_at: The started_at of this Alert.
        :type: datetime
        """

        self._started_at = started_at

    @property
    def ended_at(self):
        """
        Gets the ended_at of this Alert.
        ISO 8601 timestamp when the alert stopped being active

        :return: The ended_at of this Alert.
        :rtype: datetime
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """
        Sets the ended_at of this Alert.
        ISO 8601 timestamp when the alert stopped being active

        :param ended_at: The ended_at of this Alert.
        :type: datetime
        """

        self._ended_at = ended_at

    @property
    def external_account(self):
        """
        Gets the external_account of this Alert.
        Associated External Account

        :return: The external_account of this Alert.
        :rtype: ExternalAccount
        """
        return self._external_account

    @external_account.setter
    def external_account(self, external_account):
        """
        Sets the external_account of this Alert.
        Associated External Account

        :param external_account: The external_account of this Alert.
        :type: ExternalAccount
        """

        self._external_account = external_account

    @property
    def external_account_id(self):
        """
        Gets the external_account_id of this Alert.
        Associated External Account ID

        :return: The external_account_id of this Alert.
        :rtype: int
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """
        Sets the external_account_id of this Alert.
        Associated External Account ID

        :param external_account_id: The external_account_id of this Alert.
        :type: int
        """

        self._external_account_id = external_account_id

    @property
    def region(self):
        """
        Gets the region of this Alert.
        Associated Region

        :return: The region of this Alert.
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Alert.
        Associated Region

        :param region: The region of this Alert.
        :type: Region
        """

        self._region = region

    @property
    def region_id(self):
        """
        Gets the region_id of this Alert.
        Associated Region ID

        :return: The region_id of this Alert.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this Alert.
        Associated Region ID

        :param region_id: The region_id of this Alert.
        :type: int
        """

        self._region_id = region_id

    @property
    def signature(self):
        """
        Gets the signature of this Alert.
        Associated Signature

        :return: The signature of this Alert.
        :rtype: Signature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this Alert.
        Associated Signature

        :param signature: The signature of this Alert.
        :type: Signature
        """

        self._signature = signature

    @property
    def signature_id(self):
        """
        Gets the signature_id of this Alert.
        Associated Signature ID

        :return: The signature_id of this Alert.
        :rtype: int
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """
        Sets the signature_id of this Alert.
        Associated Signature ID

        :param signature_id: The signature_id of this Alert.
        :type: int
        """

        self._signature_id = signature_id

    @property
    def custom_signature(self):
        """
        Gets the custom_signature of this Alert.
        Associated Custom Signature

        :return: The custom_signature of this Alert.
        :rtype: CustomSignature
        """
        return self._custom_signature

    @custom_signature.setter
    def custom_signature(self, custom_signature):
        """
        Sets the custom_signature of this Alert.
        Associated Custom Signature

        :param custom_signature: The custom_signature of this Alert.
        :type: CustomSignature
        """

        self._custom_signature = custom_signature

    @property
    def custom_signature_id(self):
        """
        Gets the custom_signature_id of this Alert.
        Associated Custom Signature ID

        :return: The custom_signature_id of this Alert.
        :rtype: int
        """
        return self._custom_signature_id

    @custom_signature_id.setter
    def custom_signature_id(self, custom_signature_id):
        """
        Sets the custom_signature_id of this Alert.
        Associated Custom Signature ID

        :param custom_signature_id: The custom_signature_id of this Alert.
        :type: int
        """

        self._custom_signature_id = custom_signature_id

    @property
    def suppression(self):
        """
        Gets the suppression of this Alert.
        Associated Suppression

        :return: The suppression of this Alert.
        :rtype: Suppression
        """
        return self._suppression

    @suppression.setter
    def suppression(self, suppression):
        """
        Sets the suppression of this Alert.
        Associated Suppression

        :param suppression: The suppression of this Alert.
        :type: Suppression
        """

        self._suppression = suppression

    @property
    def suppression_id(self):
        """
        Gets the suppression_id of this Alert.
        Associated Suppression ID

        :return: The suppression_id of this Alert.
        :rtype: int
        """
        return self._suppression_id

    @suppression_id.setter
    def suppression_id(self, suppression_id):
        """
        Sets the suppression_id of this Alert.
        Associated Suppression ID

        :param suppression_id: The suppression_id of this Alert.
        :type: int
        """

        self._suppression_id = suppression_id

    @property
    def metadata(self):
        """
        Gets the metadata of this Alert.
        Associated Metadata

        :return: The metadata of this Alert.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Alert.
        Associated Metadata

        :param metadata: The metadata of this Alert.
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def attribution(self):
        """
        Gets the attribution of this Alert.
        Associated Attribution

        :return: The attribution of this Alert.
        :rtype: Attribution
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """
        Sets the attribution of this Alert.
        Associated Attribution

        :param attribution: The attribution of this Alert.
        :type: Attribution
        """

        self._attribution = attribution

    @property
    def tags(self):
        """
        Gets the tags of this Alert.
        Associated Tags

        :return: The tags of this Alert.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Alert.
        Associated Tags

        :param tags: The tags of this Alert.
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def compliance_controls(self):
        """
        Gets the compliance_controls of this Alert.
        Associated Compliance Controls

        :return: The compliance_controls of this Alert.
        :rtype: list[ComplianceControl]
        """
        return self._compliance_controls

    @compliance_controls.setter
    def compliance_controls(self, compliance_controls):
        """
        Sets the compliance_controls of this Alert.
        Associated Compliance Controls

        :param compliance_controls: The compliance_controls of this Alert.
        :type: list[ComplianceControl]
        """

        self._compliance_controls = compliance_controls

    @property
    def custom_compliance_controls(self):
        """
        Gets the custom_compliance_controls of this Alert.
        Associated Custom Compliance Controls

        :return: The custom_compliance_controls of this Alert.
        :rtype: list[CustomComplianceControl]
        """
        return self._custom_compliance_controls

    @custom_compliance_controls.setter
    def custom_compliance_controls(self, custom_compliance_controls):
        """
        Sets the custom_compliance_controls of this Alert.
        Associated Custom Compliance Controls

        :param custom_compliance_controls: The custom_compliance_controls of this Alert.
        :type: list[CustomComplianceControl]
        """

        self._custom_compliance_controls = custom_compliance_controls

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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
