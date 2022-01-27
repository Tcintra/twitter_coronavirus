for file in ./*.zip; do
    nohup ./src/map.py --input_path=$file --output_folder=test_outputs &
done >> stdout
