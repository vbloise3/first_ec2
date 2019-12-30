#!/usr/bin/env python3

from aws_cdk import core

from first_ec2.first_ec2_stack import FirstEc2Stack


app = core.App()
FirstEc2Stack(app, "first-ec2")

app.synth()
