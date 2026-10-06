import subprocess
import os

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Lỗi khi chạy lệnh {command}: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))

def main():
    print("Bắt đầu mô phỏng bài tập Git Interactive Rebase...")
    
    # Khởi tạo repository Git tạm thời
    if not os.path.exists(".git"):
        run_command("git init")
    
    # Tạo các commit theo kịch bản
    # Commit 1
    with open("auth.js", "w") as f:
        f.write("// Module auth khoi tao")
    run_command("git add auth.js")
    run_command('git commit -m "feat: khoi tao module auth"')
    
    # Commit 2
    with open("auth.js", "a") as f:
        f.write("\n// Fix typo")
    run_command("git add auth.js")
    run_command('git commit -m "fix typo"')
    
    # Commit 3
    with open("auth.js", "a") as f:
        f.write("\n// Add utility functions")
    run_command("git add auth.js")
    run_command('git commit -m "adds utility functions"')
    
    # Commit 4
    with open("temp.txt", "w") as f:
        f.write("debug info")
    run_command("git add temp.txt")
    run_command('git commit -m "add temp file for debug"')
    
    print("Đã tạo xong 4 commit mẫu. Lịch sử hiện tại:")
    run_command("git log --oneline")
    
    print("\nHướng dẫn thực hiện Interactive Rebase thủ công:")
    print("Chạy lệnh: git rebase -i HEAD~4")
    print("Cấu hình các dòng trong trình soạn thảo:")
    print("pick <commit_1> feat: khoi tao module auth")
    print("squash <commit_2> fix typo")
    print("squash <commit_3> adds utility functions")
    print("drop <commit_4> add temp file for debug")
    print("Lưu lại và sửa thông điệp thành: feat: hoan thien module authentication")

if __name__ == "__main__":
    main()
