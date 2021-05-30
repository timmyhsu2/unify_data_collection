# unify_data_collection

## Email Crawler 

Supported functionalities:
* correctly decode content into either html text or plain text (latter chosen if both exist)
* print subject, from, index number, content to screen
* pinpoint subject and from decoding failure by "慘了 subject跑不出來" and "慘了 from跑不出來" (see below 7 out of 2838)
* control starting point of email crawler by slicing the list inbox_item_list
* support utf-8, Big5, and GBK encoding  

Future actions:
* establish more sustainable way to store data
* solve decoding failure of subject and from
* easier inspection for correctness of decoding


