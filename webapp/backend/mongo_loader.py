from webapp import client, db, app

def loader():
    coll = app.config['MONGO_COLLECTION']

    pastes = db[coll].find({}, sort=[('_id', -1)]).distinct("PastebinLink")

    
