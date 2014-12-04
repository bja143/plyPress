import MySQLdb
from _mysql import OperationalError
from plySrc import app

try:
    db = MySQLdb.connect("localhost", "root", "", "plypress")
except OperationalError:
    app.logger.error("Database server might be down")
    exit()
finally:
    app.logger.debug("database connection established")

try:
    cursor = db.cursor()
    app.logger.debug("cursor fetched")
except:
    app.logger.error("cursor object not fetched")


def disconnect():
    try:
        db.close()
    except:
        app.logger.error("couldn't tear down db connection")

def fetch_posts():
    try:
        cursor.execute('select * from post_master')
        data = cursor.fetchall()
    except:
        app.logger.error("Couldn't execute fetch_posts")
    posts = []
    
    if posts == None:
        return None
    else:
        for i in data:
            posts.append({
                          'title':i[1],
                          'date':i[3],
                          'username':i[4],
                          'text':i[2]})
    return posts

def fetch_post_by_id(id):
    try:
        
        cursor.execute("select * from post_master where post_id='%d'" % (id))
        data = cursor.fetchone()
    except:
        app.logger.error("Couldn't execute fetch_posts")

    post = {
           'title':data[1],
           'date':data[3],
           'username':data[4],
           'text':data[2]
           }
    return post
    
def insert_post(post):
    try:
        
        cursor.execute("select max(post_id) from post_master")
        fetched = cursor.fetchone()
        if fetched is None:
            post_id=0
        else:
            post_id = fetched+1
        cursor.execute('insert into post_master(post_id,post_title,post_content,posted_on,post_author,post_url) values (%s,%s,%s,%s,%s,%s)',[ post_id, post['title'], post['text'], post['date'], post['username'], post['url']])
        cursor.commit()
    except:
        app.logger.error("Couldn't execute insert_posts")
    
    if post_id is None:
        return 0
    
    return post_id
