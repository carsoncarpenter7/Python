# CPSC 223p
## Lab 06
We shall learn how to use virtual environments and pip to manage Python software available for writing applications. Our labs will use plotting libraries to visualize data stored as [CSV](https://docs.python.org/3/library/csv.html) and [JSON](https://docs.python.org/3/library/json.html) data files.

# Background
In Python v.2, virtualenv is the preferred tool for creating virtual environments. Since Python v.3.3, the standard library module [venv](https://docs.python.org/3/library/venv.html#module-venv) is the preferred way to create virtual environments.

A summary of how to use virtual environments is given in [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments).

Should you wish to use `virtualenv` for Python3 then you must install additional software. On Debian-based systems such as Ubuntu and Raspbian, the software can be installed with the command `sudo apt install python3-virtualenv`. If in doubt, please speak with your instructor to ensure you have the appropriate software installed.

The two options are interoperable with each other and effectively have no difference for the purposes of these exercises.

# Instructions
Write a program for each exercise sub-directory. Each exercise subdirectory is prefixed with the string `part-`.

Every file that you submit must have a header. On the file that contains the main function, start the file with `#!/usr/bin/env python3`. Change the comment line (the one starting with ```#```) to state your full name. On the next line, start a new comment and state which section of CPSC 223p you are enrolled in. On the next line, start a new comment and state today's date. On the next line, start a new comment and state your CSUF email address. On the next line, start a docstring and provide a short description of the program you are writing. For example, if your name is Tuffy Titan and you are in CPSC 223p-01, the comment may look something like
  ```
  #!/usr/bin/env python3
  #
  # Tuffy Titan
  # CPSC 223p-01
  # 2050-01-01
  # tuffy.titan@csu.fullerton.edu
  #
  """
  This my first program and it prints out Hello World!
  """
  ```

Please adhere to the [Google Python coding style](https://google.github.io/styleguide/pyguide.html). Please read the style guide and ensure your code conforms. If it does not, then your assignment may not receive full credit. You may use a linter, such as `pylint`, and a style checker, such as `pycodestyle`, to check your source code to verify that it conforms to the specified style.

# Rubric
Each exercise is worth 5 points. There is a total of 15 points possible. Your program must compile, in other words be syntactically correct, before it is graded. Submissions that do not compile shall be assigned a zero grade. 

For each problem:

* Functionality (3 points): Your submission shall be assessed for the appropriate constructs and strategies to address the exercise.

* Compilation (1 point): Your submission shall compile with no warnings. Compile with errors results in a zero grade.

* Readability (1 point): Your submission shall be assessed by checking whether your code passess the style and format check, as well as how well it follows the proper naming conventions, and internal documentation guidelines. Git log messages are an integral part of how readable your project is.
