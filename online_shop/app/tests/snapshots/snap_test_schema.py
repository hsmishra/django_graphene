# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_hey 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 1
                }
            ],
            'message': 'Cannot query field "hey" on type "Query".'
        }
    ]
}
