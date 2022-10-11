# How to run 

```
> FLASK_ENV=development FLASK_APP=app.py flask run -p 5001
```

# Test

```
> http -v POST localhost:5001/sign-up name=joey email=zooyouny@gmail.com password=test1234
> http -v POST localhost:5001/sign-up name=joey2 email=zooyouny2@gmail.com password=test1234
> http -v POST localhost:5001/follow id:=1 follow:=2
> http -v POST localhost:5001/unfollow id:=1 unfollow:=2
> http -v POST localhost:5001/tweet id:=1 tweet="My First Tweet"
> http -v POST localhost:5001/tweet id:=1 tweet="My Second Tweet"
> http -v GET localhost:5001/timeline/1
```