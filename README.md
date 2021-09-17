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
  
Добавление новых транзакций пользователя происходит по адресу localhost:<port>/add_transac_info/ в качестве тела запроса необходимо передать Json со структурой :
  {'id':'1', - тип string
  'card_number':321, - тип int
  'Credit_card': 'нет',  -'да'/'нет'
  'date':'01.01.01', - тип string
  'Amount':322, - тип float
  'currency':'RUR', - тип string
  'Purpose_of_payment': 'Пополнение PSB-RETAIL 00777782', - тип string
  'MCC_code':'3222', - тип float
  'MCC_decode':'3222 Sport Kazino' -тип string
  }
  В примере Json все значения представлены в качестве примера
