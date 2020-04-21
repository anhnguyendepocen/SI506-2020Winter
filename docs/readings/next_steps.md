
# Next Steps

## Summer review

Don't let Summer go by without writing code. Consider signing up for the Python 3 Programming
Specialization on the Coursera platform. As a University of Michigan student there is no charge for
enrolling in the five Python 3 specialization courses and earning a certificate. Indeed, given what you
have learned in SI 506 you should be able to move rapidly through the first four courses (it's largely all
review). Course 5 will have you working with third-party APIs and imaging libraries as part of a
data-analysis project.

**Coursera. UMSI Faculty, [Python 3 Programming Specialization](https://www.coursera.org/specializations/python-3-programming).**

## Virtual environments

When working on unrelated Python projects, I create a "virtual environment" for each. Doing so
creates an isolated development environment that allows each project to define its own dependencies
independent of other projects. This includes not only package dependencies and their versions but
also the Python version required for the project.

**Real Python, ["Python Virtual Environments: A Primer"](https://realpython.com/python-virtual-environments-a-primer/) (Real Python, nd).**

## Multiple arguments: *args, **kwargs

A function can be designed to accept a variable number of positional arguments (`*args`) or a
variable number of keyword arguments (`*kwargs`).

**Lisa Tagliaferri, ["How To Use *args and **kwargs in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3) (DigitalOcean, November 2017).**

 **Davide Mastromatteo, [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args/) (Real Python, September 2019)**

## Lambdas (anonymous functions)

A Lambda is an anonymous function, written as a single line of execution. You will often encounter
lambdas when working with classes or functions that accept a function as an argument.

**Andre Burgaud, ["How to Use Python Lambda Functions"](https://realpython.com/python-lambda/) (Real Python, June 2019).**

**Trey Hunner, ["Overusing lambda expressions in Python"](https://treyhunner.com/2018/09/stop-writing-lambda-expressions/) (Trey Hunner, September 2018).**

## Unit tests

The Python standard library includes a `unittest` module for writing unit tests (other test
frameworks are also available). Learning how to write unit tests will improve not just the code you
write but your development skills.

**Python 3.x Official Documentation, ["unittest — Unit testing framework"](https://docs.python.org/3/library/unittest.html) (python.org, nd).**

**Anthony Shaw, ["Getting Started With Testing in Python"](https://realpython.com/python-testing/) (Real Python, nd).**

## Regular Expressions

Defining search patterns that can match on complex character sequences calls for the use of regular
expressions (a.k.a regex or regexp) and the Python `re` module.

**Thomas Nield, ["An Introduction to Regular Expressions"](https://learning.oreilly.com/library/view/an-introduction-to/9781492082569/) (O'Reilly Media, Inc., June 2019).**

Solid introduction. Uses the online RegEx tester/debugger [regular expressions 101](https://regex101.com/).

## Generators

A Generator is a high-performance function that simplifies the building of iterators. It returns
what is known as a "lazy iterator" object, using a `yield` statement to suspend execution of the
loop temporarily in order to pass a value back to the caller "on demand" without actually exiting
the function. When the function is next called loop iteration continues yielding back the next value
in the sequence. Generators come in handy when working with very large data sets (e.g., large CSV
file).

**Dan Bader, ["What Are Python Generators?"](https://dbader.org/blog/python-generators) (dbader.org, nd).**

**Dan Bader, ["Generator Expressions in Python: An Introduction"](https://dbader.org/blog/python-generator-expressions) (dbader.org, nd).**

 **Kyle Stratis, ["How to Use Generators and yield in Python"](https://realpython.com/introduction-to-python-generators/) (Real Python, September, 2019).**

## Pandas, Numpy, and Matplotlib

If you are interested in data, data manipulation, and data science, then start learning
[Pandas](https://pandas.pydata.org/) now. Pandas is built on top of [Numpy](https://numpy.org/),
the base package for scientific computing. You will learn how to work with series, data frames
stored as numpy n-dimensional arrays and matrices. Then learn how to visualize your data starting
with the [Matplotlib](https://matplotlib.org/) package. You can also do your work and publish your
results using a web-based [Jupyter notebook](https://jupyter.org/).

**George McIntire, Brendan Martin, and Lauren Washington, ["Python Pandas Tutorial": A Complete Introduction for Beginners"](https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/).**

**Coursera. UMSI Faculty, [Applied Data Science with Python Specialization](https://www.coursera.org/specializations/data-science-python#courses).**

Five course specialization in data science. Courses and certificate are free for UMich students,
faculty, and staff. I expect this will prove a bit more challenging than the Python 3 specialization.

## Web development

If you are interested in web development consider exploring [Django](https://www.djangoproject.com/)
and/or [Flask](https://flask.palletsprojects.com/en/1.1.x/). Both are Python web frameworks designed
for rapid application development of database-driven web applications.

### Learning Django

**Charles Severance, [Django for Everybody (DJ4E)](https://www.dj4e.com/lessons).**

**Django Girls, [Django Girls Tutorial](https://tutorial.djangogirls.org/en/).**

**Mozilla, MDN web docs. [Django Web Framework (Python)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).**

**Vitor Freitas, ["A Complete Beginner's Guide to Django"](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).**

### Learning Flask

**Miguel Grinberg, [Flask Web Development](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/), 2nd Edition (O'Reilly Media, Inc., 2018).**

**Miguel Grinberg, ["The Flask Mega-Tutorial"](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).**

An impressive series of blog posts that get you up an running with Flask.

**Miquel Grinberg, ["The New and Improved Flask Mega-Tutorial"](https://courses.miguelgrinberg.com/p/flask-mega-tutorial).**

What started as a series of blog posts is now a formal, fee-based, course offering on Flask web development.

## Database design and development

TODO

## Git and Github

[Git](https://git-scm.com/) is a distributed version control system for tracking changes in source
code and other files. [Github](https://github.com/) is a hosting platform for developers (and others)
who version their work using git. Both the system and the platform are designed to support
collaborative work among programmers, but versioning your solo work and maintaining copies in the
cloud is smart practice.

**Roger Dudler, [git - the simple guide](http://rogerdudler.github.io/git-guide/).**

I love this guide.

**Ross Conyers, ["Learn Git in 3 Hours"](https://learning.oreilly.com/videos/learn-git-in/9781789348231).**

Video format. Videos grouped into four chapters. Chapter 4 focuses on Github.

* Chapter 1: Version Control and the Terminal
* Chapter 2: Learning the Basics of Git
* Chapter 3: Branches and Workflow
* Chapter 4: Advanced Git Workflow
