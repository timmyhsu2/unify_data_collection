# unify_data_collection

## Email Crawler 

Supported functionalities:
* correctly decode content into either html text or plain text (latter chosen if both exist)
* print subject, from, index number, content to screen
* pinpoint subject and from decoding failure by "慘了 subject跑不出來" and "慘了 from跑不出來" (see following 7 out of 2838: index 236/838/1389/2114/2115/2116/2230)
* control starting point of email crawler by slicing the list inbox_item_list
* support utf-8, Big5, and GBK encoding  

Future actions:
* establish more sustainable way to store data
* solve decoding failure of subject and from
* easier inspection for correctness of decoding

## RSS Crawler

Supported functionalities:
* render rss from 自由時報、東森新聞雲、新頭殼 
* labels including: 政治、社會、生活、娛樂、評論、國際、財經、體育、蒐奇
* capture and store the above record periodically (per hour)
* remove duplicates from the periodic captures
* add label for each article w.r.t their category defined on company's rss website
  * 國際、et國際、nt國際 should be labelled "國際"
* store title+content/label records in a .csv file

Future actions:
* establish more sustainable way to store data
* add consistent index to each distinct record even with updates in data
* clear workflow between data used for recommendation system and NLP model to not mess up the data


