# promsvyaz

## Развертка backend

Инструкция для macOS и Linux

1) Установка Python https://python-scripts.com/install-python  
2) Установка пакетного менеджера pip http://helpexe.ru/programmirovanie/kak-ustanovit-pip-dlja-python-v-windows-mac-i  
3) Переход в директорию PSB
Затем активируем виртуальное окружение: source venv/bin/activate  
4) Затем cd PSB-backend/PSB_PFM  
5) Установка необходимых библиотек: pip install -r requirements_backend.txt  
6) Проведение миграций: make migrate  
7) Запуск сервера: make run  

## Развертка frontend:
1) Установка node.js  
2) Установка npm/любого другого пакетного менеджера  
3) Установка vue  
4) Переход в директорию PSB/psb-frontend   
5) Запуск сервера npm run serve  

*В случае наличия ошибок в новом окне терминала исполнить команду npm run lint — —fix*

## Описание приложения:

Наличие главной страницы по адресу localhost:<port>/

Наличие страницы авторизации по адресу localhost:<port>/signin. Достижима из хэдэра любой страницы (Пункт меню «Вход»)

Авторизация происходит после введения любого id пользователя из изначальной базы данных и ввода пароля «1234» - установлен для всех пользователей

Наличие профиля для каждого из пользователей из исходной базы по адресу localhost:<port>/profile