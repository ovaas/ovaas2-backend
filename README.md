# Django rest Framework + Azure Database for Mysql

## Environment
- Windows
- Azure portal
- Azure CLI
- VS code
- Postman

## Set up
### 1, Create MySQL server from AzureCLI

Go to [Azure portal](https://portal.azure.com/), open Azure Cloud Shell
and enter the following command

#### Create azure resource group
```Azure CLI
> az group create --name <your resource group name> --location japaneast
```

#### Create Azure Database For mysql
```Azure CLI
> az mysql server create --resource-group <your resource group name> --name <servername> --location japaneast --admin-user <admin name> --admin-password <admin password> --sku-name  B_Gen5_1
```
※ "servername" must be unique.
※　"admin password" must be at least 8 characters and must contain 3 categories of characters: uppercase letters, lowercase letters, numbers, and non-alphanumeric characters.
※ You can change the price level after "--sku-name". Please check [here](https://docs.microsoft.com/ja-jp/azure/mysql/concepts-pricing-tiers) for details.

#### Setting firewall-rule
Go to MySQL resource and click "Connection security".
First, "Set Allow access to Azure services" to Yes.
Then "add the current client IP address" click to save

### 2, Create  Database

enter the following command

```Azure CLI
> mysql -h <your mysql server name> -u <your mysql admin name> -p --ssl
mysql> CREATE DATABASE <dbname>;
mysql> USE <dbname>;
```
※ "your mysql server name" and "your mysql admin name" are in the overview page.

### 3, Edit source code

ovaas_backend_django/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your dbname>',
        'USER': '<your mysql admin name>',
        'PASSWORD': '<your password>',
        'HOST': '<your mysql server name>',
        'PORT': '3306',
        'OPTIONS': {'ssl': {'ca': BASE_DIR/'ssl/BaltimoreCyberTrustRoot.crt.pem'}}


### 4, makemigrations

If you haven't migrated db, enter the following command:
```powershell
> python manage.py makemigrations
> python manage.py migrate
```

### 5, Create User

Add the username and password in the user_userinfo table in the Azure CLI.
```Azure CLI
mysql> INSERT into user_userinfo (username, password) VALUES ("<your name>", "<your password>")
```

## Send Request

### 1, Run server
```powershell
> python manage.py runserver
```

### 2, Set up Postman and send request

If set as in the example in the image below, it will return a JWT token.
![postman](.img/postman.png "postman")