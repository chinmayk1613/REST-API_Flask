# REST-API_Flask

REpresentation State Transfer is the software architecure which is use to communicate with web server in terms of request and response. REST API are very usefull when we want only data instead web page on which that data is present. Server will send us data in XML/JSON format which can be requested via API end points. The project contain the CRUD operation on video management syste. In this user can create new video, fetch the video name using video id, update the information about video such likes, views and comments etc and delete the videos. Serialization is most important thing that we need to do when we send back the response in json format. As database gives us model instance hence we have to serialize it to send over endpoint from server to client.

<code>__1. Create Operation : http://127.0.0.1:5000/{"name": "HI my video","likes":50000,"views": 1001}__</code>
