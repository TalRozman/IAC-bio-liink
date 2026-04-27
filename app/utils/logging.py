from datetime import datetime
from app.database.mongo_client import logs

def insert_log(query:str,chunks:list[str],answer:str,citations:list[str],metadata:dict[str, str],duration:float):
    """
        Add a document to mongo db with the query info
        \nparam:
        \n\tstr: query
        \n\tlist[str]: chunks
        \n\tstr: answer
        \n\tlist[str]: citations
        \n\tdict[str,str]: metadata
        \n\tfloat: duration
        \nreturns: 
        \n\tNone
    """
    logs.insert_one({
        "Timestamp":datetime.now().timestamp(),
        "User Query":query,
        "Retrieved document chunks":chunks,
        "Generated answer":answer,
        "Source citations":citations,
        "Processing metadata":metadata,
        "Performance metrics": f"{duration} seconds"
    })