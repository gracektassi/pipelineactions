import aws_cdk as core
import aws_cdk.assertions as assertions

from my_project1.my_project1_stack import MyProject1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_project1/my_project1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyProject1Stack(app, "my-project1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
