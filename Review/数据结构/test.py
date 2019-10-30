# coding=utf-8
import sys


def solution(long_string, alphabet):
    # 在这里写你的实现
    if len(long_string)<len(alphabet):
        return ""
    result=[]
    for i in range(len(long_string)):
        array=[]
        alphabets=list(alphabet)
        if long_string[i] in alphabets:
            start=i
            alphabets.remove(long_string[i])
            array.append(long_string[i])
            while start+1<len(long_string):
                start=start+1
                array.append(long_string[start])
                if long_string[start] in alphabets:
                    alphabets.remove(long_string[start])
                    if len(alphabets)==0:
                        result.append(array)
                        break
    if len(result)==0:
        return ""
    else:
        b=[]
        for i in range(len(result)):
            b.append(len(result[i]))
        index=b.index(min(b))
        return ''.join(result[index])


if __name__ == "__main__":
    # 读取第一行的n
    long_string = sys.stdin.readline().strip()
    alphabet = sys.stdin.readline().strip()
    print(solution(long_string, alphabet))