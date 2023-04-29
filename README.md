# Sakura
___
### Sakura is an imitation of a bookstore. After registering in the store, you can select books, add them to the cart and after placing an order. The order receipt will be sent to your mail.
___
### Local launch

#### Create a virtual environment
```
python3 -m venv venv
```
#### Activate virtual environment
```
source venv/bin/activate
```
#### Install dependencies
```
pip install -r requirements.txt
```
#### Make migrations
```
python manage.py migrate
```
#### Start local server
```
python manage.py runserver
```