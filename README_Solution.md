# Requirements
Python 3.8

## First Steps - Creating the Environment
```cmd
pip install virtualenv
virtualenv venv

venv\scripts\activate (Windows)
or
source venv/bin/activate (Linux)

pip install -r requirements.txt
```
## First Steps - CLI commands
```cmd
cd src
python main.py --version
python main.py --help
python main.py combine-orders --help
python main.py n-open-contracts --help
```

# Solutions
## Question 1
```cmd
python main.py combine-orders 100 --orders [70,30,10]
```

## Question 2
```cmd
python main.py n-open-contracts 3 --open_contracts [[1,1],[2,2],[3,3],[4,4],[5,5]] --renegotiated_contracts [3]
```
