# 주어진 유병률과 양성이 나올 확률을 통해, 양성이 나왔을 때 실제 질병이 있을 확률을 구하는 함수

def baeys_prob(prevalence_rate, abnormal_test_positive, normal_test_positive):
    # 질병이 있고 양성이 나올 확률 (민감도)
    abnormal_positive_ratio = abnormal_test_positive
    
    # 질병이 없고 양성이 나올 확률 (위양성률)
    normal_positive_ratio = normal_test_positive
    # 질병이 있고 음성이 나올 확률 
    abnormal_negative_ratio =  (1 - abnormal_test_positive) * prevalence_rate
    # 양성이 나올 전체 비율
    positive_ratio = (abnormal_positive_ratio * prevalence_rate) + (normal_positive_ratio * (1 - prevalence_rate))
    # 양성이 나왔을 때 실제로 질병이 있을 확률 (베이즈 정리)
    positive_abnormal_ratio = (abnormal_positive_ratio * prevalence_rate) / positive_ratio
    
    # 결과 출력
    print(f"유병률: {100*prevalence_rate:.1f}%")
    print(f"질병이 있을 때 양성이 나올 확률(민감도): {100*abnormal_test_positive:.1f}%")
    print(f"질병이 없을 때 양성이 나올 확률(위양성률): {100*normal_test_positive:.1f}%")
    print(f"양성이 나왔을 때 실제 질병이 있을 확률: {100*positive_abnormal_ratio:.2f}%")
    print(f"질병이 있는데 음성이 나올 확률(1-민감도): {100*abnormal_negative_ratio:.2f}%")

# 예시 실행
baeys_prob(0.7, 0.99, 0.01)

baeys_prob(0.005, 0.98, 0.02)

baeys_prob(0.02, 0.99, 0.01)
