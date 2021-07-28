# AWS API GATEWAY SERVICE PROXY

This project allows you to define a list of microservices in the `services.json` file and then generate a single endpoint that will proxy each request through to the services

## Usage

```
python generate.py

aws cloudformation create-stack --stack-name {example} --template-body file://data.template --profile {example (do not supply if default)}
```


![image-proxy](https://github.com/joshpauline/api-gateway-service-proxy/images/proxyimage.png?raw=true)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
