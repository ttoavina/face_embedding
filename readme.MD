<marquee>
<h1>Scoring</h1>
</marquee>


A brief description of your project, what it does and why it's useful.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them. For example:

Python 3.8 or higher

### Installing

A step by step series of examples that tell you how to get a development env running.

Clone the repository<br>
Install the required packages using pip:
`pip install -r requirements.txt`<br>
Run the program using the following command:
python main.py

### Usage

#### Tri croisé:

```shell
optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    Fichier source sous forme CSV
  --config CONFIG  Fichier de configuration du fichier source
```

Example:
```shell
python decile.py --input ./scprepv.csv --target leave_stay --config config.json
```

#### Decile:
```shell
python decile.py --input ./scprepv.csv --target leave_stay --score scorepv --class-number 20 --confidence 0.5
```

#### Feature selection:
```shell
python feature_selection.py --input abo.csv --target leave_stay --p-value 0.001 --correlation 0.8
```



