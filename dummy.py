import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}
data = '''Bangladesh,[a] officially the People's Republic of Bangladesh,[b] is a country in South Asia. It is the eighth-most populous country in the world and among the most densely populated with a population of 170 million in an area of 148,460 square kilometres (57,320 sq mi). Bangladesh shares land borders with India to the north, west, and east, and Myanmar to the southeast. To the south, it has a coastline along the Bay of Bengal. To the north, it is separated from Bhutan and Nepal by the Siliguri Corridor, and from China by the mountainous Indian state of Sikkim. Dhaka, the capital and largest city, is the nation's political, financial, and cultural centre. Chittagong is the second-largest city and the busiest port. The official language is Bengali, with Bangladeshi English also used in government.

Bangladesh is part of the historic and ethnolinguistic region of Bengal, which was divided during the Partition of British India in 1947 as the eastern enclave of the Dominion of Pakistan, from which it gained independence in 1971 after a bloody war.[17] The country has a Bengali Muslim majority. Ancient Bengal was known as Gangaridai and was a stronghold of pre-Islamic kingdoms. The Muslim conquest after 1204 led to the sultanate and Mughal periods, during which an independent Bengal Sultanate and wealthy Mughal Bengal transformed the region into an important centre of regional affairs, trade, and diplomacy. The Battle of Plassey in 1757 marked the beginning of British rule. The creation of Eastern Bengal and Assam in 1905 set a precedent for the emergence of Bangladesh. The All-India Muslim League was founded in Dhaka in 1906.[18] The Lahore Resolution in 1940 was supported by A. K. Fazlul Huq, the first Prime Minister of Bengal. The present-day territorial boundary was established with the announcement of the Radcliffe Line.'''

maxL = 150
minL = 30

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": data,
	"parameters": {'max_length': maxL, 'min_length': minL},
})


print(output)
print(len(output[0]['summary_text']))
print(len(data))