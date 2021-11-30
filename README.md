# advisor-network-api

create advisor accounts at https://advisor-network-api.herokuapp.com/administrator/advisor/ add authorization token of admin ,name of advisor,image file to the request body.

register users at https://advisor-network-api.herokuapp.com/user/register/ add name,email and password to the request body.

login users at https://advisor-network-api.herokuapp.com/user/login/ add email and password to the request body.

view all user accounts at  https://advisor-network-api.herokuapp.com/users/ add authorization token of admin to the request body.

get the list of all advisors at https://advisor-network-api.herokuapp.com/user/<int:user_id>/advisor/ 

book a call with an advisor at https://advisor-network-api.herokuapp.com/user/<int:user_id>/advisor/<int:advisor_id>/ add authorization token of the user and {'appointment' : '2021-12-18T10:00'} in this format to the request body.

get list of all booked call for a user at https://advisor-network-api.herokuapp.com/user/<int:user_id>/advisor/booking/ add authorization token of the user to the request body.


Dummy data
admin - email : admin@gmail.com , password : admin  # admin already created only one admin can exist
user3 - email : user3@gmail.com , password : 12345
user4 - email : user4@gmail.com , password : 12345
user5 - email : user5@gmail.com , password : 12345
