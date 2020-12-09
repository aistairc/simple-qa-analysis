
EMB_DIR="./preprocess"
MAP_DIR="./preprocess"
EMB_DIM=250

TARGET=SQ

cd ../KEQA_WSDM19
. keqa/bin/activate

DATADIR="../datasets/"$TARGET
OUTDIR=$TARGET
mkdir -p $TARGET

echo "RUNNING: trim_names"
time python trim_names.py -f data/freebase-FB2M.txt -n data/FB5M.name.txt -d $DATADIR -o $OUTDIR

echo "RUNNING: augment_process_dataset"
time python augment_process_dataset.py -d $DATADIR -o $OUTDIR

echo "RUNNING: train_detection"
time python train_detection.py --entity_detection_mode LSTM --fix_embed --output $OUTDIR

echo "RUNNING: train_entity"
time python train_entity.py --qa_mode GRU --fix_embed --map2id_dir $MAP_DIR --entity_emb $EMB_DIR"/entities_emb.bin" --embed_dim $EMB_DIM --output $OUTDIR

echo "RUNNING: train_pred"
time python train_pred.py --qa_mode GRU --fix_embed --map2id_dir $MAP_DIR --pred_emb $EMB_DIR"/predicates_emb.bin" --embed_dim $EMB_DIM --output $OUTDIR

echo "RUNNING: test_main"
time python test_main.py --map2id_dir $MAP_DIR --entity_emb $EMB_DIR"/entities_emb.bin" --pred_emb $EMB_DIR"/predicates_emb.bin" --embed_dim $EMB_DIM --output $OUTDIR

cd ../scripts
