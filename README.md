<p align="center">
<img width="400" height="250" src="https://github.com/user-attachments/assets/1cd7fce2-5d40-45a1-992b-334508c70fe4">
</p>
<p align="center">
<img width="400" height="250" src="https://github.com/user-attachments/assets/0e864108-dfc2-4507-b480-e38f76741e1f">
</p>

Auto Dialer - утилита, которая нужна для того, чтобы упросить и ускорить звонки по объявлениям на Авито с ПК.

https://mega.nz/folder/hykXFS7J#QBKSS2lM4j2ZJKOPDqi4zA - скачивание браузерного расширения, необходимого для её работы и
самой утилиты в скомпилированном виде.

Связка "расширение - утилита Auto Dialer" работает так:
При нажатии  на кнопку "Показать номер телефона", расширение копирует PNG картинку с номером телефона в буфер обмена, затем
Python код автоматически забирает её, отправляет на распозвонание в Teseract OCR и автоматически совершает звонок по
полученному номеру телефона, одновременно сохраняя его в буфер обмена, уже в текстовом формате.

Таким образом, нет необходимости использовать User Agent Swithcer на Авито, с чем часто возникают проблемы (например, блокировки от Авито)
чтобы получать номер в тектовом формате. Звонок происходит в 1 клик и номер телефона не нужно набирать вручную.

Чтобы выбрать какая программма будет получать номер и совершать звонок - просто выберите её в настройках Windows
как программу по умолчанию, которая обрабатывает протокол "TEL".
