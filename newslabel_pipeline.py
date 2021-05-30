import pandas as pd

# 使用時改一下path即可
# 記得pip install openpyxl
# excel 檔須先從google sheet上下載下來as .xlsx
path = "/Users/timmyhsu/Desktop/rss crawl.xlsx"
xls = pd.ExcelFile(path,engine='openpyxl')

def title_plus_summary_add_label(df,string):
	df = df.drop_duplicates(subset=['Title','Summary'])
	df["title_plus_summary"] = df["Title"]+df["Summary"]
	df["label"] = string
	return df[["title_plus_summary","label"]]

# 即時 (不用了)
# ltn_news = pd.read_excel(xls,"即時")
# et_news = pd.read_excel(xls,"et 即時")
# news = ltn_news[20:].append(et_news[20:])
# news = title_plus_summary_add_label(news,"即時")

# 政治
ltn_politics = pd.read_excel(xls,"政治的archive")
et_politics = pd.read_excel(xls,"et 政治")
nt_politics = pd.read_excel(xls,"nt政治")
politics = ltn_politics.append([et_politics[20:],nt_politics[20:]])
politics = title_plus_summary_add_label(politics,"政治")

# 社會
ltn_society = pd.read_excel(xls,"社會")
et_society = pd.read_excel(xls,"et社會")
nt_society = pd.read_excel(xls,"nt社會")
society = ltn_society[20:].append([et_society[20:],nt_society[20:]])
society = title_plus_summary_add_label(society,"社會")

# 生活
ltn_life = pd.read_excel(xls,"生活")
et_life = pd.read_excel(xls,"et生活")
nt_life = pd.read_excel(xls,"nt生活")
life = ltn_life[20:].append([et_life[20:],nt_life[20:]])
life = title_plus_summary_add_label(life,"生活")

# 娛樂
ltn_entertain = pd.read_excel(xls,"娛樂")
et_entertain = pd.read_excel(xls,"et娛樂")
nt_entertain = pd.read_excel(xls,"nt娛樂")
entertain = ltn_entertain[20:].append([et_entertain[20:],nt_entertain[20:]])
entertain = title_plus_summary_add_label(entertain,"娛樂")

# 評論
ltn_op = pd.read_excel(xls,"評論")
et_op = pd.read_excel(xls,"et評論")
nt_op = pd.read_excel(xls,"nt評論")
op = ltn_op[20:].append([et_op[20:],nt_op[20:]])
op = title_plus_summary_add_label(op,"評論")

# 國際
ltn_intl = pd.read_excel(xls,"國際")
et_intl = pd.read_excel(xls,"et國際")
nt_intl = pd.read_excel(xls,"nt國際")
intl = ltn_intl[20:].append([et_intl[20:],nt_intl[20:]])
intl = title_plus_summary_add_label(intl,"國際")

# 財經
ltn_bus = pd.read_excel(xls,"財金")
et_bus = pd.read_excel(xls,"et 財經")
nt_bus = pd.read_excel(xls,"nt財經")
bus = ltn_bus[20:].append([et_bus[20:],nt_bus[20:]])
bus = title_plus_summary_add_label(bus,"財經")

# 體育
ltn_sport = pd.read_excel(xls,"體育")
et_sport = pd.read_excel(xls,"et體育")
nt_sport = pd.read_excel(xls,"nt體育")
sport = ltn_sport[20:].append([et_sport[20:],nt_sport[20:]])
sport = title_plus_summary_add_label(sport,"體育")

# 地方（不用了）
# ltn_local = pd.read_excel(xls,"地方")
# et_local = pd.read_excel(xls,"et地方")
# local = ltn_local[20:].append(et_local[20:])
# local = title_plus_summary_add_label(local,"地方")

# 蒐奇
ltn_novel = pd.read_excel(xls,"蒐奇")
et_novel = pd.read_excel(xls,"et蒐奇")
nt_novel = pd.read_excel(xls,"nt蒐奇")
novel = ltn_novel[20:].append([et_novel[20:],nt_novel[20:]])
novel = title_plus_summary_add_label(novel,"蒐奇")

concat_list = [politics,society,life,entertain,op,intl,bus,sport,novel]
df = pd.concat(concat_list,sort=True,ignore_index=True)
df.to_csv('新聞-類別配對.csv')




