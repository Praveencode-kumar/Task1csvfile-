import facebook

page_access_token = "YOUR TOKEN GOES HERE"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "1792403390912826"
graph.put_object(facebook_page_id, "feed", message='test message')