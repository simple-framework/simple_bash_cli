#!/usr/bin/python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This script extracts the LC fqdn's from the augmented site level config file
and saves the output to a new file

Installation:
virtualenv ~/.simple/lc_extractor
source ~/.simple/lc_extractor/bin/activate && pip install argparse pyyaml && deactivate

Example Usage:
source ~/.simple/lc_extractor/bin/activate && python extract-lc.py -f /etc/simple_grid/site_config/augmented_site_level_config_file.yaml -o ~/.simple/lc 
&& deactivate
"""

import yaml
import argparse

def parse_args():
    """Parse CLI arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    return {
        'augmented_site_level_config_file': args.filename,
        'output': args.output,
    }

if __name__ == "__main__":
    args = parse_args()
    site_fqdns = ['ls']
    with open(args['augmented_site_level_config_file'], 'r') as f:
        augmented_site_level_config = yaml.safe_load(f)
        site_fqdns = set([x['fqdn'] for x in augmented_site_level_config['site_infrastructure']])
    with open(args['output'], 'w') as f:
        f.write("\n".join(site_fqdns))
