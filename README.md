# StudyWithMe
Добро пожаловать в мир продуктивной учёбы и работы!

## О проекте
Однажды в те редкие минуты, когда действительно хочется продуктивно потрудиться, я искал фоновое видео с шумом моря или дождя, или что-то в этом роде. Каким-то образом мне попался сервис [lifeat.io](https://lifeat.io/app?space=223), который предлагал множество видосов разной тематики для фоновой работы. Одним из преимуществ данного сервиса было наличие таймера типа Pomidoro (метод обучения, когда вы занимаетесь 25 минут и 5 минут после этого отдыхаете, после чего повторяете цикл)
<p>Этот сервис и был моим вдохновением!</p>

Вы можете попробовать desktop-версию этого сервиса с возможностью добавления собственных видео. В репозитории проекта встроены только демо-версии видео для того, чтобы размер проекта имел адекватные значения. Поэтому в папке ``media/videos`` Вы можете вставить свои видео файлы. Единственное, не забудьте поменять наименование файлов на стандартные (video1.mp4, video2.mp4 и тд.)

## Установка [Linux Mint/Ubuntu]
1.  Установка необходимых модулей 
    ```console
    python3 -m pip install -r requirements.txt
    ```
2. Установка дополнительного ПО для PyQt5
    ```console
    sudo apt install python3-pyqt5.qtmultimedia
    ```
