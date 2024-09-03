import facebook
import json
import os

def generateMetadata(api_route, graph, file_name=False):
    """
    Author: Abenezer Tamirat
    
    Accepts graph API object of facebook and returns a dict with prop message.

    """

    # preparing the file name to store the metadata
    if(not file_name): file_path = "facebook/m_data" + api_route + ".txt"
    else: file_path = "facebook/m_data" + file_name + ".txt"

    # try requesting the route for metadata
    # Checks the metadata for links to other nodes and run recursively
    # connections refer to connection to other api routes
    # If error encountered during request it prints it out

    try:
        response = graph.get_object(api_route, metadata="1", fields='')
        
        with open(file_path, "w") as file:
            json.dump(response, file, indent=4)
        
        if(('metadata' in response) and ('connections' in response['metadata'])):
            connections = parseConnections(api_route, response["metadata"]["connections"])
            available_connections = {}
            for route in connections:
                test, value = hasData(route, graph)
                if(test):
                    available_connections[route] = value
            
            for route in available_connections:
                generateMetadata(available_connections[route], graph, file_name=route)

    except facebook.GraphAPIError as e:
        print(f'! {file_path} $$ Error: {e}\n')
        return {"message": "failure"}
    
    print("**" + file_path + " ------- success\n")
    return {"message": "success"}


# It recieves all the connections of an api route to other api routes and returns a modified link to make a request
def parseConnections(parent, connections):
    links = []
    for connection in connections:
        link = parent + connection
        links.append(link)
    return links


# checks if an api route has data before generating a metadata for the route.
# If the api route has a data it stores it to facebook/data

def hasData(api_route, graph):
    file_path = "facebook/data" + api_route + ".txt"
    if (api_route == "/me/picture"): return (False, None)

    try:
        response = graph.get_object(api_route)
        if(('data' in response) and (len(response['data']) > 0) and ('id' in response['data'][0])):
            with open(file_path, "w") as file:
                try:
                    json.dump(response, file, indent=4)
                except:
                    print("Binary data dectected from: ", api_route)
                    return False
                return (True, response['data'][0]['id'])
            
        return (False, None)
    except facebook.GraphAPIError as e:
        return False, None
    

