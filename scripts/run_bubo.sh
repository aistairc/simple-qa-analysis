DATA=../datasets/SQ
TARGET=SQ

cd ../BuboQA
. bubo/bin/activate

cd entity_detection/nn
python train.py --entity_detection_mode LSTM --fix_embed --data_dir ../../$DATA --save_path ./$TARGET
python top_retrieval.py --trained_model ./$TARGET/lstm/id1_best_model.pt --entity_detection_mode LSTM --results_path ./$TARGET --data_dir ../../$DATA

cd ../../entity_linking
python entity_linking.py --model_type lstm --query_dir ../entity_detection/nn/$TARGET/lstm --data_dir ../$DATA --output_dir ./$TARGET

cd ../relation_prediction/nn
python train.py --fix_embed --relation_prediction_mode CNN --data_dir ../../$DATA --save_path ./$TARGET
python top_retrieval.py --relation_prediction_mode CNN --trained_model ./$TARGET/cnn/id1_best_model.pt --data_dir ../../$DATA --hits 5 --results_path ./$TARGET

cd ../../evidence_integration
python evidence_integration.py --ent_type lstm --ent_path ../entity_linking/$TARGET/lstm/test-h100.txt --rel_type cnn --rel_path ../relation_prediction/nn/$TARGET/cnn/test.txt --data_path ../$DATA/test.txt --output_dir ./$TARGET

deactivate
cd ../scripts


