# 関数アプリの作成と展開

<img src="images/mcw-exercise-1.png" />

### Task 1: 関数アプリの作成

- Azure ポータルのトップ画面から **＋ リソースの作成** をクリック

  <img src="images/add-resources.png" />

- **関数アプリ** の **作成** をクリック

  <img src="images/create-azure-functions-01.png" />

- 関数アプリの作成

  <details>
    <summary>C#</summary>
    
    - **基本**

      - **プロジェクトの詳細**

        - **サブスクリプション**: 使用するサブスクリプション

        - **リソース グループ**: 使用するリソース グループ(任意) 

      - **インスタンスの詳細**

        - **関数アプリ名**: 任意の名前 (2 ～ 60 文字、英数字、およびハイフンのみ)

        - **コードまたはコンテナー**: コード

        - **ランタイム スタック**: 

        - **バージョン**: 

        - **地域**: リソース グループと同じ地域を選択

      - **オペレーティング システム**

        - **オペレーティング システム**: 

      - **ホスティング**

        - **ホスティング オプションとプラン**: 

        - **Windows プラン**: 任意 (既定の名前を変更する場合は新規作成をクリックして入力)

        - **価格プラン**: エラスティック Premium EP1 (ACU 合計 210, 3.5 GB メモリ, 1 vCPU)

      - **ゾーン冗長**

        - **ゾーン冗長**: 無効

        <img src="images/create-azure-functions-02.png" />

  - **Storage**

    - **ストレージ アカウント**: (新規)xxx (名前を変更する場合は新規作成をクリックして入力、英子文字、数字で 3 ～ 24 文字)

      <img src="images/create-azure-functions-03.png" />

  - **ネットワーク**

    - **パブリック アクセスを有効にする**: オン

    - **ネットワーク インジェクションを有効にする**: オフ

      <img src="images/create-azure-functions-04.png" />

  - **監視**

    - **Application Insights を有効にする**: いいえ

      <img src="images/create-azure-functions-05.png" />

  - **デプロイ**

    - **継続的デプロイ**: 無効化

      <img src="images/create-azure-functions-06.png" />

  - **確認および作成** をクリック、表示される内容を確認し **作成** をクリック

    <img src="images/create-azure-functions-07.png" />

  </details>

  <br />

  <details>
    <summary>Python</summary>

  - **基本**

    - **プロジェクトの詳細**

      - **サブスクリプション**: ワークショップで使用するサブスクリプション

      - **リソース グループ**: ワークショップで使用するリソース グループ

    - **インスタンスの詳細**

      - **関数アプリ名**: 任意の名前 (2 ～ 60 文字、英数字、およびハイフンのみ)

      - **コードまたはコンテナー**: コード

      - **ランタイム スタック**: Python

      - **バージョン**: 3.10

      - **地域**: リソース グループと同じ地域を選択

    - **オペレーティング システム**

      - **オペレーティング システム**: Linux

    - **ホスティング**

      - **ホスティング オプションとプラン**: Functions Premium

      - **Linux プラン**: 任意 (既定の名前を変更する場合は新規作成をクリックして入力)

      - **価格プラン**: エラスティック Premium EP1 (ACU 合計 210, 3.5 GB メモリ, 1 vCPU)

    - **ゾーン冗長**

      - **ゾーン冗長**: 無効

      <img src="images/create-azure-functions-python-02.png" />

  - **Storage**

    - **ストレージ アカウント**: (新規)xxx (名前を変更する場合は新規作成をクリックして入力、英子文字、数字で 3 ～ 24 文字)

      <img src="images/create-azure-functions-03.png" />

  - **ネットワーク**

    - **パブリック アクセスを有効にする**: オン

    - **ネットワーク インジェクションを有効にする**: オフ

      <img src="images/create-azure-functions-04.png" />

  - **監視**

    - **Application Insights を有効にする**: いいえ

      <img src="images/create-azure-functions-05.png" />

  - **デプロイ**

    - **継続的デプロイ**: 無効化

      <img src="images/create-azure-functions-06.png" />

  - **確認および作成** をクリック、表示される内容を確認し **作成** をクリック

    <img src="images/create-azure-functions-python-07.png" />

  </details>

<br />

### Task 2: Visual Studio Code からのデプロイ

- **Terminal** - **New Terminal** を選択し、ターミナルを表示

  <img src="images/git-config-01.png" />

- az login コマンドを実行

  ```
  az login
  ```

  Web ブラウザーが起動、サインイン画面が表示されるのでサインインを実行

  ※ サインイン後はブラウザを閉じる

- プロジェクト ファイルのディレクトリへ移動

  <details>
    <summary>C#</summary>

  ```
  cd src/CS/Api1
  ```

  </details>

  <br />

  <details>
    <summary>Python</summary>

  ```
  cd src/Python/Api1
  ```

  </details>

  <br />

- func azure functionapp publish コマンドでプロジェクト ファイルをデプロイ

  <details>
    <summary>C#</summary>
    
  ```
  func azure functionapp publish <作成した関数アプリ名>
  ```

  - デプロイが正常に終了したことを確認

    <img src="images/deploy-function-02.png" />

  </details>

  <br />

  <details>
    <summary>Python</summary>
    
  ```
  func azure functionapp publish <作成した関数アプリ名> --python
  ```

  - デプロイが正常に終了したことを確認

    <img src="images/deploy-function-02.png" />

  </details>

  <br />

### Task 3: 関数アプリの構成

- Azure ポータルで SQL Database (AdventureWorksLT) の管理ブレードを表示

  <details>
      <summary>C#</summary>

  - **接続文字列** を選択し **ADO.NET (SQL 認証)** の接続文字列をコピーし、メモ帳などのテキスト エディターに貼り付け

    <img src="images/sql-connection-string.png" />

  - **{your_password}** を SQL Database への認証で使用するアカウントのパスワードに変更

            ※ 後の手順で使用するためコピー

  </details>

  <br />

  <details>
      <summary>Python</summary>

  - **接続文字列** を選択し **ODBC (Node.js を含む) (SQL 認証)** の接続文字列をコピーし、メモ帳などのテキスト エディターに貼り付け

    <img src="images/sql-connection-string-python.png" />

  - **{your_password}** を SQL Database への認証で使用するアカウントのパスワードに変更

  - **接続文字列の冒頭 Driver={ODBC Driver 18 for SQL Server} を Driver={ODBC Driver 17 for SQL Server} に変更してください。**

            ※ 後の手順で使用するためコピー

  </details>

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

### Task 4: 関数アプリの実行

- Web ブラウザーを起動、アドレス バーに関数アプリの展開時に出力された URL を貼り付け

- ?id=xx (xx は数字、5, 7, 10, 22, 27, 35 の間で指定) を付与して実行

  <img src="images/function-result-01.png" />

  ※ データベースから取得したレコードを表示

<br />

