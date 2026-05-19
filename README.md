\# CTA200 Mini Coding Project



Code and report for the CTA200 mini coding project. The analysis compares

the same radio source observed at three different frequencies across three surveys: VLASS (3 GHz), FIRST (1.4 GHz), and LoTSS (300 MHz). The target source is at RA = 10h50m07.270s, Dec = +30°40'37.52'' (ICRS), the example coordinates from the `radioquery` README.



\## Files



\- `CTA200\_Mini\_Project.pdf` - the compiled report

\- `report.tex` - LaTeX source for the report

\- `FITS\_images.ipynb` - notebook that produces all figures

\- `download\_radio\_image.py` - wrapper function for downloading FITS files

\- `LOTSS\_J105007.27+304037.52.fits`, `FIRST\_J105007.27+304037.52.fits` -

&#x20; FITS images for the FIRST and LoTSS surveys

\- Figure PDFs referenced in the report (see below)



\## Running the notebook



1\. Place all three FITS files in the same directory as `FITS\_images.ipynb`.

&#x20;  The VLASS file (`J105047+303000\_qle123Imedian.fits`) was emailed

&#x20;  separately because it exceeds GitHub's 100 MB file size limit.

2\. Open `FITS\_images.ipynb` in JupyterLab or Jupyter Notebook.

3\. Run all cells from top to bottom (Kernel → Restart \& Run All).



\## Figures



Running the notebook produces:

\- `vlass\_panel.pdf`, `first\_panel.pdf`, `lotss\_panel.pdf` - zoomed cutouts

&#x20; of the source for each survey.

\- `vlass\_contour.pdf`, `first\_contour.pdf`, `lotss\_contour.pdf` - contour

&#x20; maps overlaid on greyscale images.

\- `lotss\_noise\_diagnostic.pdf` - diagnostic plot showing the noise region

&#x20; selection (referenced in the appendix of the report).



\## Dependencies



\- `astropy`

\- `numpy`

\- `matplotlib`

\- `radioquery` (https://github.com/lazdam/radioquery), installed in a

&#x20; dedicated `conda` environment.

