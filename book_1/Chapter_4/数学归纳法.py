def sum_formula(n):
    """计算 1 + 2 + ... + n 的和，并返回公式 n*(n+1)/2 的结果"""
    actual_sum =sum(range(1,n+1))
    formula_sum = n * (n+1)/2
    return actual_sum, formula_sum

def mathmatical_induction_proof(max_n):
    """模拟数学归纳法证明 1 + 2 + ... + n = n*(n+1)/2"""
    print("=== 数学归纳法证明：1 + 2 + ... + n = n(n+1)/2 ===")

    # 步骤 1：验证基本情况 (n=1)
    print("\n步骤 1：验证基本情况 (n=1)")
    actual, formula = sum_formula(1)
    if actual == formula:
        print(f"n=1 时，实际和={actual}，公式结果={formula}，基本情况成立！")
    else:
        print(f"基本情况不成立，证明失败！")
        return

    # 步骤 2：归纳假设和归纳步骤
    print("\n步骤 2：归纳假设与归纳步骤")
    print("假设对 n=k 成立，即 1 + 2 + ... + k = k(k+1)/2")
    print("验证 n=k+1 时是否成立：1 + 2 + ... + k + (k+1) = (k+1)(k+2)/2")
# 使用循环验证前 max_n 项，模拟归纳步骤
    for k in range(1, max_n):
        print(f"\n验证 n={k+1}：")
        actual, formula = sum_formula(k + 1)
        if actual == formula:
            print(f"实际和={actual}，公式结果={formula}，n={k+1} 成立！")
        else:
            print(f"n={k+1} 不成立，证明失败！")
            return

    print(f"\n结论：通过基本情况和归纳步骤验证，命题对所有正整数 n 成立（验证至 n={max_n}）。")

# 测试代码
max_n = 10  # 验证前 5 项
mathmatical_induction_proof(max_n)