# AWS API GATEWAY SERVICE PROXY

This project allows you to define a list of microservices in the `services.json` file and then generate an AWS Cloudformation template that will provision a single endpoint that will proxy each request through to the services

## Usage

```
python generate.py

aws cloudformation create-stack --stack-name {example} --template-body file://data.template --profile {example (do not supply if default)}
```

### Post Stack Upload

![image-proxy](https://github.com/joshpauline/api-gateway-service-proxy/blob/master/images/proxyimage.png?raw=true)

![image-proxy1](https://github.com/joshpauline/api-gateway-service-proxy/blob/master/images/proxyimage1.png?raw=true)

![image-proxy2](https://github.com/joshpauline/api-gateway-service-proxy/blob/master/images/proxyimage2.png?raw=true)

### Note

- You will need to deploy the API gateway before being able to access the endpoint.
- My example does not require an Authorizer because I prefer to define the auth permissions at a service level

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
