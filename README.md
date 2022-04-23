# RemoteScriptStarter
 A basic, unopinionated example of a Remote Script for Ableton Live 11. The goal of this script is to create a starting point for a new remote script with tools to help with development, like installing into an Ableton Live instance. It make no assumptions about your goals or the hardware you are using, so feel free to make anything you want. However, there's not much explanation here about what a Remote Script can do or how to do it. Luckily there are a few unofficial resources, like [Structure Void's Live API version 11 Documentation](https://structure-void.com/PythonLiveAPI_documentation/Live11.0.xml), [nsuspray API Documentation](https://nsuspray.github.io/Live_API_Doc/) or [Hanz Petrov's "Introduction to the Ableton Framework Classes"](http://remotescripts.blogspot.com/2010/03/introduction-to-framework-classes.html).

More Examples and Resources:

[Push2UserModeScript by jzgdev](https://github.com/jzgdev/Push2UserModeScript)
[Push 2 Midi Mappings](https://i2.wp.com/www.joshuacasper.com/contents/uploads/MidiMapping.png?ssl=1)

## Getting Started
The goal of this repo is to make creating a new Remote Script easy, so if there are any difficulties please let me know in the issues.

### Step 0: Have python installed
If you don't already, install a stable version of python on your computer. A download can be found [here](https://www.python.org/downloads/). This repo has not been tested with MacOS' default version of python (2), but if you find that it works please let me know.

### Step 1: Clone the repo
Use git clone to make a copy on your local machine. This project folder does not need to be put in any specific place, so feel free to put in a projects folder or Desktop. At this point I would suggest naming your project with git clone option name argument.

```shell
git clone https://github.com/isfopo/RemoteScriptStarter.git <YourRemoteScriptName>
```

### Step 2: Run the `rename.py` script
Included in the repo there is a script that allows you to quickly change the name of your remote script from the default `RemoteScriptStarter` name. Additional information about the arguments the script can use are in the file, but to change it to the same name as the top-level folder use this command: 

```shell
python rename.py
```

### Step 3: Install your script with `install.py`
In this repo there is also a script that will move how `src` folder to the appropriate location on your computer for Ableton Live 11 to compile and make your script available in the application. Note that this location is different in older versions of Ableton (10 and lower), so to install your script with these version you must do it manually. Additional information about the arguments the script can use are in the file, but to move your script to the default location of "User Library" with the name of your top-level directory simply run:

```shell
python install.py
```

Once the folder has been successfully copied you can start or restart Ableton for the code to compile to `.pyc` files and your script will be available in your set. Remote Script can be found under the MIDI section in Preference. Here are instructions.

This step, running the script and restarting Ableton, will need to be repeated in order to see any changes in your code, but I would suggest doing this before making any code changes in order to check my sanity. Please let me know if there are any issues. If the code does not compile or the script is not available then it is likely that there is an error in the code.

Note: Mac users who are not using their default version of python or have not changed their path to python3 will have to use `python3` instead of `python` to run these scripts

## Development Notes

Folders that start with a `_`, like `_Framework`, and `ableton` are included in this repo for convenience, but they should not be modified here. These are modules that will be exposed to your remote script within the Ableton environment, meaning the modules in this folder are never actually used. Having them in this folder prevents import error warnings and allows for auto-complete in your editor. These modules where downloaded from https://github.com/gluon/AbletonLive11_MIDIRemoteScripts, which has a number of other scripts that can be referenced in your script. These script are subject to change when Ableton releases an update, so it is possible that the code that is in this repo will become outdated. If that is the case, add an Issue or a PR to fix the problem.

If you are getting some kind of import error for the `Live` module, like `Warning: Import "Live" could not be resolved`, that can be ignored. Again, this is a module that will be used in the Ableton environment.

## Contribution
Feel free to fork and open a PR for whatever changes you would like to add, keeping in might that the goal of this repo is to have a blank slate to work off of. It's not really the place for specific hardware (ex. Launchpad) with specific functionality (ex. Clip Control), but having separate branches demonstrating how to incorperate either specific hardware or a specific feature might be helpful. 
