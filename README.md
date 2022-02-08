# Human Friendly Clock 
This is a clock that present the current time in a more "Human Friendly" way.

##Manual ##
Clone the repository to the local.

```angular2html
git clone https://github.com/jajajalalalala/human_friendly_text_clock.git
```

<br>

### Object 1 ###
Write a command-line program that returns the current time using the "Human Friendly Text" demonstrated in the example below.

In the folder, run command to get the current time:

```angular2html
> python main.py
```

Unit test can be executed via:

```angular2html
> python HumanFriendlyTextClockTest.py
```

<br>

### Object 2 ###

Allow the command to take an arbitrary Numeric Time parameter as input and return the "Human Friendly Text" equivalent.

In the repository folder, run the following command to get the specified time:

```angular2html
> python main.py -t <time>
```
or
```angular2html
python main.py --time <time>
```

<br>

### Object 3 ###
Write a REST service to expose the clock and allow an optional parameter to pass the arbitrary Numeric Time like Objective 2, returning the "Human Friendly Text" as JSON.

* Run the following terminal to start the server:

```angular2html
> python HumanClockREST.py
```
* Access the default URL  http://127.0.0.1:5000/ to get the current time json time.
* Attach the time to the end of the URL in HH:MM or H:MM format like http://127.0.0.1:5000/<specified_time> to get the specified time JSON.


