###admin/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET--админка
###news/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,POST--список новостей,создание новости
###news/<int:pk>/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,PUT--одна новость,изменение новости
###news/<int:pk>/delete/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DELETE--удаление новости
###news/<int:pk>/comments/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,POST--все комментарии к конкретной новости
###comments/<int:pk>/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET,PUT--комментарий ,изменение комментария 
###comments/<int:pk>/delete&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DELETE--удаление комментария
###news/<int:pk>/like/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST--лайк
###auth/signup/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST--регистрация нового пользователя
###auth/login/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST-- Логин 