# Scoop
### As of now only the backend is functional, the frontend is yet to be written
**Requirements:**
Python v3.7.7
Node.js v16.3.1

```bash
pip install -r requirements.txt
```

```
# API ENDPOINTS
GET "/" - returns {"Hello": "World"}
POST "/user/create" - creates a new user
POST "/user/sessions" - logs in user
POST "/user/{username}/score" -  currently a dummy end point -> to be upgraded
POST "/user/{username}/resume" - uploads a resume, and saves it onto the file system
POST "/user/{username}/keywords" - extracts common keywords from a user's resume, and the job description provided
```
