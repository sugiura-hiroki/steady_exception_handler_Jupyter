def main():
    from functools import partial
    from .core import SteadyExceptionHandler
    # from send_gmail import Send_Gmail

    # エラーによる停止時に自動メール送信
    # mailObj = Send_Gmail('py.auto.send@gmail.com')
    exceptionHandle = SteadyExceptionHandler(
        lambda : print('エラー発生'),
        # partial(
        #     mailObj.send,
        #     mail_title='エラー発生', 
        #     mail_text='エラー発生により、jupyterの実行を停止しました。', 
        #     mail_to='hiroki.sugiura.915@gmail.com'
        # )
    )

if __name__ == '__main__':
    main()
