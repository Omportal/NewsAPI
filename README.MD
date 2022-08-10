
                     ROUTING

ADMIN/                            GET--админка
news/                             GET,POST--список новостей,создание новости
news/<int:pk>/                    GET,PUT--одна новость,изменение новости
news/<int:pk>/delete/             DELETE--удаление новости
news/<int:pk>/comments/           GET,POST--все комментарии к конкретной новости
comments/<int:pk>/                GET,PUT--комментарий ,изменение комментария 
comments/<int:pk>/delete          DELETE--удаление комментария
news/<int:pk>/like/               POST--лайк
auth/signup/                      POST--регистрация нового пользователя
auth/login/                       POST-- Логин 
