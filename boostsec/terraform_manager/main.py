import json
from pprint import pprint

import hcl

from models import Tfvars


def parse_tfvars(file_path):
    with open(file_path, 'r') as f:
        tfvars_hcl = hcl.load(f)
    tfvars = Tfvars.model_validate_json(hcl.dumps(tfvars_hcl))
    pprint(tfvars)
    for k, org in tfvars.organizations.items():
        if not org.boost_org_features:
            print(k)
    # pprint(hcl.dumps(tfvars.model_dump_json()))
    with open("test.tfvars", 'w') as f:
        f.write(hcl.dumps(tfvars_hcl))



file_path = '/home/kraken/repos/boostsecurityio/terraform-releases/workspaces/dev/02-auth0/terraform.auto.tfvars'
parsed_data = parse_tfvars(file_path)