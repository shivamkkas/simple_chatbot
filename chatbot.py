import tkinter as tk
from tkinter import scrolledtext
import calendar
from tkinter.ttk import *
import re
import webbrowser
import wikipedia
import subprocess
from time import strftime
from googletrans import Translator
import random
import requests
from geopy.geocoders import Nominatim
from datetime import datetime

class SimpleChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Simple Chatbot")

        self.chat_history = scrolledtext.ScrolledText(master,bg="#ADD8E6", wrap=tk.WORD, width=40, height=10)
        self.chat_history.pack(padx=10, pady=10)
        self.master.resizable(0,0)

        self.user_input = tk.Entry(master, width=40)
        self.user_input.pack(padx=10, pady=10)

        self.send_button = tk.Button(master, bg="blue",text="Send", command=self.process_input)
        self.send_button.pack(pady=10)

        # Initialize chat history
        self.display_message("Hello! I'm your simple chatbot. Ask me anything!")

    def get_current_time(self):
        """Return the current date and time."""
        current_time = datetime.now()
        return current_time
    

    def get_state_or_union_territory(self,input_data, is_state_to_capital=True):
        india_capitals = {
            'Andhra Pradesh': 'Amaravati',
            'Arunachal Pradesh': 'Itanagar',
            'Assam': 'Dispur',
            'Bihar': 'Patna',
            'Chhattisgarh': 'Raipur',
            'Goa': 'Panaji',
            'Gujarat': 'Gandhinagar',
            'Haryana': 'Chandigarh',
            'Himachal Pradesh': 'Shimla',
            'Jharkhand': 'Ranchi',
            'Karnataka': 'Bengaluru',
            'Kerala': 'Thiruvananthapuram',
            'Madhya Pradesh': 'Bhopal',
            'Maharashtra': 'Mumbai',
            'Manipur': 'Imphal',
            'Meghalaya': 'Shillong',
            'Mizoram': 'Aizawl',
            'Nagaland': 'Kohima',
            'Odisha': 'Bhubaneswar',
            'Punjab': 'Chandigarh',
            'Rajasthan': 'Jaipur',
            'Sikkim': 'Gangtok',
            'Tamil Nadu': 'Chennai',
            'Telangana': 'Hyderabad',
            'Tripura': 'Agartala',
            'Uttar Pradesh': 'Lucknow',
            'Uttarakhand': 'Dehradun',
            'West Bengal': 'Kolkata',
            'Andaman and Nicobar Islands': 'Port Blair',
            'Chandigarh': 'Chandigarh',
            'Dadra and Nagar Haveli and Daman and Diu': 'Daman',
            'Lakshadweep': 'Kavaratti',
            'Delhi': 'New Delhi',
            'Puducherry': 'Puducherry',
        }

        # Reverse the dictionary to create a capital-state mapping
        capital_states = {v: k for k, v in india_capitals.items()}

        if is_state_to_capital:
            # Convert state to capital
            result = india_capitals.get(input_data, 'Unknown State or Union Territory')
        else:
            # Convert capital to state
            result = capital_states.get(input_data, 'Unknown Capital')

        return result    

    def process_input(self):
        user_message = self.user_input.get()
        self.display_message(f"You: {user_message}")
        self.user_input.delete(0, tk.END)  # Clear the input field

        # Process user input and generate a response
        bot_response = self.get_bot_response(user_message)
        self.display_message(f"Bot: {bot_response}")

    def solve_math_problem(self,expression):
  
        try:
            # Evaluate the mathematical expression
            result = eval(expression)
            return result
        except Exception as e:
            # Handle errors, such as invalid expressions
            return f"Error: {e}"
    def get_bot_response(self, user_input):
        greeting=['hello','hi']
        questions=['what are you doing?','how are you',"i love you","are you single","are you male or female"]
        rules=["1.! symbol is used before asked a question\n","2.Translate the text\n","3.Recommandation system(movies ,books,music,etc) use recommend in statement\n","4. I can open calculator\n",
               "5.I can show you a digital clock by just include $time in your question$\n","6.I can give jokes\n","7.I can comment on your message\n",
               "8.I can tell you weather\n","9.I can give capital of states of india\n","10. I can give you state of capital\n","11.I can set timer\n","12.I can give solution for each questions\n",
               "13.I can solve mathematical expressions\n"]
        joke=["Why don\'t scientists trust atoms?Because they make up everything!",
"Did you hear about the mathematician who's afraid of negative numbers?He'll stop at nothing to avoid them.",
"What do you call fake spaghetti? An impasta.",
"Why did the scarecrow win an award? Because he was outstanding in his field.",
"How do you organize a space party? You planet.",
"I told my wife she was drawing her eyebrows too high. She looked surprised.",
"Why don't skeletons fight each other? They don't have the guts.",
"Parallel lines have so much in common. It's a shame they\'ll never meet.",
"Why don't oysters donate to charity? Because they are shellfish.",
"How does a penguin build its house? Igloos it together.",
"What do you call fake lettuce? A shamrock.",
"Why did the bicycle fall over? Because it was two-tired.",
"How do you make a tissue dance? You put a little boogie in it.",
"What did one wall say to the other wall? I'll meet you at the corner.",
'Why did the tomato turn red? Because it saw the salad dressing!',"What\'s a vampire\'s favorite fruit? A blood orange.","Why don\'t skeletons fight each other? They don\'t have the guts.",
'Did you hear about the cheese factory explosion?','There was nothing left but de-brie.',
'What\'s a pirate\'s favorite letter? Arrrr!',
"Why did the coffee file a police report? It got mugged."]
        recommendations = {
    "movies": ["Inception", "The Shawshank Redemption", "The Matrix", "Interstellar", "Pulp Fiction"],
    "books": ["To Kill a Mockingbird", "1984", "The Great Gatsby", "The Catcher in the Rye", "Harry Potter series"],
    "music": ["The Beatles", "Queen", "Michael Jackson", "Ed Sheeran", "Billie Eilish"]
}

        if user_input.lower() == 'exit':
            return"Goodbye! Have a great day."
            

        if  user_input.lower() in greeting:
            return" {} there! How can I help you?".format(user_input)
        
        elif user_input.lower() in questions:
            return"Thank you for Asking ,But I am only a computer program"
        
        elif re.search(r'\brules\b', user_input, re.IGNORECASE):
            result_list = ['' + string + '' for string in rules]

            final_result = '\n'.join(result_list)
            return final_result 
        elif re.search(r'\bcalculator\b', user_input, re.IGNORECASE):
            subprocess.run('calc.exe', shell=True)
        elif re.search(r'\btranlate\b',user_input,re.IGNORECASE):
            try:
                # Extract the text to be translated
                text_to_translate = user_input.split("translate")[1].strip()
                
                # Translate the text to English (you can modify the target language if needed)
                translator = Translator()
                translation = translator.translate(text_to_translate, dest='en')
                
                return f"The translation is: {translation.text}"
                       
            except Exception as e:
                return "Error during translation. Please try again."
                         
        elif re.search(r'\bThank you\b', user_input, re.IGNORECASE):
            return "Its my pleasure!"
        elif re.search(r'\brecommend\b',user_input,re.IGNORECASE):
            
            def get_personalized_recommendation(category):
                category = category.lower()
                if category in recommendations:
                    return random.choice(recommendations[category])
                else:
                    return "I'm sorry, I don't have recommendations for that category."
            try:
                category = user_input.split("recommend")[1].strip()
                recommendation = get_personalized_recommendation(category)
                return f"I recommend checking out {recommendation} in the {category} category."

            except Exception as e:
                return "Error while providing recommendations. Please try again."
    
        


        elif re.search('^!', user_input, re.IGNORECASE):
            return "According to Wikipedi:",wikipedia.summary(user_input)
        elif re.search(r'\btime\b', user_input, re.IGNORECASE):
            get=self.get_current_time()
            return get
            

        elif re.search(r'\bjoke\b', user_input, re.IGNORECASE):
            return random.choice(joke)

        elif re.search(r'\bsports game\b', user_input, re.IGNORECASE):
            return "I'm sorry, I don't have the latest sports game information."

        elif re.search(r'\bcapital of\b', user_input, re.IGNORECASE):
            state_name= user_input.split("of")[1].strip().title()
            capital_result = self.get_state_or_union_territory(state_name)
            return f"The capital of {state_name} is {capital_result}"

        elif re.search(r'\bstate of\b', user_input, re.IGNORECASE):
            capital_name= user_input.split("of")[1].strip().title()
            state_result = self.get_state_or_union_territory(capital_name, is_state_to_capital=False)
            return f"The state or union territory with capital {capital_name} is {state_result}"


        elif re.search(r'\bset a timer for\b', user_input, re.IGNORECASE):
            timer_match = re.search(r'\b(?:set a timer for)\s+(\d+)\s+minutes?\b', user_input, re.IGNORECASE)
            if timer_match:
                minutes = timer_match.group(1)
                return f"Timer set for {minutes} minutes."
 
        elif re.search(r'\b my name is\b', user_input, re.IGNORECASE):
            user_name = user_input.replace("my name is","").strip()
            return "hello!"+ user_name
        
        elif re.search(r'\bclear\b',user_input,re.IGNORECASE):
             return self.clear_window()
        
        elif re.search(r'\bsolve\b',user_input,re.IGNORECASE):
            equation = user_input.replace("solve","").strip()
            answer=self.solve_math_problem(equation)
            return answer

        else:
            return " I'm not sure how to respond to that. Ask me something else."
    
    def clear_window(self):
        self.chat_history.delete(1.0, tk.END)
        self.user_input.delete(0, tk.END)
    def display_message(self, message):
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.yview(tk.END)  

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = SimpleChatbot(root)
    root.mainloop()
