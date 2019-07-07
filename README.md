# slack-archiver

## Why

__slack-archiver__ is a handy CLI tool that makes archiving your Slack workspace channels easily in a variety of formats and to purge messages in bulk.

## Installing

Until it is ready to be published to `pip`, you can install this by cloning and installing it as a local package via pip.

```
git clone git@github.com:mcataford/slack-archiver.git
python3 -m pip install [path to the repo] --user
```

## Usage

### Setting up a local config file

You can set up a local config file using the `init` command:

```
python3 -m slack-archiver init --token [your slack token]
```

### Archiving a channel in your workspace

_Once you have set up the config file_

```
python3 -m slack-archiver archive --channel [channel name]
```

This will produce a JSON archive of your channel in your current working directory.

## Contributing

### Getting set up

Get a virtual environment going and install dependencies
```
python3 -m virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

This project uses [invoke](http://www.pyinvoke.org/), use any of the commands below as `invoke [command]`.

|Command|Effect|
|---|---|
|`lint`|Checks source for formatting issues|
|`format`|Formats the source. __This must be done to anything being committed__|
|`test`|Runs all tests|
