#ete mi textum uzumenq barery gtnenq , hashvenq voric qanisna
sample_text=" is, simply dummy text .of the printing and typesetting industry Lorem Ipsum has been the industrys standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to"
words_dict={}

sample_text=sample_text.lower()# bolory poqratar e sarqum vor heto nuyn barery mecatari patcharov tarber chhamari
sample_text=sample_text.replace(",","")# sa nra hamar e vor storaketnery jnji
sample_text=sample_text.replace(".","")# sa nra hamar e vor ketery jnji
sample_text=sample_text.split(" ")#taranjatum enq bolor barery vorpes arandzin string


# vor gtni chkrknvox barery u avelacni nor words_dictin
for word in sample_text:
	if word in words_dict.keys():
		words_dict[word]+=1
	else:
		words_dict[word]=1# arajin angam handipelis bary else ov kgna heto arden if ov
# sa el kazmum enq nra hamar vor tpi miayn 2ic avel krknvox barery

for (word,amount) in words_dict.items():
	if amount>2:
		print(word,":",amount)
