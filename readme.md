Setting up your local environment
-----

This assumes that you have python3 installed. (we are using 3.4 but this should work for most python 3 versions)

1. Clone the project by entering `git clone git@github.com:MOOCCircle/codeforeveryone.git` in the terminal
    - This will create a folder called `codeforeveryone` where you ran the command

2. Create a virtualenv by creating a new folder `mkdir virtualenvironments` and going into that folder `cd virtualenvironments` 

3. Create the virtual environment by running `venv codeforeveryone` (you might have to run `pyvenv codeforeveryone` instead if `venv` does not work or even `python3 -m venv codeforeveryone`)
    - If you are on windows, you might have some problems. Refer to https://docs.python.org/3/library/venv.html for help

4. Run `source bin/activate` to activate the virtualenv

5. Go into the `codeforeveryone` directory `cd ../codeforeveryone`

6. Run `pip install -r requirements.txt` to install the pip dependencies

7. Run `python manage.py runserver`

8. Success! (hopefully)

* If you see anything wrong here, please make an issue or a pull request!