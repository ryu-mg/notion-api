import os
from dotenv import load_dotenv
from notion.client import NotionClient


load_dotenv(verbose=True)
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_EMAIL = os.getenv('NOTION_EMAIL')
NOTION_PASSWORD = os.getenv('NOTION_PASSWORD')
NOTION_PAGE_URL = os.getenv('NOTION_PAGE_URL')

# token을 통한 client 생성
token_client = NotionClient(token_v2=NOTION_TOKEN)
# user info를 통한 client 생성
user_info_client = NotionClient(email=NOTION_EMAIL, password=NOTION_PASSWORD)

# 수정할 페이지 URL 지정
"""
notion client 생성 시, 유의 사항
loadPageChunk가 최근 100000개로 증가함에 따라 브라우져에서 requests.execptions.HTTPError: invalid input 에러를 발생시킴
따라서 notion store 스크립트 중 call_load_page_chunk 메서드 중 data.limit을 10으로 변경 하여 진행
변경하지 않으면 페이지를 가져올 수 없음 
"""
page = user_info_client.get_block(NOTION_PAGE_URL)

# page title 출력
print(page.title)

# page 타이틀 수정
page.title = '페이지 수정'

