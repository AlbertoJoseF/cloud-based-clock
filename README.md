# cloud-based-clock

#How to run

Include FLASK_APP to enviorment variables:

```bash
export FLASK_APP='clockService.py'
```

In this case, 'clockService.py' is our application's name. In any other case, were the application's name changes, include FLASK_APP to enviorment variables with new name:

```bash
export FLASK_APP='NEW APPLICATION NAME'
```

For running the server from the console type:

```
flask run
```

To check remote and local times go to: http://127.0.0.1:5000/clocks.html on browser.

To quit running server from console press CTRL+C.
