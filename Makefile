init:
    conda env create -f environment.yml

test:
    python -m coverage run --source=pysd -m pytest -v tests

coverage:
    python -m coverage report -m

run:
    python -m pysd.core -i data/websites.txt -o out/

.PHONY: init test coverage run