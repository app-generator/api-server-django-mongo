
# [Django API Server Mongo](https://github.com/app-generator/api-server-django-mongo)

Simple starter built with Python / Django Rest / Sqlite3 and JWT Auth. The authentication flow is based on [json web tokens](https://jwt.io).

<br />

> Features:

- ✅ [API Definition](https://docs.appseed.us/boilerplate-code/api-unified-definition) - the unified API structure implemented by this server
- ✅ Simple, intuitive codebase - built for beginners (can be extended with ease) 
- ✅ Django / Django REST / a simple, easy to use backend
- ✅ Authentication with JWT (JWT login, JWT logout, Register)
- ✅ **Persistance**:  `MongoDB`
- ✅ Unitary tests, Docker
- ✅ [API Interface Descriptor](https://github.com/app-generator/api-server-unified/blob/main/api.postman_collection.json): POSTMAN Collection

<br />

> Can be used with other [React Starters](https://appseed.us/apps/react) for a complete **Full-Stack** experience:

| [React Node JS Berry](https://appseed.us/product/berry-dashboard/api-server-nodejs/react/) | [React Node Soft Dashboard](https://appseed.us/product/soft-ui-dashboard/api-server-nodejs/react/) | [React Node Horizon](https://appseed.us/product/horizon-ui/api-server-nodejs/) |
| --- | --- | --- |
| [![React Node JS Berry](https://user-images.githubusercontent.com/51070104/176936514-f1bccb21-bafe-4b43-9e4c-b6fe0ec9511d.png)](https://appseed.us/product/berry-dashboard/api-server-nodejs/react/) | [![React Node Soft Dashboard](https://user-images.githubusercontent.com/51070104/176936814-74386559-4e05-43d5-b9a4-8f70ce96a610.png)](https://appseed.us/product/soft-ui-dashboard/api-server-nodejs/react/) | [![React Node Horizon](https://user-images.githubusercontent.com/51070104/174428337-181e6dea-0ad9-4fe1-a35f-25e5fa656a9d.png)](https://appseed.us/product/horizon-ui/api-server-nodejs/)

<br />

![Nodejs API Server - Open-source Nodejs Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/124414813-142aa180-dd5c-11eb-9279-6b082dadc51a.png)

<br />

## Requirements

- Django==3.2.5
- djangorestframework==3.12.4
- PyJWT==2.1.0
- django-cors-headers==3.7.0 
- djongo==1.3.6

<br />

## How to use the code

**Create** `.env` from `.env.sample`

Update the file with your data.

**Clone the sources**

```bash
$ git clone https://github.com/app-generator/api-server-django-mongo.git
$ cd api-server-django-mongo
```

**Create a virtual environment**

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

**Install dependencies** using pip

```bash
$ pip install -r requirements.txt
```

**Start the API server** 

```bash
$ python manage.py migrate
$ python manage.py runserver
```

The API server will start using the default port `8000`.

<br />

### [Docker](https://www.docker.com/) execution
---

> Get the code

```bash
$ git clone https://github.com/app-generator/api-server-django-mongo.git
$ cd api-server-django-mongo
```
Make sure the `DB_HOST` in the `.env` file is set to : `mongo`. As it's the name of the container
for the mongo database service in the `docker-compose.yml` file.

> Start the app in Docker

```bash
$ docker-compose up -d --build
```

Visit `http://localhost:5000` in your browser. The API server will be running.


<br />

## API

For a fast set up, use this POSTMAN file: [api_sample](https://github.com/app-generator/api-server-Django/blob/master/media/api.postman_collection.json)

> **Register** - `api/users/signup`

```
POST api/users/signup
Content-Type: application/json

{
    "username":"test",
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> **Login** - `api/users/login`

```
POST /api/users/login
Content-Type: application/json

{
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> **Logout** - `api/users/logout`

```
POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}
```

<br />

---
[Django API Server Mongo](https://github.com/app-generator/api-server-django-mongo) - provided by AppSeed [App Generator](https://appseed.us)
