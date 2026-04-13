from ArrayList import ArrayList

List = ArrayList(1000)

while True:
    command = input("[메뉴선택] i= 삽입, d= 삭제, r= 변경, p= 출력, l= 파일열기, s= 파일 저장, q= 종료")

    if command == "i" :
        pos = int(input("입력행 번호:")) # 데이터를 지정할 번호이니까 정수자료형으로 만듬
        str = input("입력행 내용:")
        List.insert(pos,str)

    elif command == "d" :
        pos = int(input("삭제행 번호:"))
        List.delete(pos)
        
    elif command == "r" :
        pos = int(input("변경행 번호:"))
        str = input("변경할 내용:")
        List.replace(pos,str)

    elif command == "p" :
            print("인하의 라인 에디터")
            for line in range(List.size):
                print("[%2d] : "%line, end='') 
                print(List.getEntry(line))

                 
    elif command == "l" :
        filename = input("불러올 파일 이름을 입력해주세요")    #'202344070/C_DS/test.txt' 
        filename = '202344070/C_DS/' + filename #파일 위치떄문에 따로 지정
        infile = open(filename, "r" ,encoding="UTF-8")
        lines = infile.readlines() # 모두 통으로 읽으려면 lines
        for line in lines:
             List.insert(List.size, line.rstrip('\n'))
        infile.close()
        print("파일을 읽어왔습니다.")


    elif command == "s" :
        filename = input("저장할 파일 이름을 입력해주세요")    #'202344070/C_DS/test.txt'
        filename = '202344070/C_DS/' + filename
        outfile = open(filename, "w" ,encoding="UTF-8") # W => 쓰기 전용
        len = List.size
        for i in range(len):
             outfile.write(List.getEntry(i)+'\n')
        outfile.close
        print("파일을 저장했습니다.")

    elif command == "q" :
        exit()
