# MusicEye
Run the following commands to run the engine
```
sudo apt install freepats python3-venv
python3 -m venv ~/music
source ~/music/bin/activate
```

Run the following commands to test the code.
 ```
 python -m pip install --upgrade pip
 pip install -r requirements.txt
 ```

 To train the model 
 ```
 python train.py
 ```

 To run using django
 ```
 python mangage.py makemigrations api
 python manage.py migrate
 python manage.py create superuser
 
 Enter required super user values and run

 python manage.py runserver 
 ```
 Make request on server and run the required output generated using play_midi.py

 ```
 python play_midi.py -f filenpath 
 ```

 Now install flutter using flutter docs and run the flutter using :
 ```
 cd mobile_app
 flutter run
 ```