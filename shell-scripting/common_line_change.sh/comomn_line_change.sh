#!/bin/bash

input_file="words.txt"
output_file="output_records.txt"


if [[ ! -f $input_file ]]; then
    echo "Input file '$input_file' not found!"
    exit 1
fi

# Clear the output file if it exists
> "$output_file"


while IFS= read -r word; do
    
    
    line="<option value=\"$word\">$word</option>"
    # Append the sentence to the output file
    echo "$line" >> "$output_file"
done < "$input_file"

echo "Sentences written to $output_file"
