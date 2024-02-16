# add number of words and pages
conda activate

# date
line=$(date +"%Y-%m-%d")
line+=" "

# countwords in thesis
echo word count
wordCount=$(ps2ascii thesis.pdf | wc -w)
line+=$(grep -Eo '[0-9]+' <<<"$wordCount")

echo page count
pageCount=$(mdls -name kMDItemNumberOfPages thesis.pdf)
line+=" "
line+=$(grep -Eo '[0-9]*' <<<"$pageCount")

echo $(grep -Eo '[0-9]*' <<<"$pageCount")

echo $line

# append to file
echo $line >> date_wordCount_pageCount.txt

python progressCount.py
python progressCountCombined.py

conda deactivate

