# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CustomSignaturesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, external_account_ids, identifier, name, provider, risk_level, **kwargs):
        """
        Create a(n) Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(external_account_ids, identifier, name, provider, risk_level, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] external_account_ids: The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. (required)
        :param str identifier: The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 (required)
        :param str name: The name of the custom signature (required)
        :param str provider: The cloud provider this account is for (required)
        :param str risk_level: The risk-level of the problem identified by the custom signature. Valid values are low, medium, high (required)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :param str description: The description of the custom signature that is displayed on alerts
        :param bool include_new_accounts: When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user.
        :param str resolution: Details for how to resolve this custom signature that is displayed on alerts
        :param int service_id: The service this custom signature is for. If no service is selected it will default to Custom.
        :return: CustomSignature
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(external_account_ids, identifier, name, provider, risk_level, **kwargs)
        else:
            (data) = self.create_with_http_info(external_account_ids, identifier, name, provider, risk_level, **kwargs)
            return data

    def create_with_http_info(self, external_account_ids, identifier, name, provider, risk_level, **kwargs):
        """
        Create a(n) Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(external_account_ids, identifier, name, provider, risk_level, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] external_account_ids: The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run. (required)
        :param str identifier: The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001 (required)
        :param str name: The name of the custom signature (required)
        :param str provider: The cloud provider this account is for (required)
        :param str risk_level: The risk-level of the problem identified by the custom signature. Valid values are low, medium, high (required)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :param str description: The description of the custom signature that is displayed on alerts
        :param bool include_new_accounts: When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user.
        :param str resolution: Details for how to resolve this custom signature that is displayed on alerts
        :param int service_id: The service this custom signature is for. If no service is selected it will default to Custom.
        :return: CustomSignature
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_account_ids', 'identifier', 'name', 'provider', 'risk_level', 'include', 'description', 'include_new_accounts', 'resolution', 'service_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'external_account_ids' is set
        if ('external_account_ids' not in params) or (params['external_account_ids'] is None):
            raise ValueError("Missing the required parameter `external_account_ids` when calling `create`")
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params) or (params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `create`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create`")
        # verify the required parameter 'provider' is set
        if ('provider' not in params) or (params['provider'] is None):
            raise ValueError("Missing the required parameter `provider` when calling `create`")
        # verify the required parameter 'risk_level' is set
        if ('risk_level' not in params) or (params['risk_level'] is None):
            raise ValueError("Missing the required parameter `risk_level` when calling `create`")


        collection_formats = {}

        resource_path = '/api/v2/custom_signatures.json_api'.replace('{format}', 'json_api')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'external_account_ids' in params:
            form_params.append(('external_account_ids', params['external_account_ids']))
            collection_formats['None'] = 'csv'
        if 'identifier' in params:
            form_params.append(('identifier', params['identifier']))
        if 'include_new_accounts' in params:
            form_params.append(('include_new_accounts', params['include_new_accounts']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'provider' in params:
            form_params.append(('provider', params['provider']))
        if 'resolution' in params:
            form_params.append(('resolution', params['resolution']))
        if 'risk_level' in params:
            form_params.append(('risk_level', params['risk_level']))
        if 'service_id' in params:
            form_params.append(('service_id', params['service_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CustomSignature',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete(self, id, **kwargs):
        """
        Delete a(n) Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Custom Signature ID (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_with_http_info(id, **kwargs)
            return data

    def delete_with_http_info(self, id, **kwargs):
        """
        Delete a(n) Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Custom Signature ID (required)
        :return: Meta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete`")


        collection_formats = {}

        resource_path = '/api/v2/custom_signatures/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Meta',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, **kwargs):
        """
        Get a list of Custom Signatures
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, name, identifier] Matching Searchable Attributes: [name, identifier] Limited Searchable Attribute: [provider_eq] Sortable Attributes: [name, provider, updated_at, created_at, id] Searchable Associations: [organization, teams, definitions, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information.
        :param str page: Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Get a list of Custom Signatures
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :param dict(str, str) filter: Filter Params for Searching.  Equality Searchable Attributes: [id, risk_level, service_id, name, identifier] Matching Searchable Attributes: [name, identifier] Limited Searchable Attribute: [provider_eq] Sortable Attributes: [name, provider, updated_at, created_at, id] Searchable Associations: [organization, teams, definitions, integrations, suppressions] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information.
        :param str page: Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page.
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include', 'filter', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v2/custom_signatures.json_api'.replace('{format}', 'json_api')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'filter' in params:
            form_params.append(('filter', params['filter']))
        if 'page' in params:
            form_params.append(('page', params['page']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaginatedCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def show(self, id, **kwargs):
        """
        Show a single Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Custom Signature ID (required)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :return: CustomSignature
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_with_http_info(id, **kwargs)
        else:
            (data) = self.show_with_http_info(id, **kwargs)
            return data

    def show_with_http_info(self, id, **kwargs):
        """
        Show a single Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Custom Signature ID (required)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :return: CustomSignature
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `show`")


        collection_formats = {}

        resource_path = '/api/v2/custom_signatures/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CustomSignature',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update(self, id, **kwargs):
        """
        Update a(n) Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Custom Signature ID (required)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :param str description: The description of the custom signature that is displayed on alerts
        :param list[int] external_account_ids: The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run.
        :param str identifier: The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001
        :param bool include_new_accounts: When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user.
        :param str name: The name of the custom signature
        :param str resolution: Details for how to resolve this custom signature that is displayed on alerts
        :param str risk_level: The risk-level of the problem identified by the custom signature. Valid values are low, medium, high
        :param int service_id: The service this custom signature is for. If no service is selected it will default to Custom.
        :return: CustomSignature
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(id, **kwargs)
        else:
            (data) = self.update_with_http_info(id, **kwargs)
            return data

    def update_with_http_info(self, id, **kwargs):
        """
        Update a(n) Custom Signature
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Custom Signature ID (required)
        :param str include: Related objects that can be included in the response:  organization, teams, external_accounts, definitions, suppressions, service See Including Objects for more information.
        :param str description: The description of the custom signature that is displayed on alerts
        :param list[int] external_account_ids: The external account IDs this custom signature should run for. If no accounts are selected the custom signature will not be run.
        :param str identifier: The identifier to use for the custom signature. Common format is AWS:- such as AWS:IAM-001
        :param bool include_new_accounts: When enabled, automatically adds new accounts to this signature. This field can only be set by an organization level user.
        :param str name: The name of the custom signature
        :param str resolution: Details for how to resolve this custom signature that is displayed on alerts
        :param str risk_level: The risk-level of the problem identified by the custom signature. Valid values are low, medium, high
        :param int service_id: The service this custom signature is for. If no service is selected it will default to Custom.
        :return: CustomSignature
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include', 'description', 'external_account_ids', 'identifier', 'include_new_accounts', 'name', 'resolution', 'risk_level', 'service_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update`")


        collection_formats = {}

        resource_path = '/api/v2/custom_signatures/{id}.json_api'.replace('{format}', 'json_api')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'external_account_ids' in params:
            form_params.append(('external_account_ids', params['external_account_ids']))
            collection_formats['None'] = 'csv'
        if 'identifier' in params:
            form_params.append(('identifier', params['identifier']))
        if 'include_new_accounts' in params:
            form_params.append(('include_new_accounts', params['include_new_accounts']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'resolution' in params:
            form_params.append(('resolution', params['resolution']))
        if 'risk_level' in params:
            form_params.append(('risk_level', params['risk_level']))
        if 'service_id' in params:
            form_params.append(('service_id', params['service_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CustomSignature',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
