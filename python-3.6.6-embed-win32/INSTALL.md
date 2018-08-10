# embeddable python

このフォルダに下記の手順で作成したembeddable pythonをコピーしてください。

1. embeddable pythonのダウンロード
  * https://www.python.org/downloads/windows/ から Windows x86 embeddable zip file をダウンロードし、解凍します。UiPathのPython Activityが認識するバージョンを選択してください。
  テストはPython 3.6.6で行いました。


2. pipの導入
  * pythonNN._pthファイルのの"import site"をuncommentします。
  * https://bootstrap.pypa.io/get-pip.py からget-pip.pyをダウンロードします。
  * python get-pip.py　を実行します。

  
3. OpenCVを導入
  * python -m pip install opencv_python を実行します。

