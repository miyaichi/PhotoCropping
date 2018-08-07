# PhotoCropping

## 顔認識による証明写真の切り抜き

写真から認識した顔の高さ（髪の毛の上から顎まで）をもとに、写真を切り抜きます。
切り抜くエリアは、顔の高さが写真の高さの60%、顔の上に10%の空きとなるよう調整します。ただし、利用している顔認識システム（OpenCV）では、髪の毛を含めた顔を認識する識別器がないので、調整が必要そうです。

<img src='./photo.png'>
