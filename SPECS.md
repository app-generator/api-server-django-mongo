# Product Specification

Copyright (c) 2019 - present [AppSeed](http://appseed.us/)

<br />

## Requirements 

The product should provide a simple API Server with below features: 

<br />

**1# - API Methods** as defined by the [Unified API Descriptor](https://docs.appseed.us/boilerplate-code/api-server/api-unified-definition): [POSTMAN_collection](https://github.com/app-generator/api-server-unified/blob/main/api.postman_collection.json)


> USERS API:
    - `/api/users/register`: create a new user
    - `/api/users/login`: authenticate an existing user
    - `/api/users/logout`: delete the associated JWT token
    - `/api/users/checkSession`: check an existing JWT Token for validity
    - `/api/users/edit` - edit the information associated with a registered user

<br />

**2# - DATA Validation**

API Input should be sanitized and checked for consistance 

<br />

**3# - Unitary Tests**

All exposed API methods should have unitary tests

<br />

**4# - Docker**

<br />

The API should be provided with scrips to run Dockerized 

**5# - Persistance**

- **Master**: SQLite Persistance
- **Mongo**:  MongoDB Persistance 

<br />

**6# - Quality Checks**

The starter should pass all unitary checks and should be usable with a `production-ready` React UI already configured to work with the [Unified API Descriptor](https://docs.appseed.us/boilerplate-code/api-server/api-unified-definition)

- [React Datta Able](https://github.com/app-generator/react-node-js-datta-able) - open-source project

<br />

---
API Specs - AppSeed [App Generator](https://appseed.us)
