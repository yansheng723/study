import wave

# 参考: https://blog.csdn.net/qq_39516859/article/details/79819276
def 从wav文件读取信息(文件名):
    #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据。
    文件 = wave.open(文件名,"rb")
    #读取格式信息
    帧数 = 文件.getnframes()
    信息 = {
        "帧": 文件.readframes(帧数),
        "频道数": 文件.getnchannels(),
        "量化位数": 文件.getsampwidth(),
        "帧速": 文件.getframerate()
    }
    文件.close()
    return 信息

# 参考: https://blog.csdn.net/zzZ_CMing/article/details/81739193
def 合成(文件名):
    帧 = []
    格式信息1 = 从wav文件读取信息("你.wav")
    格式信息2 = 从wav文件读取信息("好.wav")
    帧 = 格式信息1["帧"] + 格式信息2["帧"]

    文件 = wave.open(文件名, 'wb')
    文件.setnchannels(格式信息1["频道数"])
    文件.setsampwidth(格式信息1["量化位数"])
    文件.setframerate(格式信息1["帧速"])
    文件.writeframes(帧)
    文件.close()

    print("*"*10, "合成结束\n")

合成("你好.wav")