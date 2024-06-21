# 定義廣告平台及其成本和點擊率下降規則
platforms = [
    {"name": "A", "base_cost": 200, "ctr": 0.05, "decline": (100, 0.02)},
    {"name": "B", "base_cost": 300, "ctr": 0.04, "decline": (50, 0.02)},
    {"name": "C", "base_cost": 150, "ctr": 0.045, "decline": (100, 0.03)},
    {"name": "D", "base_cost": 500, "ctr": 0.015, "decline": (float('inf'), 0.0)},  # 無下降
    {"name": "E", "base_cost": 250, "ctr": 0.055, "decline": (100, 0.05)}
]

# 預算
budget = 1400

def calculate_effectiveness(platform, investment):
    # 計算給定投資下的實際CTR
    base_ctr = platform["ctr"]
    decline_interval, decline_rate = platform["decline"]
    
    if investment <= decline_interval:
        return base_ctr
    
    # 計算下降後的CTR
    intervals = investment // decline_interval
    declined_ctr = base_ctr * ((1 - decline_rate) ** intervals)
    return declined_ctr

# 貪婪選擇平台
selected_platforms = []
total_cost = 0
total_clicks = 0

while total_cost < budget:
    best_platform = None
    best_effectiveness = 0
    best_additional_cost = 0
    best_additional_clicks = 0
    
    for platform in platforms:
        investment = platform["base_cost"]
        if total_cost + investment <= budget:
            current_ctr = calculate_effectiveness(platform, investment)
            effectiveness = current_ctr / investment
            if effectiveness > best_effectiveness:
                best_effectiveness = effectiveness
                best_platform = platform
                best_additional_cost = investment
                best_additional_clicks = current_ctr * investment
    
    if best_platform is None:
        break
    
    selected_platforms.append(best_platform)
    total_cost += best_additional_cost
    total_clicks += best_additional_clicks
    platforms.remove(best_platform)

# 結果
print("選擇的廣告平台:")
for platform in selected_platforms:
    print(f"平台 {platform['name']}, 成本: {platform['base_cost']}, 點擊率: {platform['ctr']}, 點擊數: {platform['ctr'] * platform['base_cost']:.2f}")

print(f"總成本: {total_cost}, 總點擊數: {total_clicks:.2f}")
