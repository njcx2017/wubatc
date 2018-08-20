from pymongo import MongoClient

def get_db():
    #建立连接
    client = MongoClient("localhost", 27017)
    #test,还有其他写法
    db = client.test
    return db

def get_collection(db):
    #选择集合(mongo中collection和database都是lazy创建的，具体可以google下)
    collection = db['posts']
    print(collection)
	

def insert_one_doc(db):
    #插入一个document
    posts = db.posts
    post = {"name":"lzz", "age":25, "weight":"55"}
    post_id = posts.insert(post)
    print(post_id)
	
def insert_mulit_docs(db):
    #批量插入documents,插入一个数组
    posts = db.posts
    post = [ {"name":"nine", "age":28, "weight":"55"},
                 {"name":"jack", "age":25, "weight":"55"}]
    obj_ids = posts.insert(post)
    print(obj_ids)
	
##查询，可以对整个集合查询，可以根ObjectId查询，可以根据某个字段查询等
def get_all_colls(db):
    #获得一个数据库中的所有集合名称
    print(db.collection_names())

	
def get_one_doc(db):
    #有就返回一个，没有就返回None
    posts = db.posts
    print (posts.find_one())