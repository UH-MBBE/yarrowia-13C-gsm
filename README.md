# _Yarrowia lipolytica_ <sup>13</sup>C-MFA Constrained GSM

This project is a series of Jupyter notebooks focused on the analysis of the metabolism of the oleaginous yeast, <i>Yarrowia lipolytica</i>, when grown with glucose, glycerol, and oleic acid. The analysis involves growth parameter calculations, using a genome scale model (GSM) to generate feasible flux ranges for <sup>13</sup>C-MFA, using <sup>13</sup>C-MFA results to constrain GSM reaction rates, and transcriptomic analyses.

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
  <li>git clone https://github.com/UH-MBBE/yarrowia-13C-gsm.git</li>
  <li>cd yarrowia-13C-gsm</li>
  <li>python3 -m venv venv</li>
  <li>source venv/bin/activate</li>
  <li>pip install -r requirements.txt</li>
</ol>

## Summary of notebooks

- Notebook A: Experimental Growth Parameter Calculations
- Notebook B: Find Feasible Bounds for <sup>13</sup>C-MFA Using GSM and Observed Biomass Yield
- Notebook C: Find GSM Flux Bounds by Constraining the GSM with <sup>13</sup>C-MFA
- Notebook D: Plot Figures Related to the GSM
- Notebook E: Comparative Transcriptomic Analysis in <i>Y. lipolytica</i>
- Supplemental Notebook A: Gene Annotation Correction in GSM iYLI647
- Supplemental Notebook B: Refining <i>Y. lipolytica</i> Biomass Reaction with Strain-Specific Data

## Reference

This work is currently being prepared for publication

## License

This code is distributed under the 3-Clause BSD license specified in the [license][1] file. It is open source and commercially usable.

[1]: license
