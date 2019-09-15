# How to create a new project

## Create a directory for the project

* Open a terminal (konsele/…)
* `cd directory/other_directory/…` to navigate to where you want to put the new project.
* `mkdir project_name` to create the directory.

## Start VSCode

* `cd project_name` to change to the new directory.
* `code .` to start VSCode for thi project.

## Create a file

* Click on the new-file icon to the right of the project name (hover over it to see the icon appear).
* Name the new file `<whatever_you_like>.py`.

### Initial content

Start off copying the following into your new file:

``` python
#!/usr/bin/env python3

print('Hello world!")
```

## Make the new file executable

* `chmod +x <whatever_you_like>.py`
* You can now run it as `./<whatever_you_like>.py` (so long as you are in the project directory)

## Tips and tricks

* `cd` all by itself gets you back to your home directory
