import shutil

src_path = r"E:\demos\files\report\profit.txt"
dst_path = r"E:\demos\files\account\profit.txt"
shutil.copy(src_path, dst_path)
print('Copied')
