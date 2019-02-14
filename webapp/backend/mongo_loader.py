from webapp import client, db, app

def loader(alarm_status):
    coll = app.config['MONGO_COLLECTION']

    if alarm_status == "All":

        pastes = db[coll].find({}, sort=[('_id', -1)]).distinct("PastebinLink")

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
                # This isn't defined yet, default to maybe
                except KeyError:
                    FalseAlarm = "Maybe"
                    # Update this record right now
                    updater(id, "Maybe")
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

    elif alarm_status == "False":
        pastes = db[coll].find({"FalseAlarm": "False"}, sort=[('_id', -1)]).distinct("PastebinLink")

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

    elif alarm_status == "True":
        pastes = db[coll].find({"FalseAlarm": "True"}, sort=[('_id', -1)]).distinct("PastebinLink")

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
            
def updater(ID, alarm_status):
    coll = app.config['MONGO_COLLECTION']
    try:
        db[coll].update_one({'_id': ID}, {"$set": {"FalseAlarm": alarm_status}})
    except Exception as e:
        message = "An error has occurred updating the record\n\n:Error -- {}".format(str(e))
        return message


    print('i')
