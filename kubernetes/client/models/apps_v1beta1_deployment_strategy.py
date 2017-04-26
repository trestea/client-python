# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppsV1beta1DeploymentStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rolling_update=None, type=None):
        """
        AppsV1beta1DeploymentStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rolling_update': 'AppsV1beta1RollingUpdateDeployment',
            'type': 'str'
        }

        self.attribute_map = {
            'rolling_update': 'rollingUpdate',
            'type': 'type'
        }

        self._rolling_update = rolling_update
        self._type = type

    @property
    def rolling_update(self):
        """
        Gets the rolling_update of this AppsV1beta1DeploymentStrategy.
        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

        :return: The rolling_update of this AppsV1beta1DeploymentStrategy.
        :rtype: AppsV1beta1RollingUpdateDeployment
        """
        return self._rolling_update

    @rolling_update.setter
    def rolling_update(self, rolling_update):
        """
        Sets the rolling_update of this AppsV1beta1DeploymentStrategy.
        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

        :param rolling_update: The rolling_update of this AppsV1beta1DeploymentStrategy.
        :type: AppsV1beta1RollingUpdateDeployment
        """

        self._rolling_update = rolling_update

    @property
    def type(self):
        """
        Gets the type of this AppsV1beta1DeploymentStrategy.
        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.

        :return: The type of this AppsV1beta1DeploymentStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AppsV1beta1DeploymentStrategy.
        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.

        :param type: The type of this AppsV1beta1DeploymentStrategy.
        :type: str
        """

        self._type = type

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other