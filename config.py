dbname = "test"
password= "test"
mongourl = f"mongodb://puneet:{password}@cluster0-shard-00-00.1bfkc.mongodb.net:27017,cluster0-shard-00-01.1bfkc.mongodb.net:27017,cluster0-shard-00-02.1bfkc.mongodb.net:27017/{dbname}?ssl=true&replicaSet=atlas-xz2b37-shard-0&authSource=admin&retryWrites=true&w=majority"
