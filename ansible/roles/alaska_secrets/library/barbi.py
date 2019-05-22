#!/usr/bin/env python

# import some python modules that we'll use.  These are all
# available in Python's core

ANSIBLE_METADATA = {'metadata_version': '1.0'}

import sys
import json
import os

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.openstack import openstack_full_argument_spec, openstack_module_kwargs, openstack_cloud_from_module


def main():
    argument_spec = openstack_full_argument_spec(
        key=dict(required=True, type='str'),
    )
    module_kwargs = openstack_module_kwargs()
    module = AnsibleModule(argument_spec, **module_kwargs)

    sdk, cloud = openstack_cloud_from_module(module)

    secret_key = module.params['key']
    secret = cloud.key_manager.find_secret(secret_key)
    if secret:
        module.exit_json(changed=False, secret=secret.payload)
    else:
        msg = "Failed to retrieve secret with key '%s'".format(secret_key)
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
