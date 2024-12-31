import os
import requests


# 下载指定的JSON文件
def download_json_files(username, repo_name, json_files):
    base_url = f"https://oss.x-lab.info/open_digger/github/{username}/{repo_name}/"
    folder_name = f"data/opendigger_data/{repo_name}"  # 以项目名称命名本地文件夹

    # 创建项目文件夹（如有必要）
    os.makedirs(folder_name, exist_ok=True)

    # 遍历每个JSON文件，尝试下载
    for json_file in json_files:
        file_url = f"{base_url}{json_file}"
        print(f"Trying to download: {file_url}")
        response = requests.get(file_url)
        #response = requests.get(file_url, verify=False)
        if response.status_code == 200:  # 如果请求成功（状态码200）
            with open(f"{folder_name}/{json_file}", "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {json_file} for {repo_name}")
        else:
            print(f"Failed to download: {json_file} for {repo_name} (status: {response.status_code})")  # 下载失败时打印错误信息


# 主函数
def get_opendigger_data():
    # JSON文件列表
    json_files = [
        "active_dates_and_times.json", "activity_details.json", "activity.json",
        "attention.json", "bus_factor_detail.json", "bus_factor.json",
        "change_request_age.json", "change_request_resolution_duration.json",
        "change_request_response_time.json", "change_request_reviews.json",
        "change_requests.json", "code_change_lines_add.json",
        "code_change_lines_remove.json", "code_change_lines_sum.json",
        "contributor_email_suffixes.json", "inactive_contributors.json",
        "issue_age.json", "issue_comments.json", "issue_resolution_duration.json",
        "issue_response_time.json", "issues_and_change_request_active.json",
        "issues_closed.json", "issues_new.json", "new_contributors_detail.json",
        "new_contributors.json", "openrank.json", "participants.json",
        "stars.json", "technical_fork.json"
    ]

    # 用户名和仓库名的列表
    projects = [
        ("tensorflow", "tensorflow"),
        ("pytorch", "pytorch"),
        ("vuejs", "vue"),
        ("huggingface", "transformers"),
        ("tailwindlabs", "tailwindcss"),
        ("facebook", "react"),
        ("vercel", "next.js"),
        ("django", "django"),
        ("pallets", "flask"),
        ("expressjs", "express"),
        ("fastapi", "fastapi"),
        ("kubernetes", "kubernetes"),
        # ("docker-archive", "docker-ce"),
        ("hashicorp", "terraform"),
        ("ansible", "ansible"),
        ("d3", "d3"),
        ("plotly", "plotly.js"),
        ("godotengine", "godot"),
        ("bitcoin", "bitcoin"),
        ("Microsoft", "vscode"),
        ("Homebrew", "brew"),
    ]

    # 遍历每个项目并下载其JSON文件
    for username, repo_name in projects:
        print(f"Processing: {username}/{repo_name}")
        download_json_files(username, repo_name, json_files)


if __name__ == "__main__":
    get_opendigger_data()
