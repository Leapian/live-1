# live-interview

Time: 20 min.

Important: Be chill, relaxed and do your best!

# Tasks app

- Fill the methods and classes of this app to create a fully working tasks app
- The app should connect to an API (will be provided) to get data of Tasks that need doing 
- The app then parses the data from the API in a TaskList
- We then display tasks based on the request of the user.

# Detailed Requirements
  1) Fetch a list of tasks from an API (will be provided at time of interview)
  2) Create one TodoTask for each task fetched from the server and insert these into the TaskList
  3) Based on user input, there are a couple of operations that we need to support. These actions are defined as methods in the TaskList class. Implement the functionality of these methods. 
  (Feel free to add any other methods, variables that you deem are needed for the completion of this exercise)

We recommend implementing the data fetch and list print functions first, then move onto implementing the other functionality.

# Useful Information
  1) The datetimes are provided in miliseconds from the server
  2) The id is provided from the server for each task

The tasks should be displayed in the format below

[ ] Task description / Due 12th Jan 2021 - For todo tasks

[x] Task description / Due 12th Jan 2021 - For done tasks

[o] Task description / Due 12th Jan 2021 - For overdue tasks

# Bonus task (After completing everyhting else, if there is time)
  - Results should be displayed ascending / descending based on a flag that the user can change and stays that way until the user changes it again
