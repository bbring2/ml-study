import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# 붓꽃 데이터셋 로딩
iris = load_iris()

# iris.data는 Iris 데이터 세트에서 피처만으로 된 데이터를 numpy로 갖고 있다
iris_data = iris.data

# iris.target은 붗꽃 데이터 세트에서 레이블(결정값) 데이터를 numpy로 갖고 있다
iris_label = iris.target

print('iris target amount: ', iris_label)
print('iris target name: ', iris.target_names)

# 붓꽃 데이터 세트를 자세히 보기 위해 data frame으로 변환
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label'] = iris.target
iris_df.head(3)

# 학습용 데이터와 테스트용 데이터 분리
# test size = 0.2 -> 테스트 데이터 20%, 학습 데이터 80%
# train_test_split의 파라미터
# 첫번째 파라미터 : iris_data는 피처 데이터 세트
# 두번째 파라미터 : iris_label은 레이블 데이터 세트
# 세번째 파라미터 : 전체 데이터 세트 중 테스트 데이터 세트 비율
# 네번째 파라미터 : 호출할 때 마다 같은 학습 및 테스트용 데이터 세트를 생성하기 위해 주어지는 난수 발생값
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.2, random_state=11)

# X train -> 학습용, X_test -> 테스트용, y_train -> 학습용 레이블 데이터 세트, y_test -> 테스트용 레이블 데이터 세트

# TODO : 데이터를 기반으로 머신러닝 분류 알고리즘의 하나인 의사 결정 트리를 이용해 학습과 예측을 수행하기
dt_clf = DecisionTreeClassifier(random_state=11)

# 학습
dt_clf.fit(X_train, y_train)

# 학습이 완료된 decistionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행
pred = dt_clf.predict(X_test)

# 정확도 측정 (예측 결과가 실제 레이블 값과 얼마나 정확하게 맞는지 평가하는 지표)
print('예측 정확도 : , {0:.4f}'.format(accuracy_score(y_test, pred)))
