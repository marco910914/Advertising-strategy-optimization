#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt

# 定義廣告平台及其成本和點擊率
platforms = [
    {"name": "A", "cost": 200, "ctr": 0.05},
    {"name": "B", "cost": 300, "ctr": 0.04},
    {"name": "C", "cost": 150, "ctr": 0.06},
    {"name": "D", "cost": 500, "ctr": 0.03},
    {"name": "E", "cost": 250, "ctr": 0.055}
]

# 預算
budget = 1000

# 計算點擊成本效益
for platform in platforms:
    platform["effectiveness"] = platform["ctr"] / platform["cost"]

# 根據點擊成本效益排序平台
platforms.sort(key=lambda x: x["effectiveness"], reverse=True)

# 貪婪選擇平台
selected_platforms = []
total_cost = 0
total_clicks = 0

for platform in platforms:
    if total_cost + platform["cost"] <= budget:
        selected_platforms.append(platform)
        total_cost += platform["cost"]
        total_clicks += platform["ctr"] * platform["cost"]

# 結果展示
platform_names = [platform["name"] for platform in selected_platforms]
costs = [platform["cost"] for platform in selected_platforms]
clicks = [platform["ctr"] * platform["cost"] for platform in selected_platforms]

# 創建圖表
fig, ax1 = plt.subplots()

# 設置柱狀圖
ax1.bar(platform_names, costs, color='b', alpha=0.6)
ax1.set_xlabel('platform')
ax1.set_ylabel('cost', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# 創建折線圖
ax2 = ax1.twinx()
ax2.plot(platform_names, clicks, color='r', marker='o')
ax2.set_ylabel('click', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# 添加標題
plt.title('platform&effect')

# 顯示圖表
plt.show()


# In[ ]:




