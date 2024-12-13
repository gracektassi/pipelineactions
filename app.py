#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_project1.my_project1_stack import MyProject1Stack


app = cdk.App()
MyProject1Stack(app, "MyProject1Stack222",    )

app.synth()
