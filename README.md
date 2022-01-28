# Coronavirus twitter analysis

This repository is my solution to cmc143 homework01, forked from https://github.com/mikeizbicki/cmc-csci143/tree/2022spring/hw_twitter. This project aimed to leverage a MapReduce procedure to analyze the occurrence of particular hashtags in a partitioned Twitter dataset. 

We have a partitioned dataset of `zip` files containing geotagged tweets from particular dates, eg. `geoTwitter20-02-16.zip` corresponding to tweets from the 16th of February of 2020. This repository uses `map.py` to count the occurrence of particular hashtags by language and country in a given day. The output of these counters is contained in the `outputs` directory. Notice that in `src` we run the `map.py` script on the `.zip` files using the `run_maps.sh` bash program. The `.lang` and `.country` files are reduced into one `reduced.lang` and one `reduce.country` file by running the following commands from root:

```
$ ./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.lang
$ ./src/reduce.py --input_paths outputs/geoTwitter*.country --output_path=reduced.country
```

Finally, we run the `visualize.py` script on these reduced files to save the counts of each hashtag by country and language in more human-friendly files in the `viz` directory. The script to run these commands is `src/run_visualize.sh`.
