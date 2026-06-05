parametric knowledge: basically llm do this by getting all the accesss of the data on the internet during the pretraining time and just store all the info in the form of parameters
and when the users prompt they get the info by this 


#Problems
1:private data
2:recent data
3:hallucination

#solution:fine-tuning

there are many types of fine-tuning
1:Supervised Training: in this we give llm the prompt and desired output with that prompt now that is called supervised ex:ScaleAI work was to generate this in huge amount for company like OPENAI to use

2:Continued Pretraining:it is unsupervised pretraining in this we did not get the model the desired output but the data and the model just like in training phase process the data and work with the help of it 

3:RLHF: In this training aspect you training(Reinforcement Learning from Human Feedback) in this a llm is seperately trained to processs the things and give rewards to llm in this the rating help in determing which answer should be given to each of them by the help of this the models like chatgpt became conversational and have so much conversation powers



#problems with fine tuning
1: basicaslly it is very expensive to train the models down it is expensive 
2: require so much technical expertise and its expensive and difficulttt


so the new solution

INCONTEXT LEARNING"
IN Incontext learning we make to learn the llm by the help of giving possible examples and the model train itself by analyzing the previous examples and set the benchmark for it write basically it do it by training from its thingsss in the example given from prompt and don the task

it is called few shot prompt 

it is calleds Emergent Property as it suddenly emerges in the system by training in such a billion parameters


now the RAG Is a way to give extra info at the time we ask for questions in itttt
so thats why with the help of this context+userquery get the personalized result when it get into llm

RAG = INFORMATION Retriver + text generation

Rag is divided into these stages

1:INDEXING
2:RETRIEVER
3:AUGUMENTATION
4:GENERATION

    INDEXING:    DOCUMENT INGESTION
                 TEXT CHUNKING
                 EMBEDDING GENERATION
                 STORAGE IN VECTOR STORE

    RETRIEVAL:   searching the query with the vector store

    Augumentation:   query+contextual thing from store

    Generation




    therefore rag is a cheaper option as fine tuning and it 






