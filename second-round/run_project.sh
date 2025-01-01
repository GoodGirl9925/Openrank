#python get_opendigger_data.py
#echo "Run get_opendigger_data.py successfully."
cd data_preprocessor
echo "Changed directory to data_preprocessor."
python adjust_opendigger_data.py
echo "Run adjust_opendigger_data.py successfully."
python filter_adjusted_data.py
echo "Run filter_adjusted_data.py successfully."
python normalize_filtered_data.py
echo "Run normalize_filtered_data.py successfully."
cd ../trustworthy_model
echo "Changed directory to trustworthy_model."
python calc_trustworthy.py
echo "Run calc_trustworthy.py successfully."
python filter_trustworthy.py
echo "Run filter_trustworthy.py successfully."
cd ../visualization
echo "Changed directory to visualization."
python averageOverallTrustworthy_projects.py
echo "Run averageOverallTrustworthy_projects.py successfully."
python overallTrustworthy_time_projects.py
echo "Run overallTrustworthy_time_projects.py successfully."
python trustworthy_time_overallAndAttr.py
echo "Run trustworthy_time_overallAndAttr.py successfully."
echo "Finished tasks. Exited."