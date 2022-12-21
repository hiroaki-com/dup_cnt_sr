### 概要
仕事で大量レコードのCSVファイル内の特定カラムの重複度を確認する必要があり、記述した簡易的なPythonスクリプト
出力先はは新しいCSVファイルとしています

### 準備

分析対象の`file.csv`を用意<br>
"index=['']" へ集計対象としたいカラム名を入力

### 備考
初期の仮想環境構築<br>
`python3 -m venv env`

一括でパッケージをインストール<br>
`pip install -r requirements.txt`
 
 "duplicates.py"を実行<br>
`python3 duplicates.py`
