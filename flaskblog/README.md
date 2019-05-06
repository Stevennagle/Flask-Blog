# Flask-Blog

Based off of a tutorial by Corey Schafer (15 videos) :

     1) https://youtu.be/MwZwr5Tvyxo -- Complete
     2) https://youtu.be/QnDWIZuWYW0 -- Complete
     3) https://youtu.be/UIJKdCIEXUQ -- Complete
     4) https://youtu.be/cYWiDiIUxQc -- Complete
     5) https://youtu.be/44PvX0Yv368 -- Complete
     6) https://youtu.be/CSHx6eCkmv0 -- Complete
     7) https://youtu.be/803Ei2Sq-Zs -- 21 min


----------------------------------------------------------------------
Python installation issue :

	Error 0x80072efd: Cache thread exited unexpectedly.

	Solution : De-select "Download debugging symbols" or "Download debug binaries"

----------------------------------------------------------------------

CLI

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

     $ pip install flask-login



----------------------------------------------------------------------

DB :

     >>> user_1 = User(username='Steven', email='sa@gmail.com', password='tempPassword')
     >>> db.session.add(user_1)
     >>> db.session.commit()
     >>> User.query.all()

     >>> User.query.first()
     >>> User.query.filter_by(username='John').all()
     >>> user = User.query.filter_by(username='John').first()
     >>> user.id

     >>> User.query.get(2)
     >>> post_2 = Post(title='Blog 1', content='First Post Content', user_id=user.id)
     >>> db.session.add(post_2)
     >>> db.session.commit()

     >>> user.posts
     >>> for post in user.posts:
     ...     print (post.title)
     >>> post = Post.query.first()

     >>> post
     >>> post.user_id
     >>> post.author
     >>> db.drop_all()

     >>> User.create_all()
     >>> User.query.all()

----------------------------------------------------------------------

Hashing Passwords :

     $ pip install flask-bcrypt
     >>>from flask_bcrypt import Bcrypt
     >>>bcrypt = Bcrypt()

     >>> bcrypt.generate_password_hash('testing')
     b'$2b$12$gNtuAJE0/E3f2xYrP85MV.K1nGhQNXqekNC3zn.VX/eO0EmLkYram'

     >>> bcrypt.generate_password_hash('testing').decode('utf-8')
     '$2b$12$rQ7LfXiQbn2uQ8.WpoAtVO/Scuf2h2la20M49G2B8Ft9St7P107AG'

     >>> bcrypt.check_password_hash()
     >>> bcrypt.check_password_hash(hashed_pw, 'testing')



----------------------------------------------------------------------

Dependencies :

     BootStrap : https://getbootstrap.com/docs/4.3/getting-started/introduction/
     Flask : http://flask.pocoo.org/
     Flask Forms : https://flask-wtf.readthedocs.io/en/latest/index.html#
     sqlalchemy
     flask-bcrypt
     flask-login

