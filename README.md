# todolist django rest framework
a todolist api with django rest framework

Backend of: [todo app](https://faez-todoapp.netlify.app)

## installation
1. install python3 from <a href="https://www.python.or
g/" target="_blank">here</a> 
1. pip install -r requirements.txt
1. python manage.py migrate
1. python manage.py createsuperuser(insert user name and password)
1. python manage.py runserver
---
# api paths
* [**api/v1/**](#apiv1)
	* [**api/v1/todo/**](#apiv1todo)
		* [**api/v1/todo/add/**](#apiv1todoadd) 
		* [**api/v1/todo/edit/{pk}/**](#apiv1editpk)
		* [**api/v1/todo/delete/{pk}/**](#apiv1deletepk) 


* [**auth/v1/**](#authv1)
	* [**auth/v1/login/**](#authv1login)
		* [**auth/v1/login/refresh/**](#authv1loginrefresh)
	* [**auth/v1/register/**](#authv1register)
	* [**auth/v1/change_password/{pk}/**](#authv1change_passwordpk)
	* [**auth/v1/update_profile/{pk}/**](#authv1update_profilepk)
	* [**auth/v1/logout/**](#authv1logout)
	* [**auth/v1/change_image/**](#authv1change_image)


## api/v1/
### api/v1/todo/
**Allowed Methods** : GET
<br>**Access Level** : Authorized users
<br>return array of objects of all todos in the database related to the authorized user.
<br>you can get a specific todo object with passing the pk to the end of the path.

### api/v1/todo/add/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'title'}, 'optional': {"description", "image", "is_active", "priority", "send_email"}
<br>*POST :* The data should include fields available if user authorized.

### api/v1/todo/edit/{key}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': 'optional': {"title", description", "image", "is_active", "priority", "send_email"}
<br>*POST :* The data should include fields available if user authorized.

### api/v1/todo/delete/{key}/
**allowed methods** : DELETE
<br>**Access Level** : Authorized users
<br>*DELETE :* there is no data to send. you should put the key of products that are in user cart you want to delete in the url instead of *{key}*


## auth/v1/
### auth/v1/login/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password'}
<br>*POST :* the data you post should include 'username' and 'password' fields if the user was authorized the access token and the refresh token will return as json.[more information about JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)

#### auth/v1/login/refresh/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'refresh'}
<br>*POST :* the data you post should include 'refresh' and the value of it should be user refresh token that is sent when user login.

### auth/v1/register/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}
<br>*POST :* should include the 'fields' keys and proper value. errors and exceptions handled , should have a proper place to show them in frontend.

### auth/v1/change_password/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'old_password', 'password1', 'password2'}
<br>*PUT :* should include 'fields' keys with proper values. errors and exceptions handled , should have a proper place to show them in frontend.

### auth/v1/update_profile/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'optional': {'username', 'first_name', 'last_name', 'email'}
<br>*PUT :*  should include the authorized user access token. the uniqueness of email and username handled.

### auth/v1/logout/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'refresh_token'}
<br>*POST :* should include the authorized user access token. post user refresh token with 'refresh_token' key to expire the access and refresh token of the given user.

### auth/v1/change_image/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'image'}
<br>*PUT :* should include the authorized user access token
