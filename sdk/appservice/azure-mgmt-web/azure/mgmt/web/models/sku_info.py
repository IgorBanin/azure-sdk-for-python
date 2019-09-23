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

from msrest.serialization import Model


class SkuInfo(Model):
    """SKU discovery information.

    :param resource_type: Resource type that this SKU applies to.
    :type resource_type: str
    :param sku: Name and tier of the SKU.
    :type sku: ~azure.mgmt.web.models.SkuDescription
    :param capacity: Min, max, and default scale values of the SKU.
    :type capacity: ~azure.mgmt.web.models.SkuCapacity
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'SkuDescription'},
        'capacity': {'key': 'capacity', 'type': 'SkuCapacity'},
    }

    def __init__(self, **kwargs):
        super(SkuInfo, self).__init__(**kwargs)
        self.resource_type = kwargs.get('resource_type', None)
        self.sku = kwargs.get('sku', None)
        self.capacity = kwargs.get('capacity', None)