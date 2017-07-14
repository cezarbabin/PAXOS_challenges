## CHALLENGE #1 

#### RUNNING_INSTRUCTIONS

```shell
$ export FLASK_APP=p1.py
$ flask run
$ curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://127.0.0.1:5000/message
$ curl http://127.0.0.1:5000/message/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
```



#### EXTRA
We would need to be able to handle concurrent requests. This version only runs one single synchronous process and can handle only one request at a time. We could add workers through a tool like Gunicorn, in order to handle more requests at a time.  


## CHALLENGE #2

#### RUNNING_INSTRUCTIONS

```shell
$ cat prices.txt
Candy Bar, 500
Paperback Book, 700
Detergent, 1000
Headphones, 1400
Ermuffs, 2000
Bluetooth Stereo, 6000
```

For 2 items
```shell
$ python p2.py prices.txt 2 2500
```

#### EXTRA
For 3 items
```shell
$ python p2.py prices.txt 3 2500
```


#### RUNTIME
NlogN


## CHALLENGE #3

```shell
$ python p3.py 0X0X
```

#### RUNTIME
2^N (where N is the length of the input)
