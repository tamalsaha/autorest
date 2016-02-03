# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .operations.head_exception_operations import HeadExceptionOperations


class AutoRestHeadExceptionTestServiceConfiguration(AzureConfiguration):
    """Configuration for AutoRestHeadExceptionTestService

    :param credentials: Gets Azure subscription credentials.
    :type credentials: credentials
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str or None
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int or None
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool or None
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError('credentials must not be None.')
        if not base_url:
            base_url = 'http://localhost'

        super(AutoRestHeadExceptionTestServiceConfiguration, self).__init__(base_url, filepath)

        self.user_agent = 'auto_rest_head_exception_test_service/1.0.0'

        self.credentials = credentials
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class AutoRestHeadExceptionTestService(object):
    """Test Infrastructure for AutoRest

    :param config: Configuration for client.
    :type config: AutoRestHeadExceptionTestServiceConfiguration
    """

    def __init__(self, config):

        self._client = ServiceClient(config.credentials, config)

        client_models = {}
        self._serialize = Serializer()
        self._deserialize = Deserializer(client_models)

        self.config = config
        self.head_exception = HeadExceptionOperations(
            self._client, self.config, self._serialize, self._deserialize)