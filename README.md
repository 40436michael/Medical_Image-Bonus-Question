# 醫療影像 bonus
https://docs.google.com/presentation/d/19sbsD_2t7-B8Zd-f4vRYfYB1mkfcQC35uxHKW17tPko/edit?usp=sharing

## 專案介紹

本專案使用 **Python + OpenCV** 實作六種常見的邊緣偵測方法，並比較其在：

* 自然影像（Natural Image）
* 醫學影像（Medical Image）

上的效果差異。

透過不同演算法的結果分析，可了解各方法的優缺點與適用場景。

---

# 使用的邊緣偵測方法

本專案共實作以下六種方法：

1. Canny
2. Sobel
3. Laplacian
4. LoG（Laplacian of Gaussian）
5. Prewitt
6. Roberts

---

# 測試影像

## 自然影像

使用聖母峰北壁影像：

Everest North Face toward Base Camp Tibet

## 醫學影像

使用腦部 MRI 影像。

---

# 專案結構

```bash
project/
│── image/
│   ├── natural.jpg
│   └── medical.jpg
│
│── output/
│   ├── 自然影像_總比較圖.png
│   ├── 醫學影像_總比較圖.png
│   └── 各方法輸出圖片
│
│── edge_detection.py
│── README.md
```

---

# 安裝套件

請先安裝 Python 套件：

```bash
pip install opencv-python numpy matplotlib
```

---

# 執行方式

```bash
python edge_detection.py
```

執行後將會：

* 顯示六種邊緣偵測結果
* 自動儲存圖片至 `output/`

---

# 輸出結果

每張影像會輸出：

* 原圖
* Canny
* Sobel
* Laplacian
* LoG
* Prewitt
* Roberts
* 總比較圖

---

# 方法比較

| 排名 | 方法        | 特性          |
| -- | --------- | ----------- |
| 1  | Canny     | 邊緣最清楚、抗雜訊最佳 |
| 2  | Sobel     | 快速穩定        |
| 3  | LoG       | 細節佳、較平滑     |
| 4  | Laplacian | 細節多但雜訊高     |
| 5  | Prewitt   | 簡單快速        |
| 6  | Roberts   | 最快但較不穩定     |

---

# 分析結果

## 自然影像（聖母峰）

* Canny 可清楚抓出山脈輪廓與冰雪紋理
* Sobel 適合快速偵測輪廓
* LoG 可保留較多地形細節

## 醫學影像（MRI）

* Canny 最適合腦部邊界偵測
* LoG 可保留組織細節
* Sobel 可抓主要輪廓

---

# 最佳方法推薦

## 整體最佳：

```text
Canny Edge Detection
```

## 快速處理：

```text
Sobel / Prewitt
```

## 醫學影像：

```text
Canny / LoG
```

---

# 使用技術

* Python
* OpenCV
* NumPy
* Matplotlib



### 圖諞來源
https://upload.wikimedia.org/wikipedia/commons/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg
https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/BrainAtrophy%28exvacuo%29.png/330px-BrainAtrophy%28exvacuo%29.png
