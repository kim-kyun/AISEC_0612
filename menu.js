menu_sets = []
//메뉴 생성기 시작 S==============================
class Menu {
    constructor(mtitle) {
        this.mtitle = mtitle;
    }
    mtitle; url; tips;
}
//?menu=0 의 쿼리스트링은 데이터 생성함수 data_sets 객체의 push 순서와 일치합니다.
menu0 = new Menu("1. 로또번호 선형회귀 예측")//1. 개발목적/언어-선정/요구사항명세/분석 2. 구현도구/라이센스 3. 테스트도구(junit,mockobj)  4. 형상관리도구  5. 빌드도구
menu0.url = "?menu=0"
menu0.tips = ["1.1 데이터 수집 및 전처리", "1.2 회귀예측 모델 구성 및 훈련 평가", "1.3 코드 리팩토링", "1.4 플라스크 미들웨어 구현", "1.5 사용자 UI 구현", "1.6 로또 예측 서비스 구동"]

menu_sets.push(menu0)


