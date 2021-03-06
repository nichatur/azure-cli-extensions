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


class SchedulerInformation(Model):
    """SchedulerInformation.

    :param submitted_at:
    :type submitted_at: datetime
    :param scheduled_at:
    :type scheduled_at: datetime
    :param ended_at:
    :type ended_at: datetime
    :param cancellation_requested_at:
    :type cancellation_requested_at: datetime
    :param current_state: Possible values include: 'Queued', 'Scheduled',
     'Ended'
    :type current_state: str or ~azure.synapse.models.SchedulerCurrentState
    """

    _attribute_map = {
        'submitted_at': {'key': 'submittedAt', 'type': 'iso-8601'},
        'scheduled_at': {'key': 'scheduledAt', 'type': 'iso-8601'},
        'ended_at': {'key': 'endedAt', 'type': 'iso-8601'},
        'cancellation_requested_at': {'key': 'cancellationRequestedAt', 'type': 'iso-8601'},
        'current_state': {'key': 'currentState', 'type': 'str'},
    }

    def __init__(self, *, submitted_at=None, scheduled_at=None, ended_at=None, cancellation_requested_at=None, current_state=None, **kwargs) -> None:
        super(SchedulerInformation, self).__init__(**kwargs)
        self.submitted_at = submitted_at
        self.scheduled_at = scheduled_at
        self.ended_at = ended_at
        self.cancellation_requested_at = cancellation_requested_at
        self.current_state = current_state
