
try:
    # 텍스트 파일 오픈
    f = open('./0713/data/readme.txt', mode='r', encoding='utf-8')
    f2 = open('./0713/data/writeme.txt', mode='w', encoding='utf-8')

    line = f.read()
    while line:
        print(line)
        f2.write(line)      # line을 그대로 f2에 출력
        line = f.read()

    # 데이터 쓰기
    f2.write("\n추가 내용입니다.")
    f2.close()

    # 파일 닫기
    f.close()

    print('파일 작성 완료!')

except Exception as e:
    print('예외 발생 : {0}'.format(e))

