# pdv-nd

Our final election results validation report for this dataset is available [here](https://redistrictingdatahub.org/dataset/vest-2016-north-dakota-precinct-and-election-results/).

We do not have the raw data sources available on this Github due to file constraints, but we are happy to share them if needed. 

Please reach out to info@redistrictingdatahub.org to reach our support team if you have any questions, or if you would like to request a full validation report. 

## Raw from source

### Accessible files:

- File: ND VEST 2016 File
   - Date accessed: 7/28/2021
   - Link: https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/NH5S2I/JM0M6V&version=61.0
   - File: `nd_2016.zip`
- File: VEST Documentation File, 2016
   - Date accessed: 7/28/2021
   - Link: https://dataverse.harvard.edu/file.xhtml?fileId=4863153&version=61.0
   - File: `documentation.txt`
- File: ND Precinct-Level Election Results, 2016
  - Date accessed: 7/28/2021
  - Link: https://results.sos.nd.gov/ResultsSW.aspx?text=All&type=SW&map=CTY&eid=292
  - Note: Selected 'EXPORT' and downloaded both 'Precinct' and 'County' for each election
- File: ND Voter Precinct Shapefile, 2016
  - Date accessed: 8/3/2021
  - Link: https://www.census.gov/geo/partnerships/pvs/partnership16v1/st38_nd.html
  - Note: Downloaded up to 5 at a time

## File processing:

`vest-nd-2016-validation.ipynb` is the script that is the basis of the validation report
