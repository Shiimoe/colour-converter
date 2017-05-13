# colour-converter
Converts between RGB and hex colour values.

## Installation
In your terminal, clone and enter the repository:
```shell
git clone https://github.com/Demonstrandum/colour-converter.git && cd colour-converter
```
then install the package through `setup.py`:
```shell
sudo python setup.py install
```
## Usage
From anywhere in your terminal write
```shell
colour-convert [COLOUR VALUE]
```
e.g.

`colour-convert 255, 14, 127`

`colour-convert 255 14 127`

which both yield `#ff0e7f`

and

`colour-convert "#ac6710"`

`colour-convert ac6710`

both would return  `172, 103, 16`
