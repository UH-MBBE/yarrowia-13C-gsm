# _Yarrowia lipolytica_ E-Flux2

This project is a series of Jupyter notebooks focused on the analysis of the metabolism of the oleaginous yeast, Yarrowia lipolytica, when grown with glucose, glycerol, and oleic acid. The analysis ranges from growth parameter calculations to transcriptomic analysis, utilizing 13C-metabolic flux analysis a Genome-Scale Model (GSM).

- [System Requirements](#system-requirements)
- [Instructions for use](#instructions-for-use)
- [Summary of notebooks](#summary-of-notebooks)
- [Reference](#reference)
- [License](#license)

## System Requirements

The code was written using python 3.10.2

## Instructions for use

To run the code in this repository use the following commands:

<ol>
  <li>git clone https://github.com/garrettroell/yarrrowia_eflux2.git</li>
  <li>cd yarrrowia_eflux2</li>
  <li>python3 -m venv venv</li>
  <li>source venv/bin/activate</li>
  <li>pip install -r requirements.txt</li>
</ol>

## Summary of notebooks

- Notebook A: Experimental Growth Parameter Calculations
- Notebook B: Find Feasible Bounds for 13C-MFA using GSM and observed biomass yield
- Notebook C: Find GSM flux bounds by constraining the GSM with 13C-MFA
- Notebook D: Analysis of NADPH and Acetyl-CoA sources and sinks
- Notebook E: Comparative Transcriptomic Analysis in Y. lipolytica
- Supplemental Notebook A: Gene Annotation Correction in GSM iYLI647
- Supplemental Notebook B: Refining Yarrowia Biomass Reaction with Strain-Specific Data

## Reference

This work is currently unpublished.

## License

This code is distributed under the 3-Clause BSD license specified in the [license][1] file. It is open source and commercially usable.

[1]: license
