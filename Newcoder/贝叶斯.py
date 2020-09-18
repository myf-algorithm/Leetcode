# 9.18ƽ���Ƽ�
# �����е����������������������Ѿ�ָ���������޸ģ�ֱ�ӷ��ط����涨��ֵ����
# ѧϰѵ�����ݣ���������������и���������0��ĸ��ʡ�
# @param train_input int���Ͷ�ά���� ѵ�����ݵ����룬�����������������ݡ�ע�⣬�����ڸ���ά���ϵ�ȡֵ���Ƕ�ֵ���ġ�
# @param train_label int����һά���� ѵ�����ݵ�����������ǩ
# @param test_input int���Ͷ�ά���� �������ݵ����룬���������������������ݡ�
# @return float������һά����
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