#Test Strategy

## About
This document highlights the coverage method and the reasoning behind using the branch
coverage by our team. It also includes the reasoning for not taking any other coverage
which could also have been used for the Assignment. The decision taken in this document 
were through thorough discussion on some test cases and pieces of code by our team of 
two. This documents aim to express the decision ideas which were taken during the brain
storming session. 

##Coverages
###Conditional Coverage
This approach was not taken in account from the start because its `adds a plethora of test 
cases to implement`. Also in this Assignment, we coded the TASK1 to have a lot of IF 
statements but there are not a lot of else statements to execute. Just to have a 100% 
conditional coverage, our team would have wasted a lot of time making test cases, which 
are redundant or just useless to the TASK1.

###Path Coverage
Path coverage counts the number of paths used to find the coverage of the code. For a 
program in TASK1, it would have been very `difficult` to `draw and plan a Control Flow Path`
and pan out all the possible paths present inside the program. The implementation would 
turn out to be even difficult as there are many cases through which the user can get same
results. And for many, it would use the same path.  

###Statement Coverage
In Lectures, we were shown cases where `100% Statement Coverage might not give 100% Branch 
coverage` but it is true the other way round. In our TASK1, though there are less amount of
'else if' statements, it would be too far fetched to not consider the 'else and else if' 
statements at all. Hence, this coverage plan was ruled out.

###Decision Coverage
This method covers all the cases in the assignment with less effort and would have been 
the most `preferred choice` among the rest of the coverage methods. Decision Coverage 
reduces a lot of test cases from Conditional Coverage and ensures that each one of the 
possible branch from each decision point is executed at least once and thereby ensuring 
that all reachable code is executed. 

###Branch Coverage 
The method we used for the test strategy is branching coverage.
**Branching testing** method is useful in ensuring that each possible branch from a decision
point is _executed at least once_ and thereby ensuring that all reachable code is executed.
It also helps in checking or **validating** every branch to make sure that no branch leads to 
an unexpected behaviour of the program. It is the `most suitable approach` to tackle the 
assignment as it doesn't make the tasks complicated and does not provide a plethora of test
cases to implement.

Thank you for your time! 

##Author
**Created by Aryaman Singh & Yunpeng Cheng**



#openweather MANUAL

##About
**Welcome to *openweather.py* manual.** 
This manual contains all the necessary data
to use the *openweather.py* program to the fullest and aims to teach user the 
fundamentals.

The respective function is used to check various climate conditions of a particular 
place. It also provides features which outputs time of the place provided, all in all
it works as a handy weather program. But to use this program, it is necessary to know
all the features it provides with their following syntax.

##LETS GET STARTED
###API

To simply get all the data about the weather, this program uses the data from a website
named https://openweathermap.org/api . But for calling this site from the program, it
needs an accesskey/API code which helps to retrieve data securely and to only 
authorised members. __*Access key for this module is provided at the back*__. 

The syntax for putting the API key is 
* openweather.py -api 'API'

###Location

After the user has put the API, he/she has the option to put the arguments which
include the location. It is to be noted that the user cannot put different locations in
the following or use more than one of these arguments ::

1. name of city (-city)
1. city ID (-cid)
1. the ZIP code (-z)
1. geographic coordinates (-gc)

If the user doesnt choose any of the methods or decides to use more than one of these 
methods, then the user would get an error stating that *"You must specify only one of 
city name, city id, geographic coordinates or zip code".* 

The syntax for putting the location is 
* openweather.py -api 'API' -city 'Name of city'
* openweather.py -api 'API' -cid 'city ID'
* openweather.py -api 'API' -z 'ZIP code'
* openweather.py -api 'API' -gc 'xcoordinate ycoordinate'

###Functions

After signing the location, the user has the power to check the time or the climatic
condition flexibly. The user can put all the function behind the location and
the output given out by the program would be a flexible string containing all the data
which was put in by the user through the arguments.

The functions which are provided by the program are ::

1. temperature (-temp)
1. windy (-wind)
1. humidity (-humidity)
1. cloudy (-cloud)
1. sunset (-sunset)
1. sunrise (-sunrise)
1. pressure (-pressure)
1. time (-time) (FORMAT IS **YYYY-MM-DD HH:MM:SS**)

####Examples

Few example to see how it works :-

`openweather.py -api API -city Melbourne -time `

_OUTPUT :_ "On 2019-10-21 10:40:29, The temperature ranges from 11.11 - 14.44"

Keep in mind, the temperature might change according to different time and 
different city. 

Another example :-

`openweather.py -api API -city Melbourne -time -pressure -wind `

_OUTPUT :_ "On 2019-10-21 10:45:58, The temperature ranges from 9.44 - 11.11, 
Pressure is 1014hPa, Wind speed of 3.1 from 360 degrees"

Keep in mind, the variable data that includes temperature, pressure, and wind might 
change according to different time and different city. 

This is the end of the Manual. Thank you for your patience! 


##API KEY
_API KEY : a61cbb04fbd6033b201358290286a8ed_


##Author
**Created by Aryaman Singh & Yunpeng Cheng**
