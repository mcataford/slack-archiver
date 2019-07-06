# slack-archiver

## Why

__slack-archiver__ is a handy CLI tool that makes archiving your Slack workspace channels easily in a variety of formats and to purge messages in bulk.

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
|`format`|Formats the source. __This must be done to anything being committed__|
