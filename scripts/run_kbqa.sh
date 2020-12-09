DATA=../datasets/SQ
TARGET=SQ

cd ../BuboQA
. bubo/bin/activate

cd entity_detection/nn
python train.py --entity_detection_mode LSTM --fix_embed --data_dir ../../$DATA --save_path ./$TARGET
python top_retrieval.py --trained_model ./$TARGET/lstm/id1_best_model.pt --entity_detection_mode LSTM --results_path ./$TARGET --data_dir ../../$DATA

cd ../../entity_linking
python entity_linking.py --model_type lstm --query_dir ../entity_detection/nn/$TARGET/lstm --data_dir ../$DATA --output_dir ./$TARGET

deactivate

cd ../../KBQA-Adapter
. kbqa/bin/activate
python prepare_input.py --dataset $TARGET

cd qa+adapter

python applyingbuboentity.py $TARGET
python yml.py $TARGET
python -u start.py --run train --config ./hr-bubo/$TARGET'.yml' --star_model --fold 0
python -u start.py --run train --config ./ad-bubo/$TARGET'.yml' --star_model --fold 0

cd ../model
python bubo_convert.py rerank

cd ../qa+adapter
python applyingrerank.py hr $TARGET
python -u start.py --run train --config ./hr-bubo/$TARGET'.yml' --star_model --fold 0
python applyingrerank.py ad $TARGET
python -u start.py --run train --config ./ad-bubo/$TARGET'.yml' --star_model --fold 0

cd ../model
python bubo_convert.py convert

deactivate
cd ../../BuboQA/evidence_integration
. ../bubo/bin/activate

python evidence_integration.py --ent_type lstm --ent_path ../entity_linking/$TARGET/lstm/test-h100.txt --rel_type cnn --rel_path ../../KBQA-Adapter/model/bubo_format/$TARGET-0.txt --data_path ../$DATA/test.txt --output_dir ./HR-BiLSTM/$TARGET
python evidence_integration.py --ent_type lstm --ent_path ../entity_linking/$TARGET/lstm/test-h100.txt --rel_type cnn --rel_path ../../KBQA-Adapter/model/bubo_format/gan.all-$TARGET-0.txt --data_path ../$DATA/test.txt --output_dir ./KBQA-Adapter/$TARGET
deactivate

cd ../scripts
