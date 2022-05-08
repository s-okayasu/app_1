import traceback

def exec(input):
    try:
        # inputには入力情報が配列の要素として格納されています。
        # 処理を追記して、期待値と同じ値をoutputで返却してください。

        output = 'execute.py に処理を追記してください。'

    except Exception as ex:
        output = traceback.format_exception(type(ex), ex, ex.__traceback__)
        print('debug log : exception\n')
        for data in output:
            print(data)
        return output

    print('debug log : output=' + str(output))
    return output
