from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])

#for every row you will get a new docs in the list and it is there to load in it 


 