
import pymongo
import ssl

def mongo():
    """  mongodb+srv://ricepotato:<password@cluster0-gpvm5.gcp.mongodb.net/wetube?retryWrit """
    connection_string = "mongodb+srv://ricepotato:<password@cluster0-gpvm5.gcp.mongodb.net"
    client = pymongo.MongoClient(connection_string, ssl=True, tlsAllowInvalidCertificates=True)
    wetube = client["wetube"]
    users = wetube.users.find({}, {})
    return list(users)


    