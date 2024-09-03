def callback(code):
    global access_token
    graph = facebook.GraphAPI(access_token=code, version='2.8')
    access_token = graph.get_access_token(app_id=app_id, app_secret=app_secret, grant_type='authorization_code', redirect_uri=redirect_uri)
    print("from function")
    print(access_token)

    return access_token


redirect_uri = 'http://localhost:8000/callback'
login_url = facebook.GraphAPI().get_auth_url(scope=['email', 'public_profile'], app_id=app_id, canvas_url=redirect_uri)

access_token = webbrowser.open(login_url)


graph = facebook.GraphAPI(access_token=access_token, version='2.8')