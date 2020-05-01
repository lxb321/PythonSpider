"""
@file:titanic.py
@time:2020/1/16-16:52
@info:Titanic 存活预测
"""
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def decision():
    """
    决策树对泰坦尼克号进行预测生死
    :return: None
    """
    # titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    titan = pd.read_csv("titanic.txt")
    # 处理数据,找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]
    y = titan['survived']
    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)
    print(x)
    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # 进行处理(特征工程) 特征-> 类别 -> one_hot编码
    dict = DictVectorizer(sparse=False)

    # orient='records' 形成[{column -> value}, … , {column -> value}]的结构
    # 参数 ‘dict’, ‘list’, ‘series’, ‘split’, ‘records’, ‘index’
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))
    x_test = dict.fit_transform(x_test.to_dict(orient="records"))

    print(dict.get_feature_names())
    # print(x_train)
    # 用决策树进行预测
    dec = DecisionTreeClassifier(max_depth=5)

    dec.fit(x_train, y_train)

    # 预测准确率
    print(f"预测准确率：{dec.score(x_test, y_test)}")

    # 导出决策树的结构
    export_graphviz(dec, out_file="./tree.dot",
                    feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性']
                    )

    return None


if __name__ == '__main__':
    decision()
