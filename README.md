<p align="center">
<img width="400" height="250" src="https://github.com/user-attachments/assets/1cd7fce2-5d40-45a1-992b-334508c70fe4">
</p>


Auto Dialer - утилита для упрощенного и ускоренного осуществления звонков по объявлениям.

https://mega.nz/folder/UuVwGZJC#QBKSS2lM4j2ZJKOPDqi4zA - скачивание браузерного расширения, необходимого для её работы и
сама утилита в скомпилированном виде.

кАК ЭТО РАБОТАЕТ:
Связка "расширение - утилита Auto Dialer" работает так:
При нажатии  на кнопку "Показать номер телефона", расширение копирует PNG картинку с номером телефона в буфер обмена, затем
Python код автоматически забирает её, отправляет на распозвонание в Teseract OCR и автоматически совершает звонок по
полученному номеру телефона, одновременно сохраняя его в буфер обмена, уже в текстовом формате.

зАЧЕМ ЭТО НУЖНО:
Таким образом, нет необходимости использовать User Agent Swithcer на Авито, с чем часто возникают проблемы (например, блокировки от Авито)
чтобы получать номер в тектовом формате. Звонок происходит в 1 клик и номер телефона не нужно набирать вручную.

ЕСЛИ ЧТО-ТО НЕ РАБОТАЕТ
Чтобы выбрать какая программма будет получать номер и совершать звонок - просто выберите её в настройках Windows
как программу по умолчанию, которая обрабатывает протокол "TEL".
Если не знаете где находятся эти настройки, запустите файл tels.bat, в открывшемся окне в поиске введите TEL и установите Софтфон по умолчанию.

@fet157 - если нашли баг или что-то не получается настроить - пожалуйста, напишите мне в Telegram.

-------------------------------------------------------------------------------
РАЗРАБОТЧИКАМ                                                              
                                                                              
Для билда:                                                                 
                                                                              
- создать виртуальное окружение                                               
- установить зависимости - pip install req.txt                                
- компилировать - pyinstaller --onefile --noconsole --name "Auto Dialer" main.py            
- готово, забираем exe из папки dist.                                         
                                                                              
Залить распакованный Teseract OCR в ту же папку, где у вас будет лежать exe   
(https://mega.nz/folder/Bml0QDYC#6CLg0XOgsUAxp0ZczkrUXg)                      
                                                                              
Файл Auto Dialer.ico тоже скопировать в папку с exe.                          
