import os
import numpy as np
import nibabel as nib

def convert_nii_to_npz(nii_file, save_folder):
    # 读取 NIfTI 文件
    nii_data = nib.load(nii_file).get_fdata()

    # 为了保存空间，将数据转换为 float32 类型
    nii_data = np.array(nii_data, dtype=np.float32)

    # 构造保存的文件路径和文件名
    save_filename = os.path.splitext(os.path.basename(nii_file))[0] + ".npz"
    save_path = os.path.join(save_folder, save_filename)

    # 保存数据为 .npz 文件
    np.savez_compressed(save_path, data=nii_data)

def convert_folder_nii_to_npz(folder_path, save_folder):
    # 确保保存文件夹存在
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".nii") or filename.endswith(".nii.gz"):  # 检查文件扩展名
            nii_file = os.path.join(folder_path, filename)
            # 使用转换函数将NIfTI文件转换为NumPy格式并保存为npz文件
            convert_nii_to_npz(nii_file, save_folder)
            print(filename + "convert success!")
    print("success!")
if __name__ == "__main__":
    folder_path = r"E:\桌面\transu\gz_folder"  # 替换为你的文件夹路径
    save_folder = r"E:\桌面\data_for_nnunet\seg"   # 替换为你想保存的文件夹路径

    convert_folder_nii_to_npz(folder_path, save_folder)
