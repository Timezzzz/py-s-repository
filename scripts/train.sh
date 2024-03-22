
export nnUNet_N_proc_DA=36
export nnUNet_codebase="/opt/anaconda3/envs/3dtransunet/lib/python3.9/site-packages"  # replace to your codebase
export nnUNet_raw_data_base="/home/dell/user/PY/data_for_nnunet/nii/" # replace to your database
export nnUNet_preprocessed="/home/dell/user/PY/data_for_nnunet/preprocessed/"
export RESULTS_FOLDER="/home/dell/user/PY/data_for_nnunet/result/"


CONFIG=$1

echo $CONFIG

### unit test
fold=0
echo "run on fold: ${fold}"
nnunet_use_progress_bar=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
        python3 -m torch.distributed.launch --master_port=4322 --nproc_per_node=8 \
        ./train.py --fold=${fold} --config=$CONFIG --resume=''