# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import json
from aws_cdk import core as cdk
from os import path
from aws_cdk.assertions import Template
from common_cdk.foundations import DataLakeFoundations


def test_matches_snapshot(snapshot):
    app = cdk.App()
    main_stack = cdk.Stack(app, 'MainStack')
    datalake_foundation_stack = DataLakeFoundations(main_stack, "Foundations")
    assembly = datalake_foundation_stack.node.root.synth()
    template = get_template(datalake_foundation_stack)
    
    print(json.dumps(template.to_json(), indent=4))
    assert template is snapshot



def get_template(stack: cdk.NestedStack):
    template_path = path.join('cdk.out', stack.template_file)
    print('##template_path', template_path);
    content = open(template_path, 'r')
    print(content)
    return Template.from_string(content)