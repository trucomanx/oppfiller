# Packaging

Download the source code

    git clone https://github.com/trucomanx/oppfiller

The next command generates the `dist/OppFiller-VERSION.tar.gz` file.

    cd oppfiller/src
    python setup.py sdist

For more informations use `python setup.py --help-commands`

# Install 

Install the packaged library

    pip install dist/OppFiller-VERSION.tar.gz
