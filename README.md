# SRF Line Counter

Every year we have to report on the number of samples collected across all projects. Each project uses an Excel spreadsheet to track this where each row records a unique sample. This app uses pandas to open an Excel file, removes duplicates (because some rows have formulas so "empty rows" are not actually empty but are also not unique), and adds that to a running tally. It does this for every Excel file in a folder, with a user specified number of header rows being ignored.
