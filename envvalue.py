import streamlit as st
import os


# パスワードの確認
def check_password():
    # 環境変数を取得
    PASSWD = os.environ.get('PASS_KEY')

    """ パスワードを確認する関数 """
    password = st.text_input("パスワードを入力してください", type="password")
    return password == PASSWD  # ここに適切なパスワードを設定してください
    
# main
def main():
    st.title('環境変数のデモ')

    if check_password():
        st.write(f'パスワードは正しいです')
    else:
        st.write(f'パスワードは間違っています')


if __name__ == "__main__":
    main()
