# cwk-flask-boilerplate

##Structure
This repository represents a simple, scalable structure that works well for Flask applications meant to be packaged 
and delivered as services/microservices. A Dockerfile for simple packaging is included.

The assumption made here is that there is a desire for consistency across services and a desire for reusable, 
modular blocks of functionality to reduce the upfront work of creating new services.

Though not implemented here, it could be entirely appropriate to use setuptools or other packaging frameworks to 
bundle the code as an installable package that is installed inside the Docker container rather than running the 
Python code directly.

In this example, all code is under the `app` directory, but the choice for that folder name is largely arbitrary. If you are using setuptools or other such packaging systems, you should follow the necessary conventions for said system. 

### The Framework
The `framework/` folder represents utility functions shared across the application. In a real application, 
these could and should be packaged using setuptools and installable via pip from a pypi repository (or however 
you choose to package your code) to make it importable and usable by an arbitrary number of Flask services that 
should share behavior. This is an effort to adhere to DRY (Don't Repeat Yourself) and OOP (Object Oriented Programming)
principles.

Functionality that would full under Framework functionality would include such things as:
* Application configuration code (parsing from environment variables, validating that required configuration keys are provided, etc.)
* Cloud provider interface code (i.e. the sort of things typically done using boto3, LibCloud, etc.)
* Secrets management code (e.g. code to authenticate to and pull secrets from Hashicorp Vault)
* ORM and database management code (SQLAlchemy models and interactions, Alembic migrations, pymongo utilities, etc.)
* Payload generation libraries (payload and/or envelope creation and standardization for arbitrary communications protocols)
* Messaging libraries (code used to connect to and interact with queuing, API, or RPC systems)
* RPC standardization (e.g. code for exposing or consuming gRPC or other standardized endpoints, managing ProtoBuffs, etc.)
* Metrics standardization (e.g. standardized functions for exposing metrics in Prometheus or other format)
* Logging standardization (e.g. Creating and customizing various log handlers and formatters for console and/or file based logging)
* User session management (e.g. validationg JWT tokens, credentials, etc.)
* Standardized health check code (e.g. checking for the presence and conenctivity of datastores or queuing systems, etc.)
* Any other functionality that might be repeated across multiple services

A fairly typical directory structure for a framework might be something like
```
framework/
  api/
    grpc/
    rest/
    swagger/
  config/
  cloud/
    aws/
    azure/
    gcp/
  database/
    alembic/
    models/
    orm/
  health/
    cloud/
    datastores/
    messaging/
  logging/
  messaging/
    payload/
    rabbitmq/
  secrets/
    kubernetes/
    vault/
```
### Utils
Though none are implemented here, any one-off utility functions that are specific to this particular service and would not be reasonable to include in the Framework should go here.

This would include any utility functions used by API endpoints (described below).

### Routes
In a simple service, such as the example here, we might be able to use only a single file to manage routes. 
In more complex service, these can and should be divided across multiple files to preserve readability and navigability of the code. 

We use the `@app.route` decorator in this example for routing as it provides the cleanest, most readable, and most understandable code. Only functions utilizing this decorator, i.e. the actual endpoint definitions themselves, should be included; any utility functions should go under the `utils` folder described above.

A standardized health check endpoint should always be provided and should be considered a baseline requirement for operating in Kubernetes.

There are multiple ways to collect and expose metrics and the solution used will be highly dependent on the solution chosen. 

