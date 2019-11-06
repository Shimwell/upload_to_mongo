import pymongo
client=pymongo.MongoClient(host="mongodb+srv://olinopass:nopass@airspeed-fgj30.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
col = db["testcol"]

data={
    "test": [
        {
            "testvar1":"testval1",
            "testvar2":"testval2",
            "testvar3":[
                {
                    "testsubvar1":"testsubval1",
                    "testsubvar2":"testsubval2"
                }
            ]
        }
    ]
}

testu = col.insert_one(data)