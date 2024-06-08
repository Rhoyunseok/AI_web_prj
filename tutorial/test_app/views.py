# test_app/views.py

import csv
from django.conf import settings
from django.shortcuts import render
import os

def get_image_paths_from_csv():
    # CSV 파일 경로 리스트
    csv_file_paths = [
        "beer.csv",
        "cocktail.csv",
        "custom_coctail.csv",
        "de_wine.csv",
        "traditional.csv",
        "traditional_liquor.csv",
        "whisky_taste.csv"
    ]

    # 이미지 파일 경로를 저장할 리스트 초기화
    image_file_paths = []

    for csv_file in csv_file_paths:
        csv_file_path = os.path.join(settings.BASE_DIR, "AI_web_prj/tutorial/data_a", csv_file)

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # 헤더를 건너뜁니다.
            for row in reader:
                image_file_path = os.path.join(settings.MEDIA_URL, row[0])  # CSV 파일의 첫 번째 열이 이미지 파일 경로인 경우
                image_file_paths.append(image_file_path)

    return image_file_paths

def show_drink_images(request):
    # CSV 파일에서 이미지 파일 경로를 가져옵니다.
    image_file_paths = get_image_paths_from_csv()

    # 템플릿 파일에 이미지 파일 경로 리스트를 전달합니다.
    return render(request, 'drink_template.html', {'image_file_paths': image_file_paths})
