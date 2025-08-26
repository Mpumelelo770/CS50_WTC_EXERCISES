

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
-Introduction into APIs and making API requests using the python request library
-Gotten introduction into unit testing where testing files are used to test certain units of code. The units of code in this case are the individual functions inside of our program to be tested. 
-Unit testing is useful in that one doesnt have to perform the tests manually by checking the output for a given input.
-This taught me about structuring my code in a way that is possible to perform unit tests(usually by separating specific elements into functions).It is also important to note that the test files together with the programs to be tested should be in the same folder.
-One should be careful with exception handling when dealing with unit test. It is also very important to keep the type of inputs amd outputs when performing unit tests.
-Did basics of file I/O. I am confortable with opening files, reading from them and getting the information requred using the .reader function. Able to write into files using the .writer function.
-Did basics of reading and writing on csv files and using the csv library to correctly format my csv files when reading and writing on them.
-Did basics of the PIL(pillow) library which works with opening and manipulating images.
-Did regular expressions basics. Confortable using the re library and associated functions(search,sub,findall)
-Confortable using valitation PyPi packages to validate user inputs without having to create my own patterns.
-Introduction into classes. I am a bit confortable with creating classes and their need. I also understand what objects are and how we can create methods(inside the class) to operate on the object. Also dealing woth validation using the setter function. 

CHALLENGES

- Need to work more on higher order functions.
- Need to get used to reading documentation. Learned that the print functions has more parameters inside of it from documentation e.g \n to move to the next line as one of the default parameters of the print statement.
-Understanding how methods work on objects. i.e string methods, list methods etc
-Some more practice on debugging is needed.
-Need more practice on working with API,s and requesting different data from different databases/servers.Also need to grasp more of how the requests are stored inside of the JSON file and how i can access and iterate through some keys and values in the JSON file.
-Must know the real difference between API, server and a database.
-Should look further into the practises of performing unit tests. That is, what types of test should one consider for specific cases to exhaust all the edge cases.
-Working with the pillow library on my phone is almost impossible as pydroid doesnt open images correctly instead showing cryptic information that is difficult to understand. 
-I found that expressing a range of numbers to validate can be quiet tricky when working with regular expressions. These need attention to detail to correctly format. But overrall they are satisfyingly challenging. As with every topic, i need some more practise in the form of more activities to fully grasp the concepts of regular expressions and explore some more functions that come with the re library/module. Need to also checkout more PyPI validators functions to validate common inputs without having to figure out the validation pattern on my own. 
-When working with classes, i dont yet know how to decide on whether to use classes or functions. Also the diffent categories of methods inside the classes confuse me a bit(instancemethod, classmethod, @method).
Again,i think the most important this with classes and coding in general is to get used to forming the habit of reading and understanding documentation(especially with function/class  parameters/arguments).

# CS50\_WTC\_EXERCISES

EXERCISES DESCRIPTION

WEEK0: Functions and Variables

1. Indoor.py: This program converts a user inputted sentence into lower case
2. playback.py: This replaces any spaces in a given sentence into triple dots
3. Faces.py: Replaces :) and :( in a sentence with a happy and sad face emogis respectively
4. Einstein.py: Uses E = mc^2 to calculate the energy based on a given mass.
5. Tip.py: This calculates the tip to be given in a restaurant based on the bill and tip percentage based on the bill.


WEEK1: Conditionals

6. deep.py: This programme says YES if someone types 42/forty-two or forty two.Otherwise NO.
7. bank.py: This program gives someone some compensation based on how the bank worker greets the customer. If greeted with "hello", the customer gets nothing, if greeted with a work that starts with an "h", they get $20. Anything else they get $100. The greeting must be at the start of the sentence.
8. Extensions.py: This shows a files media type based on the files name(with the extension at the end, e.g readme.txt media type is text/plain)
9. interpreter.py: This does mathematical operations based on an expression from the user input
10. meal.py: This tells the user whether it is time for either breakfast, lunch or dinner based on the user input's time.


WEEK2: Loops

11. camel.py: Converts a string from camel case to snake case
12. coke.py: Informs the buyer about how much money is due based on how much they insert into the coke slot machine. at the end, it tells the user the amount owed/change if any.
13. twttr.py: removes vowels in a string
14. plates.py: determines the validity of a car's number plate based on various rules(comments in script)
15.nutrition.py: Returns the number of calories of a fruit based on user input 

WEEK3: Exceptions

16.fuel.py: Display the fuel as a percentage based on users input as a fraction.
17. taqueria.py: Displays the total bill to be payed based on user selected food.
18.grocery.py: A program that promots the user for a grocery list and outputs the number and the item name in alphabetical order. If for example the user inputs bananas twice on the grocery list, the output will be 2 bananas and other groceries in alphabetical order.
19. Outdated.py: This program takes a date formated like (m/d/y or month day, year) amd outputs the date formatted differently like (y/d/month)

WEEK4: Libraries

20. Emojize.py: This program uses the emoji library to convert certain text in a string(eg thumbs up) into emojis
21. Figlet.py: This program uses the pyfiglet library/module to converts simple text into big/bold text of a certain font specified by the user or a random font provided the user doesnt specify the font.
22.Adieu.py: This program uses the inflect library to say a phrase like (adieu, adieu to xxxx) where xxxx is the names specified by the user. Adieu means goodbye in french and therefore the program is saying goodbye to whoever name(s) is/are specifies by the user.
23.game.py: This program uses the random module to generate a random number between 1 and the number specifies by the user. The user is then asked to guess the randomly generated number until theh get it right.
24. professor.py: This program asks the user for a level(1,2 or 3) and gives the user 10 randomly generated mathematical operation where the level chosed indicates the number of gidits the user will be computing. e.g level 1 means the game will generate inly single digit addition operationg (1+1; 3+4 #etc)
25. bitcoin.py: Thia program uses the request module to make crypto API request about the information on bitcoin. The user uses terminal arguments to specify the number of bitcoins they would like to purchase where the program then generate the total value of the bitcoins to be purchased using information from the bitcoin json file.

WEEK5: Unit Test

-All the activities for this week were focused on performing unit test on the twttr.py, bank.py, plates.py and fuel.py where each of these programs were modified for ease of unit testing. The pytest library was used to perform some of the test(especially when dealing with errors)


WEEK6: File I/O

-Lines: This program counts the number of lines of code in a python file. It excludes comments and blank lines but includes docstrings
-Pizza: This program takes as input a csv file with pizza menus and prices. It then provide as input a table of the menu formatted in a more humanly readable way.
-Scourgify: This program takes in as input a csv file formatted as ("second_name,first_nam", last name) and outputs a csv file formatted as (first_name,second_name,last_name)
-shirt: This program taked in a cs50 shirt as an input and overlay that shirt on a persons picture which is then produced as an output.


WEEK7: Regular expressions

-numb3rs.py: This program validate an ip address which should be formatted as #.#.#.# where the "#" represents a number between 0 and 255
-watch.py: This program extracts a youtube url from a long HTML embedded url and shorten it using the seach function inside the re module
-working.py: This program converts the 22hr standard time to the 24hr format. e.g 9:00 AM to 5:00 PM is converted to 09:00 to 17:00. This uses the search function in re.
-um.py: This program counts the number of um's in a string using another re function called findall
-response.py: This program uses a PyPi package (validator-collection') to validate whether an email is valid or not without having to create ones own pattern and regex.

WEEK8: OBject Oriented Programming(OOP)

-seasons.py: This program uses the imported datetime class to calculate the difference between any previous time to the current time(can be used to calcukate the age if a person). It then ouputs that age in words converted to minutes.
-jar.py: This program creates a jar with a certain capacity where cookies can be puylt or removed from the jar. at any given time, one can check the number of cookies inside of the jar after a combination of adding+removing cookies from the jar.
-shirtificate.py: This program uses the fpdf2 class to create a CS50 pdf certificate with a CS50 shirt. A text of the format(Mpumelelo took CS50) is then overlayed onto the t-shirt where the cerficate is then saved as a pdf file.


