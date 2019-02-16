# Notification

* Dynamic notifications and sms template.
* User can create template and send it to user or group of users.



## Environment setup

### 1. Prerequisites

* Python v3.6
* Django v2.1.5
* Docker v18.09.2
* docker-compose v1.17.1
### 1. Prerequisites

```sh
$   git clone https://github.com/Ayasser/Notification.git
```
### 2. Build
```sh
$   docker-compose build
 ```
### 3. Run
```sh
$   docker-compose up
 ```
 
## OR

### 1. Prerequisites

* Python v3.6
* Django v2.1.5
* Virtualenv v16.4.0

### 2. Clone project


```sh
$   git clone https://github.com/Ayasser/Notification.git
```
    
### 3. Create Virtualenv

```sh
$   virtualenv env
 ```

### 4. Activate Virtualenv

```sh
$ source env/bin/activate
```

### 5. Install required packages inside virtualenv

```sh
$(env)  pip install -r requirements.txt
```

### 6. Verify

```sh
$(env)  manage.py runserver
```
