import os
import cv2
import imutils
import numpy as np
import joblib
import pickle
 
pts = []  # 用於存放點
 
 
# 統一的：mouse callback function
def draw_roi(event, x, y, flags, param):
    img2 = img.copy()
 
    if event == cv2.EVENT_LBUTTONDOWN:  # 左鍵點擊，選擇點
        pts.append((x, y))  
 
    if event == cv2.EVENT_RBUTTONDOWN:  # 右鍵點擊，取消最近一次選擇的點
        pts.pop()  
 
    if event == cv2.EVENT_MBUTTONDOWN:  # 中鍵繪製輪廓
        mask = np.zeros(img.shape, np.uint8)
        points = np.array(pts, np.int32)
        points = points.reshape((-1, 1, 2))
        # 畫多邊形
        mask = cv2.polylines(mask, [points], True, (255, 255, 255), 2)
        mask2 = cv2.fillPoly(mask.copy(), [points], (255, 255, 255))  # 用於求 ROI
        mask3 = cv2.fillPoly(mask.copy(), [points], (0, 255, 0))  # 用於 顯示在桌面的圖像
 
        show_image = cv2.addWeighted(src1=img, alpha=0.8, src2=mask3, beta=0.2, gamma=1)
 
        cv2.imshow("mask", mask2)
        cv2.imshow("show_img", show_image)
 
        ROI = cv2.bitwise_and(img,mask2)
        cv2.imshow("ROI", ROI)
        cv2.waitKey(0)
    
    if len(pts) > 0:
        # 將pts中的最後一點畫出來
        cv2.circle(img2, pts[-1], 3, (0, 0, 255), -1)
    
    if len(pts) > 1:
        # 畫線
        for i in range(len(pts) - 1):
            cv2.circle(img2, pts[i], 5, (0, 0, 255), -1)  # x ,y 為滑鼠點擊地方的座標
            cv2.line(img=img2, pt1=pts[i], pt2=pts[i + 1], color=(255, 0, 0), thickness=2)
 
    cv2.imshow('image', img2)
 
 
# 創建圖像與視窗並將視窗與回呼函數綁定
img = cv2.imread("drum_fan.jpg")
img = imutils.resize(img, width=500)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_roi)
cv2.imshow('image',img)
print("[INFO] 按一下左鍵：選擇點，按一下右鍵：刪除上一次選擇的點，按一下中鍵：確定ROI區域")
print("[INFO] 按‘S’確定選擇區域並保存")
print("[INFO] 按 ESC 退出")
 
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:   
        break
    if key == ord("s"):
        saved_data = {
            "ROI": pts
        }
        joblib.dump(value=saved_data, filename="config.pkl")
        print("[INFO] ROI座標已保存到本地.")
        break


cv2.destroyAllWindows()
cv2.waitKey(1)
if os.path.isfile("config.pkl"):
  pth=open('./config.pkl','rb')
  pkl=pickle.load(pth)
  print(pkl)
  print(pts)


