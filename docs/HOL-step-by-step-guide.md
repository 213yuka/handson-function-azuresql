# 関数アプリの作成と展開

<img src="images/mcw-exercise-1.png" />

### Task 0: Git の準備

後ほど記載する

### Task 1: Azure SQL の作成

- Azure ポータルの検索窓から **Azure SQL** と検索しAzure SQLをクリック

  <img src="images/t1-01.png" />

- [作成]を選択

  <img src="images/t1-02.png" />

- [SQL データベース] で、 [リソースの種類] を [単一データベース] に設定し、 [作成] を選択

  <img src="images/t1-03.png" />

- サブスクリプションを選択し、リソースグループを作成
- ワークロード環境には、この演習の [開発] を指定
- [サーバー] で、 [新規作成] を選択

  <img src="images/t1-04.png" />

- 認証方法は **SQL 認証を使用する** を選択
- ※サーバー名は、サブスクリプション内で一意ではなく、Azure のすべてのサーバーに対してグローバルに一意にする必要がある

  <img src="images/t1-05.png" />

- [ネットワーク] タブの [接続方法] で、 [パブリック エンドポイント] を選択

  <img src="images/t1-06.png" />

- [追加設定] タブにある [データ ソース] セクションの [既存のデータを使用します] で、 [サンプル] を選択
- サンプル データセット AdventureWorksLT から作成

  <img src="images/t1-07.png" />

- [作成]を選択

  <img src="images/t1-08.png" />

- 作成が完了したら[リソースに移動]を選択

  <img src="images/t1-09.png" />

- 左のメニューから[クエリ エディター]を選択してログイン

  <img src="images/t1-10.png" />

- 以下のクエリを実行

```sql
SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName
FROM SalesLT.ProductCategory pc
JOIN SalesLT.Product p
ON pc.productcategoryid = p.productcategoryid;
```

  <img src="images/t1-11.png" />

### Task 2: 関数アプリの作成

- Azure ポータルの検索窓から **関数アプリ** と検索し関数アプリをクリック

  <img src="images/t2-01.png" />

- **関数アプリ** の **作成** をクリック

  <img src="images/t2-02.png" />

- 関数アプリの作成

  <img src="images/t2-03.png" />


<br />

### Task 3: Visual Studio Code からのデプロイ

- **Terminal** - **New Terminal** を選択し、ターミナルを表示

  <img src="images/t3-01.png" />

- az login コマンドを実行

  ```
  az login
  ```

  Web ブラウザーが起動、サインイン画面が表示されるのでサインインを実行

  ※ サインイン後はブラウザを閉じる

- プロジェクト ファイルのディレクトリへ移動

  ```
  func azure functionapp publish <作成した関数アプリ名> --python
  ```

  - デプロイが正常に終了したことを確認

    <img src="images/deploy-function-02.png" />

  <br />

### Task 4: 関数アプリの構成

- Azure ポータルで SQL Database (AdventureWorksLT) の管理ブレードを表示

  - **接続文字列** を選択し **ODBC (Node.js を含む) (SQL 認証)** の接続文字列をコピーし、メモ帳などのテキスト エディターに貼り付け

    <img src="images/sql-connection-string-python.png" />

  - **{your_password}** を SQL Database への認証で使用するアカウントのパスワードに変更

  - **接続文字列の冒頭 Driver={ODBC Driver 18 for SQL Server} を Driver={ODBC Driver 17 for SQL Server} に変更してください。**

            ※ 後の手順で使用するためコピー

- Azure Functions の管理ブレードへ移動

- **構成** メニューを選択、**＋ 新しいアプリケーション設定** をクリック

  <img src="images/function-configuration-01.png" />

- アプリケーション設定の追加/編集画面で、追加する構成の名前、値を入力し **OK** をクリック

  - **名前**: SqlConnectionString

  - **値**: SQL Database への接続文字列

    - **注意** : Python の場合、接続文字列の冒頭 **Driver={ODBC Driver 18 for SQL Server}** を **Driver={ODBC Driver 17 for SQL Server}** に変更してください。

    <img src="images/function-configuration-02.png" />

- **保存** をクリック

  <img src="images/function-configuration-03.png" />

- **変更の保存** の確認メッセージが表示されるので **続行** をクリック

<br />

### Task 5: 関数アプリの実行

- Web ブラウザーを起動、アドレス バーに関数アプリの展開時に出力された URL を貼り付け

- ?id=xx (xx は数字、5, 7, 10, 22, 27, 35 の間で指定) を付与して実行

  <img src="images/function-result-01.png" />

  ※ データベースから取得したレコードを表示

<br />

