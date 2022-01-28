for file in /data/tweets_corona/*.zip; do
    nohup ./src/map.py --input_path=$file --output_folder=outputs &
done >nohup.out 2>nohup.err
