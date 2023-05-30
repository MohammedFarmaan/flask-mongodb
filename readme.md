To run

```
conda activte <yourenv>

pip install -r requirements.json
    (this is only one time)

python app.py
```

before that i create a db called feat
inside it i have four collections
| employer_req
| employers
| engage_reqs
| users
just like json which was present in featurepreneur freelance

To view all employee req go to the givens route
http://127.0.0.1:5000/view

To view one requirements of specific employer
http://127.0.0.1:5000/view/req/28001

To view count of students engaged in one project
http://127.0.0.1:5000/view/req/engaged/28001
