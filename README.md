# Flask-Blog

Based off of a tutorial by Corey Schafer (15 videos) :

1) https://youtu.be/MwZwr5Tvyxo -- Complete
2) https://youtu.be/QnDWIZuWYW0 -- Complete
3) https://youtu.be/UIJKdCIEXUQ -- 23min



----------------------------------------------------------------------
Python installation issue :

	Error 0x80072efd: Cache thread exited unexpectedly.

	Solution : De-select "Download debugging symbols" or "Download debug binaries"

----------------------------------------------------------------------
     <CTRL>+`
     pip install flask

      export set FLASK_APP=flaskblog.py
     //$env:FLASK_APP = "run.py"
     http://127.0.0.1:5000/
     export set FLASK_DEBUG=1
     python flaskblog.py

     pip install flask-wtf

     <CTRL>+<SHIFT>+r : clear the browser cache and reload

     $ python
     >>> import secrets
     >>> secrets.token_hex(16)

----------------------------------------------------------------------
Issues :

1) Registration form is pre-populating with form data name 23:00min Vid 3 but not activating on-click



----------------------------------------------------------------------

Dependencies :


BootStrap : https://getbootstrap.com/docs/4.3/getting-started/introduction/

Flask : http://flask.pocoo.org/

Flask Forms : https://flask-wtf.readthedocs.io/en/latest/index.html#

