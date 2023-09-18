# UrlShortening

### Author Note:

First of all, if you just want to run the code please look for [prerequisites][prerequisites-link]
and [how to run][how to run-link] sections :)

### Introduction:

In this task I have designed and Implemented a short_url service API that can generate and store mappings between 
generated short_url to its original_url.

### Technologies Used:

I have written this assignment in ```Python```.

Packages used:

1. FastAPI - framework that enables creating APIs.
2. uvicorn - web server implementation to run the service.
3. sqlalchemy - manages the DB.

### Assumptions:

1. The urls that need to be shortened are shorter than 8 chars (unless it won't short them but make them longer)
2. The urls that need to be shortened are no longer then 500 chars.

### Prerequisites

[prerequisites-link]: #prerequisites

1. make sure you have pip and python/python3 installed on you computer
2. clone the [repository](https://github.com/galtoren/UrlShortening) to your local PC:
3. navigate to the main directory of the project in the terminal: ```home_assignment``` and then to ```requirements```
4. check that ```packages_installer.py``` is in this directory (write: ```ls``` in the terminal, and look for the file)
5. run this line(if you have python change python3 to python):

   ```python3 packages_installer.py```

### How To Run

[how to run-link]: #how-to-run

1. navigate to the home_assignment directory and run:

   ```uvicorn app:app --host 0.0.0.0 --port 8000```

2. once the server is up, just go to postman, or any other client you desire:
    1. for generating new ```short_url``` =>
        1. paste http://0.0.0.0:8000/generate_shorter_url in the url
        2. in the body param you should pass the next format:
            ```{"url": "anyUrlYouWant"}```
        3. post :)
   
    2. in order to get the origin url:
        1.  paste http://0.0.0.0:8000/get_origin_url?url={short_url} in the url
        2.  don't forget to fill up the ```{short_url}``` param.

3. now, feel free to short what url you want :)