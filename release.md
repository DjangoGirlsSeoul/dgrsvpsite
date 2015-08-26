How our releases work
---

For the main codeforeveryone.co website, we are running django 1.8 in a virtualenv on pythonanywhere. The database is (going to be) a mysql db also hosted on pythonanywhere.

Currently, the site is autodeployed on a merge to master. This happens by travis-ci running the tests and after all the tests pass, it runs a custom deploy to pythonanywhere.

The custom deploy adds the files to a folder in the pythonanywhere server, finds the git hash and saves it to a file. It then runs the `collectstatic` django command. `collectstatic` moves our static and user uploaded files into specified folders and then they are served by the webserver and not django. 

It then restarts the webserver and then the deploy is done! 