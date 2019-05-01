# Flask-Blog

Based off of a tutorial by Corey Schafer (15 videos) :

1) https://youtu.be/MwZwr5Tvyxo -- Complete
2) https://youtu.be/QnDWIZuWYW0 -- Complete
3) https://youtu.be/UIJKdCIEXUQ -- Complete
4) https://youtu.be/cYWiDiIUxQc -- 22min



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

     $ pip install flask-sqlalchemy

     python
     >>> from flaskblog import db
     >>> db.create_all()
     >>> from flaskblog import User, Post
     >>> user_1 = User(username='Steven', email='sa@gmail.com', password='tempPassword')
     >>> db.session.add(user_1)
     >>> db.session.commit()
     >>> User.query.all()





----------------------------------------------------------------------
Issues :


----------------------------------------------------------------------

Dependencies :


BootStrap : https://getbootstrap.com/docs/4.3/getting-started/introduction/

Flask : http://flask.pocoo.org/

Flask Forms : https://flask-wtf.readthedocs.io/en/latest/index.html#

