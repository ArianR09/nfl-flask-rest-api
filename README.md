NFL DATA MySQL exposed via REST API

Downloading a csv file, I imported it onto a MySQL database allowing the display of all players whom played in the NFL from the start-2013.
Using restful and flask, class models were made to gather information from inside the database, allowing the user to gather the information needed.
While have been created, using 'GET' requests, were used to gather information by either passing a String, or Integer as an argument to gather a
specific column that the user is trying to find. As the user was prompted of the data returned by using jsonify, would display either category that
is displayed in test.py
