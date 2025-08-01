

#GITLAB PROGRESS

TAKE-AWAYS

-Able to download and configure git.
-setting up ssh keys for both gitlab and github
-Able to use basic git commands(git init, git status, git add, git commit, git remote add origin, git push,git fetch,git pull,git log)
-cloning a repository (git clone) and creating side branches(git branch ...). switching between branches(git checkout) and merging side branches with main branch(git merge side-branch).
-pushing a side/feature branch to the remote (gitlab/github) and creating merge requests.
-Creating issues, merge requests, labels,assigning issues and merge request.
-Introduction into CI/CD. This has to do with collaborative work where for each push, automated tests are performed that are specified in the YAML file. Configuring a runner is required for the tests/jobs inside of the YAML file to be executed. This process can also be automated without configuring any yaml files and runners by just doing the AutoDevOps automated testing.
-Some introduction into the various roles in the software engineering industry. e.g DevOps engineers.

CHELLENGES

-Working on my phone can be quiet challenging.
-Understanding the difference between the main/master, pre-production and production/release branches in gitlab.
-Diffetentiating and finding similarities between gitlab and github can be confusing sometimes.
-Difficult to visualize how version control together with pull request work when multiple developers are working on a single project instead of just me alone. Would be interesting to work with multiple people on a single project to fully understand the ideas of branching,pull requests and merge conflicts.
-Need more practical work to fully grasp the concencepts of continuos intergration(CI) and continuos delivery/deployment(CD)



#PYTHON BASICS PROGRESS

TAKE-AWAYS

- Confortable with variable(integiers, string, floats, booleans).
-Confortable working with functions(parameters, arguments, return statements, side effects, function call)
- Confident working with conditionals. They go hand in hand with boolean statements
- A bit confortable working with loops(for, while). Need a bit more work visualising the while loop especially infinite loops and how many iterations it is going to have.
-Introducrd to data types (Lists, Dictionaries, Tuples)
-Learned about the main function
-Learned basic VScode commands on working with files( mkdir, cd, rmdir, code something.py etc)
-Learned about handling errors using the (try-except-else-pass statements).
-Leaned the different types of errors we can come across in python.
-Learned that i can raise my own errors by using the raise statements.
-Introduced to debugging using VScode(breakpoints) and associated controls(stepping over, stepping into) to visually see how the code works and easily deal with logic errors. Syntax errors are the simplest to deal with.
-Introduction into modules and libraries. We have build in modules in python, we can create our own or we can get from the internet using the pip install command on the command line. We can also create our packages/library. 
-Know didference between a a library/package, module and a function.
-Introduction into API's and making API requests using the python request library

CHALLENGES

- Need to work more on higher order functions.
- Need to get used to reading documentation. Learned that the print functions has more parameters inside of it from documentation e.g \n to move to the next line as one of the default parameters of the print statement.
-Understanding how methods work on objects. i.e string methods, list methods etc
-Some more practice on debugging is needed.
-Need more practice on working with API,s and requesting different data from different databases/servers.Also need to grasp more of how the requests are stored inside of the JSON file and how i can access and iterate through some keys and values in the JSON file.
-Must know the real difference between API, server and a database.


# CS50\_WTC\_EXERCISES

EXERCISES DESCRIPTION

WEEK0

1. Indoor.py: This program converts a user inputted sentence into lower case
2. playback.py: This replaces any spaces in a given sentence into triple dots
3. Faces.py: Replaces :) and :( in a sentence with a happy and sad face emogis respectively
4. Einstein.py: Uses E = mc^2 to calculate the energy based on a given mass.
5. Tip.py: This calculates the tip to be given in a restaurant based on the bill and tip percentage based on the bill.


WEEK1

6. deep.py: This programme says YES if someone types 42/forty-two or forty two.Otherwise NO.
7. bank.py: This program gives someone some compensation based on how the bank worker greets the customer. If greeted with "hello", the customer gets nothing, if greeted with a work that starts with an "h", they get $20. Anything else they get $100. The greeting must be at the start of the sentence.
8. Extensions.py: This shows a files media type based on the files name(with the extension at the end, e.g readme.txt media type is text/plain)
9. interpreter.py: This does mathematical operations based on an expression from the user input
10. meal.py: This tells the user whether it is time for either breakfast, lunch or dinner based on the user input's time.


WEEK2

11. camel.py: Converts a string from camel case to snake case
12. coke.py: Informs the buyer about how much money is due based on how much they insert into the coke slot machine. at the end, it tells the user the amount owed/change if any.
13. twttr.py: removes vowels in a string
14. plates.py: determines the validity of a car's number plate based on various rules(comments in script)
15.nutrition.py: Returns the number of calories of a fruit based on user input 

WEEK3

16.fuel.py: Display the fuel as a percentage based on users input as a fraction.
17. taqueria.py: Displays the total bill to be payed based on user selected food.
18.grocery.py: A program that promots the user for a grocery list and outputs the number and the item name in alphabetical order. If for example the user inputs bananas twice on the grocery list, the output will be 2 bananas and other groceries in alphabetical order.
19. Outdated.py: This program takes a date formated like (m/d/y or month day, year) amd outputs the date formatted differently like (y/d/month)
