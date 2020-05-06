import requests
import time
import hashlib
import console
import dialogs


def main():
    # 多行文本
    text = dialogs.text_dialog("这次想bb点啥？")
    # 单行文本
    #text = console.input_alert(u'这次想bb点啥？')
    if not text:
        print('No text input found.')
        return
    appId = 'Xq4li4CYL95Qv9GsJSiB8B2M-MdYXbMMI'
    masterKey = 'Kaa95X0LUHflxIojiFn7spsU'
    timestamp = int(round(time.time() * 1000))

    ret = str(timestamp) + masterKey
    sign = hashlib.md5(ret.encode('utf-8')).hexdigest()
    data = {"content": text}

    headers = {
        'Content-Type': 'application/json',
        'X-LC-Id': appId,
        'X-LC-Sign': "{},{},master".format(sign, timestamp)

        }

    url = 'https://{}.api.lncldglobal.com/1.1/classes/content'.format(
        appId[:8])

    print(u'开始bb...')

    r = requests.post(url, json=data, headers=headers)

    print(u'bb中...')

    if r.status_code == 201:
        print(u'bb成功！')
        print(r.text)
    else:
        print(u'bb失败！')
        print(r.text)


if __name__ == '__main__':
    main()
