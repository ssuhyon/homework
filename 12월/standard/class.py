class StandardClass:
    total_students = 0  # 전체 학생 수를 저장하는 클래스 변수

    def __init__(self):
        self.class_name = "스탠다드반"  # 반 이름 고정
        self.students = []  # 학생 정보를 저장할 리스트 초기화

    def __str__(self):
        # 학생 리스트가 비어 있는지 확인하여 메시지 반환
        if not self.students:
            return f"{self.class_name} 반에는 현재 학생이 없습니다."
        # 학생 정보를 포맷팅하여 문자열로 반환
        return "\n".join(
            [f"{s['name']} (나이: {s['age']}, 귀찮음: {s['bother_count']})" for i, s in enumerate(self.students)]
        )

    def add_student(self, name, age):
        # 학생 정보를 딕셔너리 형태로 추가
        self.students.append({"name": name, "age": age, "bother_count": 0})
        # 클래스 변수로 전체 학생 수 증가
        StandardClass.total_students += 1

    def bother_teacher(self, name):
        # 학생 리스트를 순회하며 이름이 일치하는 학생 찾기
        for student in self.students:
            if student["name"] == name:
                student["bother_count"] += 1  # 귀찮음 횟수 증가
                print(f"{name} 학생이 귀찮게 했습니다! (총 {student['bother_count']}회)")
                return
        # 이름이 없는 경우 메시지 출력
        print(f"{name} 학생을 찾을 수 없습니다.")

    def reset_bother_counts(self):
        # 학생 리스트를 순회하며 귀찮음 횟수를 초기화
        for student in self.students:
            student["bother_count"] = 0
        print("모두 나가주세요! 혼자 있고 싶으니까...")
        print("모든 귀찮음 횟수가 초기화되었습니다.")

if __name__ == "__main__":
    # 스탠다드반 생성
    class1 = StandardClass()

    # 학생 추가
    for name, age in [
        ("곽종태", 20), ("김모세", 20), ("김용수", 20), ("노호성", 21),
        ("박민지", 21), ("박종관", 21), ("백명남", 22), ("오세은", 22),
        ("유종열", 22), ("이수관", 23), ("이현지", 23), ("정지웅", 23),
        ("조수현", 24), ("최수빈", 24), ("최정은", 24)
    ]:
        class1.add_student(name, age)  # 이름과 나이를 사용해 학생 추가

    # 반 상태 출력
    print("\n<반 상태>")
    print(class1)  # 현재 반 상태 출력

    # 선생님 귀찮게 하기
    class1.bother_teacher("조수현")  # "조수현" 학생의 귀찮음 횟수 증가
    class1.bother_teacher("박민지")  # "박민지" 학생의 귀찮음 횟수 증가

    # 귀찮음 횟수 초기화
    class1.reset_bother_counts()  # 모든 학생의 귀찮음 횟수 초기화
    print("\n<귀찮음 횟수 초기화 후 반 상태>")
    print(class1)  # 초기화 후 반 상태 출력
