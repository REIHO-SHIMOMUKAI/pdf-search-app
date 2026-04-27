# PDF Search App

## 説明 / introduction

PDFをアップロードし、内容を文字列検索できるWebアプリ

A web application that allows you to upload PDF and search their contents by text

## アプリの使い方 / How to use of app

PDF Upload、PDF Search、PDF Listの3つの項目があります。

1. PDF Upload
   - PDFをUploadすると、PDF Listに追加されます。 / When you upload a PDF, it will be added to the PDF List.

2. PDF Search
   - PDF Searchの検索ボックスに検索したい文字を入れてSearchボタンを押すと、該当するPDFのみがPDF Listに表示されます。 / Enter the text you want to search for in the search box and press the Search button. Only the matching PDFs will be displayed in the PDF List.
   - 各PDFをOpenボタンで開くと、検索した文字がハイライトされた状態で全テキストが表示されます。 /  When you open each PDF using the Open button, the entire text will be displayed with the searched text highlighted.

3. PDF List
   - アップロードされたPDFの一覧を表示します。 / Displays a list of uploaded PDFs.
   - Openボタン：PDF内の全テキストが表示されます。 / Open button: Displays all text within the PDF.
   - Deleteボタン：PDFをListから削除できます。 / Delete button: Removes the PDF from the list.

## 技術スタック / Tech Stack
- Python (Flask)
- SQLite
- pdfplumber


## 実行方法 / How to run
1. ターミナルで以下を実行 / Execute the following command on Terminal
```
python app.py
```
2. ブラウザを開き、以下にアクセスする / Open browser and access below URL
```
http://localhost:5000/
```

## データベースの確認方法 / How to check the database
ターミナルで以下を実行 / Execute the following command on Terminal
```
python db_show.py
```
