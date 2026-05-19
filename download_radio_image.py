# Making a function to get FITS files

# Imports at the top
import os
from astropy.coordinates import SkyCoord
from radioquery.survey_configs.vlass import VlassQuery
from radioquery.survey_configs.first import FirstQuery
from radioquery.survey_configs.lotss import LotssQuery


def download_radio_image(ra, dec, survey):
    """
    Downloads a FITS file from a radio survey for a given RA/Dec coordinate.
    
    Parameters
    ----------
    ra : str
        Right Ascension [deg] e.g. '10h50m07.270s'
    dec : str
        Declination [deg] e.g. '30d40m37.52s'
    survey : str
        Survey name: 'VLASS', 'FIRST', or 'LOTSS'
    
    Returns
    -------
    file_path : str
        Path to the downloaded FITS file
    success : bool
        True if download was successful
    """
    
    # define the coordinate
    coord = SkyCoord(ra=ra, dec=dec, frame='icrs')
    
    # define download paths
    download_paths = {
        'VLASS': os.path.expanduser('~/RQUERY/VLASS'),
        'FIRST': os.path.expanduser('~/RQUERY/FIRST'),
        'LOTSS': os.path.expanduser('~/RQUERY/LOTSS'),
    }
    
    # check the survey name is valid
    survey = survey.upper()
    if survey not in download_paths:
        raise ValueError(f"Survey '{survey}' not recognised. Choose from: VLASS, FIRST, LOTSS")
    
    download_path = download_paths[survey]
    
    # download based on survey
    if survey == 'VLASS':
        query = VlassQuery(coord=coord, download_path=download_path, overwrite=False)
    elif survey == 'FIRST':
        query = FirstQuery(coord=coord, download_path=download_path, size_arcmin=5)
    elif survey == 'LOTSS':
        query = LotssQuery(coord=coord, download_path=download_path, size_arcmin=5)
    
    file_path, success = query.download_image()
    
    if success:
        print(f"GOOD {survey} downloaded: {file_path}")
    else:
        print(f"BAD {survey} download failed for RA={ra}, Dec={dec}")
    
    return file_path, success


# This block runs when you execute the script from the terminal (test to see if function works)
if __name__ == "__main__":
    ra = '10h50m07.270s'
    dec = '30d40m37.52s'
    
    for survey in ['VLASS', 'FIRST', 'LOTSS']:
        print(f"\n--- Downloading {survey} ---")
        download_radio_image(ra, dec, survey)
    
    print("\nDone!")