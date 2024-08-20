from langchain.llms import Llama31
from langchain.agents import create_openai_online_agent
from langchain.prompts import PromptTemplate

def get_real_time_data(song_name):

    # initalizing LangChain online agent
    online_agent = create_openai_online_agent()


    prompt_template = PromptTemplate(
        input_variables=['song_name'],
        template= "Compile a list of the most similar songs to song: {song_name}."
    )

    response = online_agent.run(prompt_template, {"song_name": song_name})
    return response


if __name__ == "__main__":
    song_name = input("Enter a song: ")
    result = get_real_time_data(song_name)
    print(result)
