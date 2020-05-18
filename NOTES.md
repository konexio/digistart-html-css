# Notes for teachers

## Running a local server for a Live Share collaborative session

Check if Node.js and npm are installed:

```bash
which node
which npm
```

If they are not, install them:

```bash
sudo apt-get install nodejs
sudo apt-get install npm
```

Then install the [serve](https://www.npmjs.com/package/serve) package as a CLI tool:

```bash
sudo npm i -g serve
```

Then use it from the current session's directory:

```bash
serve
```

The default port is `5000`. In order to change it, use the `--listen` parameter:

```bash
serve --listen 8888

# Or shorter...
serve -l 8888
```
