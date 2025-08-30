import requests
import pandas as pd

def save_to_excel(datalist, filename='data.xlsx'):
    # 将datalist转换为pandas的DataFrame
    df = pd.DataFrame(datalist)
    
    # 使用pandas将DataFrame写入Excel文件
    df.to_excel(filename, index=False, engine='openpyxl')
    print(f'数据已保存到 {filename}')

def zhuanye(current,id,name,zhuanyeList,regionName,featuresName):
    url = f"https://kaoyan.cqvip.com/api/kaoyan/info/reExamination/academic-years-scoreline?current={current}&size=20&schoolIds={id}&year=2024"

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'channelcode': 'pcKaoyan2',
    'cookie': 'duid=4479421159494445735; BOOK_TOKEN_=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJPcmdDb2RlIjoic21hcnRkZW1va3JzIiwibmJmIjoxNzM1Mjc0NjU1LCJleHAiOjE3MzUyODE4NTUsImlzcyI6IlNtYXJ0TGlicmFyeS5JZGVudGl0eUNlbnRlciIsImF1ZCI6IldlYkFwaSJ9.KtJYpby4VN5IuwjPIWmA6LeSbdC1E-wmoG5rvpW7mMc0MHZg5mumIUbg_DfEpjQHDokgt8tEuJUO-PY6LbQHbej_-4hvpM2NiJ24wcYBdCtfRnWbSZv7yre1sEXrMlgZYk5MzW7c8HD3dmnaPTc32-vqbedzwuIyqEOOzi2WDipGprjVJP4wPwJK-PgBXfRaBLqDEtKPRn5upt1OQKUdOL20XRWBaZNWrBrVTb_Jyy8gdyrh-B4kQTnFHMMJyyu2YnKibqnDviE0OQxKpWgFY0BweKYQhHulhDauv4-NnES5FXNdmay3nRpTnrc2Wj3zMLkVRvNJSLWm_RH3P-zFPw; Hm_lvt_04dac094451c2f9591092e758fc05936=1735274656; HMACCOUNT=432D5738E9905AA6; __root_domain_v=.cqvip.com; _qddaz=QD.503235274662380; _qdda=3-1.1; _qddab=3-p818ni.m569qaru; Hm_lpvt_04dac094451c2f9591092e758fc05936=1735274791',
    'dt': 'pc',
    'ht': 'kaoyan.cqvip.com',
    'platform': 'PCkaoyan',
     'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://kaoyan.cqvip.com/school/11/score?p=2',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'test': 'false',
    'timestamp': '1735274803417',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code ==200:
        aa = response.json()
        total = aa.get('data').get('total')
        pages = aa.get('data').get('pages')
        data = aa.get('data').get('records')
        if pages  ==0:
            return  zhuanyeList
        print(f'获取{name}大学专业成功。数据共计{total}条，页数共计{pages},当前页数为{current}')
        
        for  da  in data:
            year = da.get('year')#年份
            schoolName = da.get('schoolName')#大学名称
            majorType = da.get('majorType')#学位类型
            majorName = da.get('majorName')#专业类型
            majorCode = da.get('majorCode')#专业代码
            totalScore = da.get('totalScore')#总分
            totalScoreD = da.get('totalScoreD')#总分多
            politicsScore = da.get('politicsScore')#政治
            politicsScoreD = da.get('politicsScoreD')#政治多
            englishSocre = da.get('englishScore')#英语
            englishScoreD = da.get('englishScoreD')#英语多
            courseOneScore = da.get('courseOneScore')#专业课1
            courseOneScoreD = da.get('courseOneScoreD')#专业课1多
            courseTwoScore = da.get('courseTwoScore')#专业课2
            courseTwoScoreD = da.get('courseTwoScoreD')#专业课2多
            zhuanyeList.append({'年份':year,'大学名称':schoolName,'大学地点':regionName,'大学标签':featuresName,'学位类型':majorType,'专业类型':majorName,'专业代码':majorCode,
            '总分':totalScore,
            '政治':politicsScore,
            '英语':englishSocre,
            '专业课1':courseOneScore,
            '专业课2':courseTwoScore
            })
            # zhuanyeList.append({'年份':year,'大学名称':schoolName,'大学地点':regionName,'大学标签':featuresName,'学位类型':majorType,'专业类型':majorName,'专业代码':majorCode,
            # '总分':str(totalScore)+'↑'+str(totalScoreD),
            # '政治':str(politicsScore)+'↑'+str(politicsScoreD),
            # '英语':str(englishSocre)+'↑'+str(englishScoreD),
            # '专业课1':str(courseOneScore)+'↑'+str(courseOneScoreD),
            # '专业课2':str(courseTwoScore)+'↑'+str(courseTwoScoreD)
            # })
        if current != pages :
            current  +=1
            zhuanye(current,id,name,zhuanyeList,regionName,featuresName)
    return zhuanyeList

def getId(current,datalist):
    url = f"https://kaoyan.cqvip.com/api/kaoyan/info/school/index-page?current={current}&size=20"
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'channelcode': 'pcKaoyan2',
    'dt': 'pc',
    'ht': 'kaoyan.cqvip.com',
    'platform': 'PCkaoyan',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://kaoyan.cqvip.com/info/school?p=2',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'test': 'false',
    'timestamp': '1735297774793',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }

    response = requests.request("GET", url, headers=headers)
    if response.status_code ==200:
        aa = response.json()
        total = aa.get('data').get('total')
        page  = aa.get('data').get('pages')
        data = aa.get('data').get('records')
        print(f'获取数据成功。数据共计{total}条，页数共计{page},当前页数为{current}')
        for da in data:
            name = da.get('name')
            id = da.get('id')
            typeName = da.get('typeName')
            featuresName = da.get('featuresName')
            datalist.append({'大学名称':name,'大学id':id,'类型':typeName,'标签':featuresName})
            regionName = da.get('regionName')
            zhuanye(1,id,name,zhuanyeList,regionName,featuresName)

        if current != page:
            current+=1
            if  current == 20:
                return datalist
            getId(current,datalist)
    return datalist
datalist=[]

zhuanyeList=[]
getId(1,datalist)
save_to_excel(zhuanyeList)