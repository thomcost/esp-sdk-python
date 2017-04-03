# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
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


class StatsApi(object):
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

    def for_report(self, report_id, **kwargs):
        """
        A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.for_report(report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int report_id: The ID of the report to retrieve stats for (required)
        :return: Stat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.for_report_with_http_info(report_id, **kwargs)
        else:
            (data) = self.for_report_with_http_info(report_id, **kwargs)
            return data

    def for_report_with_http_info(self, report_id, **kwargs):
        """
        A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.for_report_with_http_info(report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int report_id: The ID of the report to retrieve stats for (required)
        :return: Stat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method for_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_id' is set
        if ('report_id' not in params) or (params['report_id'] is None):
            raise ValueError("Missing the required parameter `report_id` when calling `for_report`")


        collection_formats = {}

        resource_path = '/api/v2/reports/{report_id}/stats.json_api'.replace('{format}', 'json')
        path_params = {}
        if 'report_id' in params:
            path_params['report_id'] = params['report_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Stat',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def latest_for_teams(self, **kwargs):
        """
        A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.latest_for_teams(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Stat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.latest_for_teams_with_http_info(**kwargs)
        else:
            (data) = self.latest_for_teams_with_http_info(**kwargs)
            return data

    def latest_for_teams_with_http_info(self, **kwargs):
        """
        A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.latest_for_teams_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Stat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method latest_for_teams" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/api/v2/stats/latest_for_teams.json_api'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Stat]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
