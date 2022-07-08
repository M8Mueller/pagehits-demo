from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    RemovalPolicy,
)
from constructs import Construct

import os.path
dirname = os.path.dirname(__file__)

class PagehitsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        backend = lambda_.Function(
            self, "pagehitsLambda",
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="lambda_handler.lambda_handler",
            code=lambda_.Code.from_asset(os.path.join(dirname, 'lambda_handler')))

        backend.apply_removal_policy(RemovalPolicy.DESTROY)

        api = apigateway.LambdaRestApi(
            self, "pagehitsRestApi",
            handler=backend,
            proxy=False
        )

        api.apply_removal_policy(RemovalPolicy.DESTROY)

        items = api.root.add_resource("items")
        items.add_method("GET") # GET /items
        # items.add_method("POST") # POST /items

        # item = items.add_resource("{item}")
        # item.add_method("GET") # GET /items/{item}

        # the default integration for methods is "handler", but one can
        # customize this behavior per method or even a sub path.
        # item.add_method("DELETE", apigateway.HttpIntegration("http://amazon.com"))
