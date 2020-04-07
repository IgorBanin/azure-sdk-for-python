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


class SubscriptionUpdateParameters(Model):
    """Subscription update details.

    :param owner_id: User identifier path: /users/{userId}
    :type owner_id: str
    :param scope: Scope like /products/{productId} or /apis or /apis/{apiId}
    :type scope: str
    :param expiration_date: Subscription expiration date. The setting is for
     audit purposes only and the subscription is not automatically expired. The
     subscription lifecycle can be managed by using the `state` property. The
     date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
     by the ISO 8601 standard.
    :type expiration_date: datetime
    :param display_name: Subscription name.
    :type display_name: str
    :param primary_key: Primary subscription key.
    :type primary_key: str
    :param secondary_key: Secondary subscription key.
    :type secondary_key: str
    :param state: Subscription state. Possible states are * active – the
     subscription is active, * suspended – the subscription is blocked, and the
     subscriber cannot call any APIs of the product, * submitted – the
     subscription request has been made by the developer, but has not yet been
     approved or rejected, * rejected – the subscription request has been
     denied by an administrator, * cancelled – the subscription has been
     cancelled by the developer or administrator, * expired – the subscription
     reached its expiration date and was deactivated. Possible values include:
     'suspended', 'active', 'expired', 'submitted', 'rejected', 'cancelled'
    :type state: str or ~azure.mgmt.apimanagement.models.SubscriptionState
    :param state_comment: Comments describing subscription state change by the
     administrator.
    :type state_comment: str
    :param allow_tracing: Determines whether tracing can be enabled
    :type allow_tracing: bool
    """

    _validation = {
        'primary_key': {'max_length': 256, 'min_length': 1},
        'secondary_key': {'max_length': 256, 'min_length': 1},
    }

    _attribute_map = {
        'owner_id': {'key': 'properties.ownerId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'primary_key': {'key': 'properties.primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'properties.secondaryKey', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'SubscriptionState'},
        'state_comment': {'key': 'properties.stateComment', 'type': 'str'},
        'allow_tracing': {'key': 'properties.allowTracing', 'type': 'bool'},
    }

    def __init__(self, *, owner_id: str=None, scope: str=None, expiration_date=None, display_name: str=None, primary_key: str=None, secondary_key: str=None, state=None, state_comment: str=None, allow_tracing: bool=None, **kwargs) -> None:
        super(SubscriptionUpdateParameters, self).__init__(**kwargs)
        self.owner_id = owner_id
        self.scope = scope
        self.expiration_date = expiration_date
        self.display_name = display_name
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.state = state
        self.state_comment = state_comment
        self.allow_tracing = allow_tracing