
# Django-EmailSender

with  this app you can type your text in views and send that to several EmailSender




## Usage

1.Enable two Factor Authornication in your gmail account

2.go to settings.py and type your email and your authornicated password

3.go to views.py and type your mail in below order

Topic
Mail body
Senders email
email recievers 


do not forget that if you want to type several emails type  ,  between them




## Installation

first of all activate your virtual environment 

```bash
 py -3 -m venv .venv
.venv\scripts\activate
```
then install the requirements

```bash
   pip install -r requirements.txt
```

move to the project folder

```bash
   cd mail_project
```


## Deployment

To deploy this project run 

```bash
  python manage.py runserver
```


