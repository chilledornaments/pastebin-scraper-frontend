from webapp import client, db, app
from bson.objectid import ObjectId

def get_keywords():
    coll = app.config['MONGO_COLLECTION']
    pastes = db[coll].find({}, sort=[('_id', -1)]).distinct("Keyword")
    return pastes

def loader(alarm_status):
    coll = app.config['MONGO_COLLECTION']

    if alarm_status == "All":

        pastes = db[coll].find({}, sort=[('_id', -1)]).distinct("PastebinLink")

        response_json = {}

        for paste in pastes:
            query = db[coll].find({"PastebinLink": paste}, sort=[('_id', -1)])
            for q in query:
                ID = q['_id']
                Keyword = q['Keyword']
                Link = q['PastebinLink']
                RawData = q['RawData']
                try:
                    FalseAlarm = q['FalseAlarm']
                # This isn't defined yet, default to maybe
                except KeyError:
                    FalseAlarm = "Maybe"
                    # Update this record right now
                    updater(ID, "Maybe")
                response_json[ID] = {"Keyword": Keyword, "Link": Link, "RawData": RawData, "FalseAlarm": FalseAlarm}
        return response_json

    elif alarm_status == "Maybe":
        pastes = db[coll].find({"FalseAlarm": "Maybe"}, sort=[('_id', -1)]).distinct("PastebinLink")

        response_json = {}

        for paste in pastes:
            query = db[coll].find({"PastebinLink": paste}, sort=[('_id', -1)], limit=1)
            for q in query:
                ID = q['_id']
                Keyword = q['Keyword']
                Link = q['PastebinLink']
                RawData = q['RawData']
                FalseAlarm = q['FalseAlarm']

                response_json[ID] = {"Keyword": Keyword, "Link": Link, "RawData": RawData, "FalseAlarm": FalseAlarm}
        return response_json

    elif alarm_status == "Miss":
        pastes = db[coll].find({"FalseAlarm": "Miss"}, sort=[('_id', -1)]).distinct("PastebinLink")

        response_json = {}

        for paste in pastes:
            query = db[coll].find({"PastebinLink": paste}, sort=[('_id', -1)], limit=1)
            for q in query:
                ID = q['_id']
                Keyword = q['Keyword']
                Link = q['PastebinLink']
                RawData = q['RawData']
                FalseAlarm = q['FalseAlarm']

                response_json[ID] = {"Keyword": Keyword, "Link": Link, "RawData": RawData, "FalseAlarm": FalseAlarm}
        return response_json

    elif alarm_status == "Match":
        pastes = db[coll].find({"FalseAlarm": "Match"}, sort=[('_id', -1)]).distinct("PastebinLink")

        response_json = {}

        for paste in pastes:
            query = db[coll].find({"PastebinLink": paste}, sort=[('_id', -1)], limit=1)
            for q in query:
                ID = q['_id']
                Keyword = q['Keyword']
                Link = q['PastebinLink']
                RawData = q['RawData']
                FalseAlarm = q['FalseAlarm']

                response_json[ID] = {"Keyword": Keyword, "Link": Link, "RawData": RawData, "FalseAlarm": FalseAlarm}
        return response_json

def filtered_search(kw):
    coll = app.config['MONGO_COLLECTION']
    # Find distinct PasteBin URLs filtered by the keyword
    pastes = db[coll].find({"Keyword": kw}, sort=[('_id', -1)], limit=1).distinct("PastebinLink")

    response_json = {}

    for paste in pastes:
        query = db[coll].find({"PastebinLink": paste}, sort=[('_id', -1)], limit=1)
        for q in query:
            ID = q['_id']
            Keyword = q['Keyword']
            Link = q['PastebinLink']
            RawData = q['RawData']
            try:
                FalseAlarm = q['FalseAlarm']
            except KeyError:
                FalseAlarm = "Maybe"
                # Update this record right now
                updater(ID, "Maybe")
            response_json[ID] = {"Keyword": Keyword, "Link": Link, "RawData": RawData, "FalseAlarm": FalseAlarm, "ID": ID}

    return response_json

            
def updater(ID, alarm_status):
    coll = app.config['MONGO_COLLECTION']

    try:
        db[coll].update_one({"_id": ObjectId(ID)}, {"$set": {"FalseAlarm": alarm_status}})
        #a = db[coll].find_one({"_id": ObjectId(ID)})
        return "Successfully updated ObjectID: {}".format(ID)
    except Exception as e:
        message = "An error has occurred updating the record\n\n:Error -- {}".format(str(e))
        return message

