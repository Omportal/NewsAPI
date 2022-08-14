## http://212.193.50.185
### admin/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET--админка
### news/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,POST--список новостей,создание новости
### news/<int:news_pk>/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,PUT--одна новость,изменение новости
### news/<int:news_pk>/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DELETE--удаление новости
### news/<int:news_pk>/comments/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,POST--все комментарии к конкретной новости
### news/<int:news_pk>/comments/<int:comment_pk>/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,PUT--комментарий ,изменение комментария 
### news/<int:news_pk>/comments/<int:comment_pk>/delete/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DELETE--удаление комментария
### news/<int:pk>/like/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST--лайк
### auth/signup/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST--регистрация нового пользователя
### auth/login/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST-- Логин 

### Логин для входа в админку: superuser ,пароль: superuser

### Для развёртывания на сервере были использованы Gunicorn , Nginx 

