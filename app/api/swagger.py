query_endpoint={
        "consumes": ["multipart/form-data"],
    "parameters": [{
        "in": "formData",
        "name": "question",
        "type": "string",
        "description": "A general question, not based on a file",
        "required": True,
        },],
    "responses":{
        "200":{
            "description":"successfully generated an answer",
            "schema":{
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "example": "True"
                    },
                    "message": {
                        "type": "string",
                        "example": "successfully answered the question"
                    },
                    "data": {
                        "type":"object",
                        "properties":{
                            "answer":{
                                "type":"string",
                                "example":"the name of the first us president is George Washington"
                            },
                            "sources":{
                                "type":"object",
                                "properties":{
                                    "file name":{
                                    "type":"array",
                                        "items":{
                                        "type":"string",
                                        "example": "[citation1, citation2]"
                                        }
                                    },
                                }
                            },
                        },
                        "example": {
                            "answer": "the name of the first US president is George Washington",
                            "sources":{
                                "History for dummies" : ["US presidents", "US history"]
                            }
                        }
                    }
                }
            }
        },
        500:{
            "description":"An Error occurred",
            "schema":{
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "example": "False"
                    },
                    "message": {
                        "type": "string",
                        "example": "Failed to answer the question "
                    },
                }
            }
        },
    }
}