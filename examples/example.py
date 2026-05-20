"""예제 Python 스크립트"""

def main():
    print("TestDev 예제 데이터 로딩 테스트")
    
    # JSON 데이터 로드 예시
    import json
    with open('data/sample.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("사용자 수:", len(data['users']))
    print("제품 수:", len(data['products']))

if __name__ == "__main__":
    main()