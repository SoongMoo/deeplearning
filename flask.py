# http://localhost:5000

from flask import Flask

# Flask 애플리케이션 객체를 생성합니다.
# 인자 __name__은 모듈의 이름을 전달하며, Flask가 템플릿과 정적 파일을
# 찾는 데 필요합니다.
app = Flask(__name__)

# '/' 경로는 웹사이트의 루트(기본) URL을 의미합니다.
# 사용자가 이 경로로 접속하면 바로 아래의 'hello_world' 함수가 실행됩니다.
@app.route('/')
def hello_world():
    # 함수는 웹 브라우저에 표시할 응답을 반환합니다.
    return 'Hello, World!'

# 이 코드는 스크립트를 직접 실행할 때만 웹 서버를 시작하도록 보장합니다.
if __name__ == '__main__':
    # 디버그 모드를 활성화하면 코드를 변경할 때마다 서버를 수동으로
    # 다시 시작할 필요 없이 자동으로 변경 사항이 반영됩니다.
    app.run(debug=True)