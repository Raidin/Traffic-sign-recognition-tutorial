import os
import pandas as pd
import shutil

def csv_reader(filename):
    table = pd.read_csv(filename, delimiter=';')
    # print table.columns
    return table

label_dir = os.path.join(os.getcwd(), 'label')
if not os.path.exists(label_dir):
    os.makedirs(label_dir)

data_root = os.path.join(os.environ['HOME'],'data/GTSRB')
train_root = os.path.join(data_root, 'Final_Training/Images')
test_root = os.path.join(data_root, 'Final_Test/Images')

# Training Data List
print 'Create Training Data Label...'
train_label = os.path.join(train_root, 'train_label.txt')
if os.path.isfile(train_label):
    os.remove(train_label)

train_data_class_lists = sorted(os.listdir(train_root))

for idx, train_class in enumerate(train_data_class_lists):
    train_class_dir = os.path.join(train_root, train_class)
    file_lists = sorted(os.listdir(train_class_dir))
    for img_file in file_lists:
        if os.path.splitext(img_file)[1] == '.ppm':
            with open(train_label, 'a' ) as f:
                    content = '/{}/{} {}'.format(train_class, img_file, idx)
                    f.write('{}\n'.format(content))
shutil.copy(train_label, label_dir)


# Test Data List
print 'Create Test Data Label...'
test_label = os.path.join(test_root, 'test_label.txt')
class_table = csv_reader(os.path.join(data_root, 'GT-final_test.csv'))

if os.path.isfile(test_label):
    os.remove(test_label)

test_data_lists = sorted(os.listdir(test_root))

for idx, test_list in enumerate(test_data_lists):
    if os.path.splitext(test_list)[1] == '.ppm':
        with open(test_label, 'a' ) as f:
            content = '{} {}'.format(test_list, class_table['ClassId'][idx])
            f.write('/{}\n'.format(content))
shutil.copy(test_label, label_dir)
print 'Completed Creating Data Label...'