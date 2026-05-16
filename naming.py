import os
import re

# ── 설정 ──────────────────────────────────────────────
folder_path = r"C:\...\2일차\1회"   # 실제 폴더 경로로 변경하세요

new_names = [
    "01.시료에 접속",
    "02.로그인 수행 완료",
    "03.item 등록 메뉴",
    "04.item 등록 시도",
    "05.item 등록 완료",
    "06.등록한 item 선택",
    "07.소수점 세 자릿수 입력",
    "08.소수점 세 자릿수 저장 수행",
    "09.소수점 세 자릿수 저장 결과",
    "14.UI에서 소수점 세 자릿수 업데이트 결과",
]
# ──────────────────────────────────────────────────────

# 1) 스크린샷 파일만 추출 (패턴: 스크린샷 YYYY-MM-DD HHMMSS.png)
pattern = re.compile(r"스크린샷 \d{4}-\d{2}-\d{2} \d{6}\.png$")
files = sorted(
    [f for f in os.listdir(folder_path) if pattern.match(f)]
)  # 파일명 사전순 = 시간순

print(f"발견된 파일 수: {len(files)}개 / 새 이름 수: {len(new_names)}개\n")

if len(files) != len(new_names):
    print("[경고] 파일 수와 새 이름 목록 수가 다릅니다. 확인 후 재실행하세요.")
else:
    # 2) 변경 전 미리보기
    print("── 변경 예정 목록 ──────────────────────")
    for old, new in zip(files, new_names):
        print(f"  {old}  →  {new}.png")

    # 3) 확인 후 실행
    confirm = input("\n위 내용으로 변경하시겠습니까? (y/n): ").strip().lower()
    if confirm == "y":
        for old, new in zip(files, new_names):
            old_path = os.path.join(folder_path, old)
            new_path = os.path.join(folder_path, new + ".png")
            os.rename(old_path, new_path)
            print(f"완료: {old}  →  {new}.png")
        print("\n모든 파일 이름 변경이 완료되었습니다.")
    else:
        print("취소되었습니다.")