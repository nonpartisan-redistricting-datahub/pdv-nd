# pdv-nd

Our final election results validation report for this dataset is available [here](https://redistrictingdatahub.org/dataset/vest-2018-north-dakota-precinct-and-election-results/).

We do not have the raw data sources available on this Github due to file constraints, but we are happy to share them if needed.

Please reach out to info@redistrictingdatahub.org to reach our support team if you have any questions, or if you would like to request a full validation report.

## Raw from source

### Accessible files:

- File: ND VEST 2020 File
   - Date accessed: 8/12/2021
   - Link: https://dataverse.harvard.edu/file.xhtml?fileId=4931789&version=15.0
   - File: `nd_2020.zip`
- File: VEST Documentation File, 2020
   - Date accessed: 8/12/2021
   - Link: https://dataverse.harvard.edu/file.xhtml?fileId=4938251&version=15.0
   - File: `documentation.txt`
- File: ND Precinct-Level Election Results, 2020
  - Date accessed: 8/13/2021
  - Link: https://results.sos.nd.gov/ResultsSW.aspx?text=All&type=SW&map=CTY
  - Note: Selected 'EXPORT' and downloaded 'Precinct' data for each election
- File: 2020 ND Partnership Shapefile
  - Date accessed: 8/3/2021
  - Link: https://www.census.gov/geo/partnerships/pvs/partnership19v2/st38_nd.html
  - Note: Downloaded up to 5 at a time

## File processing:

`vest-nd-2020-validation.ipynb` is the script that is the basis of the validation report
