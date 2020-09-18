# 9.18平安科技
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 学习训练数据，并计算测试数据中个样本属于0类的概率。
# @param train_input int整型二维数组 训练数据的输入，即各样本的特征数据。注意，特征在各个维度上的取值都是二值化的。
# @param train_label int整型一维数组 训练数据的输出，即类标签
# @param test_input int整型二维数组 测试数据的输入，即各测试样本的特征数据。
# @return float浮点型一维数组
#
class Solution:
    def fit_transform(self , train_input , train_label , test_input ):
        # write code here
        len_train = len(train_input)
        len_feature = len(train_input[0])
        a_count = train_label.count(0)
        pa = a_count / len_train

        a_train_index = []
        for i in range(len(train_label)):
            if train_label[i] == 0:
                a_train_index.append(i)

        a_train_data = []
        for i in a_train_index:
            a_train_data.append(train_input[i])

        fenmu = 1.0
        fenzi = 1.0
        res = []

        def transpose(matrix):
            new_matrix = []
            for i in range(len(matrix[0])):
                matrix1 = []
                for j in range(len(matrix)):
                    matrix1.append(matrix[j][i])
                new_matrix.append(matrix1)
            return new_matrix

        train_input_t = transpose(train_input)
        a_train_data_t = transpose(a_train_data)

        for i in test_input:
            for j in range(len_feature):
                fenmu *= train_input_t[j].count(test_input[i][j]) / len_train
                fenzi *= a_train_data_t[j].count(test_input[i][j]) / len(a_train_data)
            res.append(fenzi * pa / fenmu)
        return res