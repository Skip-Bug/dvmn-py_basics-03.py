from dotenv import load_dotenv
import os
import smtplib
load_dotenv('access.env')
login= os.getenv('login')
password= os.getenv('password')
email_from = input ("Адрес отправителя: ")
email_to = input ("Адрес получателя: ")
subject = input ("Заголовок письма: ")
friend_name = input("Введите имя друга: ")
website_input = input("Ваша реферальная ссылка: ")
website = website_input if website_input else "https://dvmn.org/profession-ref-program/gribojor/o2mpP/"
name = input("Введите свое имя: ")
my_name = name if name else "Леонид"
letter=f"""\
From: {email_from}
To: {email_to}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл. """
letter=letter.replace("%friend_name%",friend_name)
letter=letter.replace("%website%",website)
letter=letter.replace("%my_name%",my_name)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()