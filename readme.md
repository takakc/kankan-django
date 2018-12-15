# django
## インストール手順書
- PIPのバージョンを最新
  ```
  python3.6 -m pip install --upgrade pip
  ```

- フォルダ作成
  ```
  mkdir kankanDjango
  ```

- パッケージリスト
  ```
  touch ./kankanDjango/requirements.txt
  ```
  ``` requirements.txt
  Django~=2.1.3
  ```

- kankanDjangoフォルダでdjangoインストール
  ```
  pip3.6 install -r requirements.txt
  ```

## プロジェクト作成
- kankanAppプロジェクト作成
  ```
  django-admin startproject kankanApp .
  ```
- 設定変更
  - kankanApp/settings.py
    ```
    # 時間
    TIME_ZONE = 'Asia/Tokyo'

    # 言語
    LANGUAGE_CODE = 'ja'

    # 追加
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ```

```
python3.6 manage.py migrate
```
- メインアプリケーション作成
  ```
  python3.6 manage.py startapp main
  ```

- staticフォルダ作成
  ```
  python3.6 manage.py collectstatic
  ```