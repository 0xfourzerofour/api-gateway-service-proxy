
import json
from pprint import pprint

base = {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {}
}

def generate_clouformation(data):

    add_root_service(data)

    for key, value in data["services"].items():
        add_service(data, key, value)

    return base
    

def add_root_service(data):
    base["Resources"][data['rootName']] = {
      "Type": "AWS::ApiGateway::RestApi",
      "Properties": {
        "Name": data['rootName'],
        "EndpointConfiguration": {
          "Types": [
            "EDGE"
          ]
        }
      }
    }

def add_service(data, key, value):
    base["Resources"][key] = {
      "Type": "AWS::ApiGateway::Resource",
      "Properties": {
        "RestApiId": {
          "Ref": data['rootName']
        },
        "ParentId": {
          "Fn::GetAtt": [
            data['rootName'],
            "RootResourceId"
          ]
        },
        "PathPart": key
      }
    }

    base["Resources"][f'{key}proxy'] = {
      "Type": "AWS::ApiGateway::Resource",
      "Properties": {
        "RestApiId": {
          "Ref": data['rootName']
        },
        "ParentId": {
          "Ref": key
        },
        "PathPart": "{proxy+}"
      }
    }

    base["Resources"][f'{key}method'] = {
      "Type": "AWS::ApiGateway::Method",
      "Properties": {
        "RestApiId": {
          "Ref": data['rootName']
        },
        "HttpMethod": "ANY",
        "ResourceId": {
          "Ref": f'{key}proxy'
        },
        "RequestParameters": {
          "method.request.path.proxy": True
        },
        "Integration": {
          "IntegrationHttpMethod": "ANY",
          "Uri": value,
          "Type": "HTTP_PROXY",
          "RequestParameters": {
            "integration.request.path.proxy": "method.request.path.proxy"
          }
        },
        "AuthorizationType": "NONE"
      }
    }


if __name__ == "__main__":
    with open('services.json') as f:
        data = json.load(f)
        result = generate_clouformation(data)
    
    with open('data.template', 'w') as fp:
        json.dump(result, fp)
    