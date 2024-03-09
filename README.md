# Arkanoid

## The Arkanoid game developed with pygame, as an example/exercise of programming



## Install

In the arkanoid folder:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m build
pip install dist/arkanoid-0.0.1-py3-none-any.whl
```

## Run
```bash
arkanoid
```


## Test
In the arkanoid folder:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
tox
```

## Uninstall
```bash
pip uninstall arkanoid
```
