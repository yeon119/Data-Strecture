from ArrayList import ArrayList

list = ArrayList(100)

while True:
    command = input("[메뉴 선택] :i= 삽입, d= 삭제, r= 변경, p= 출력, l= 파일열기, s= 파일 저장, q= 종료")

    if command == "i":
        pos = input("입력할 행 번호:")
        str = input("입력 행 내용")
        ArrayList.insert(pos,str)
    
    elif command == "d":
        pos = input("삭제할 행 번호:")
        ArrayList.delete(pos)
    
    elif command == "r":
        pos = input("변경할 행 번호")
        str = input("변경할 행 내용")
        ArrayList.replace(pos,str)

    elif command == "p":
        ArrayList.__str__

    elif command == "l" :
        filename = input("불러올 파일 이름을 입력해주세요")    #'202344070/C_DS/test.txt' 
        filename = '202344070/C_DS/' + filename #파일 위치떄문에 따로 지정
        infile = open(filename, "r" ,encoding="UTF-8")
        lines = infile.readlines() # 모두 통으로 읽으려면 lines
        for line in lines:
             list.insert(list.size, line.rstrip('\n'))
        infile.close()
        print("파일을 읽어왔습니다.")




        

    