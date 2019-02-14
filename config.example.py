class Config(object):
    SECRET_KEY = "a secret key that's really long and complicated"
    MONGO_PORT = 27017
    MONGO_DB_NAME = ''
    MONGO_COLLECTION = ''
    MONGO_URL = 'mongodb://localhost:%i' %(MONGO_PORT)
    # If the database requires authentication:
    # MONGO_URL = 'mongodb://username:password@host:%i/authDB' %(MONGO_PORT)
    # For example, if you created a the user "heyitsme" with a password of "yourbrother"
    # Who uses the database "hunter2" for auth, on localhost, your config would look like this:
    # MONGO_URL = 'mongodb://heyitsme:yourbrother@localhost:%i/hunter2