import tkinter as tk
from run import *
from tkinter import ttk

# application is a GUI interface of run.py

class application:
    
    def __init__(self):
        self.samples = 5
        self.samplelength = 50
        self.max_split = 2
        self.root = tk.Tk()
        self.root.wm_title("Audio Search Engine")
        self.show_enclosure()
        self.show_file_entry()
        self.show_buttons()
        self.show_result()
        self.show_canvas()
        self.show_menu()
        self.root.iconbitmap("img/logo.ico")      
        self.root.mainloop()
        self.filename=""
    
    # show right enclosure frame
    def show_enclosure(self):
        self.group_enclosure =tk.LabelFrame(self.root, text="", padx=5, pady=5, background="white")
        self.group_enclosure.pack(side="right")
    
    # show audio wavform canvas
    def show_canvas (self):
        self.group_canvas = tk.LabelFrame(self.group_enclosure, text="Top(Query) Bottom(Best Match)", padx=5, pady=5)
        self.group_canvas.pack(side='top')
        
        self.canvas_query = tk.Canvas(self.group_canvas, width = 200, height = 100, bg = 'black')
        self.canvas_result = tk.Canvas(self.group_canvas, width = 200, height = 100, bg = 'black')
        # pack the canvas into a frame/form
        
        self.canvas_query.pack(expand = 'yes', fill = 'both') 
        self.canvas_query.create_line(0, 50, 199.9, 50, fill="red", dash=(4, 4))
        
        self.canvas_result.pack(expand = 'yes', fill = 'both', side='bottom') 
        self.canvas_result.create_line(0, 50, 199.9, 50, fill="red", dash=(4, 4))   
                
        #self.photo = tk.PhotoImage(file = 'img/search.png',  width = 70, height = 70 )
        #self.canvas.create_image(5, 5, image=self.photo, anchor="nw")  
    
    def clear_canvas(self):
        self.canvas_query.create_rectangle(0, 0, 200, 100, fill="black")
        self.canvas_result.create_rectangle(0, 0, 200, 100, fill="black")
        self.canvas_query.create_line(0, 50, 199.9, 50, fill="red", dash=(4, 4))
        self.canvas_result.create_line(0, 50, 199.9, 50, fill="red", dash=(4, 4))
        
    # draw_wavform draws waveform of wav data to a target canvas
    def draw_wavform (self, wavdata, color, target):
        unit_x=200/len(wavdata)
        unit_y=20/max(wavdata)
        for i in range(len(wavdata)-1):   
            y_1 = wavdata[i]*unit_y + 50
            x_1 = i*unit_x
            y_2 = wavdata[i+1]*unit_y + 50
            x_2 = (i+1)*unit_x      
            if target == "query":
                self.canvas_query.create_line(x_1, y_1, x_2, y_2, fill=color, width=0.5)
            elif target == "result":
                self.canvas_result.create_line(x_1, y_1, x_2, y_2, fill=color, width=0.5)
    
    # refresh parameter labels
    def refresh_parameters (self):
        newtext="Number of Audio Samples to Compare: " + str(self.samples) + " repository Maximum Split Paramter: " + str(self.max_split) + " Word Length: " + str(self.samplelength )
        self.label_result.config(text=newtext)       
    
    # decrease number of samples (words or needles)   
    def sample_up (self):
        self.samples += 1
        self.refresh_parameters()    
        
    # decrease number of samples (words or needles)                    
    def sample_down (self):
        if self.samples > 0:
            self.samples -= 1
            self.refresh_parameters()        
            
    # increase samplelength (word size)    
    def word_up (self):
        self.samplelength += 5
        self.refresh_parameters()

    # decrease samplelength (word size)
    def word_down (self):
        if self.samplelength > 5:
            self.samplelength -= 5  
            self.refresh_parameters()
    
    # show_menu shows the menu at the top
    def show_menu (self): 
        self.menu = tk.Menu(self.root)
        self.menu.add_command(label="Search", command=self.on_button_click)
        self.menu.add_command(label="Precision +", command=self.sample_up)
        self.menu.add_command(label="Precision -", command=self.sample_down)
        self.menu.add_command(label="Word Size +", command=self.word_up)
        self.menu.add_command(label="Word Size -", command=self.word_down)        
        self.menu.add_command(label="Quit", command=self.quit)
        self.root.config (menu=self.menu)
        
    # add style (optional)
    def add_config (self):
        self.style = ttk.Style()
        #self.style.configure(... enter here ...)        

    # show textbox that holds the result of the search
    def show_result (self):
        self.group_result = tk.LabelFrame(self.root, text="", padx=5, pady=5)
        self.group_result.pack(padx=10, pady=15, side = 'left')
        self.label_result = tk.Label(self.group_result,  text="Number of Audio Samples to Compare: " + str(self.samples) + " repository Maximum Split Paramter: " + str(self.max_split) + " Word Length: " + str(self.samplelength ))
        self.label_result.pack()        
        self.text_result = tk.Text(self.group_result, height="20")
        self.text_result.configure(background='black', foreground='cyan')
        self.text_result.pack()
    
    # show file entry input box
    def show_file_entry(self):
        # GROUP ENTRY
        
        self.group_entry = tk.LabelFrame(self.group_enclosure, text="", padx=5, pady=5)
        self.group_entry.pack(padx=10, pady=10, side = 'bottom')
        
        
        self.label_file = tk.Label(self.group_entry, text="Query Filename")
        self.label_file.pack(padx=58)
        self.entry_file = tk.Entry(self.group_entry, bd =5, relief="flat")
        self.entry_file.pack()
        self.entry_file.insert(0, "voicequery.wav")
        self.label_db = tk.Label(self.group_entry, text="Path to repository")
        self.label_db.pack()
        self.entry_db = tk.Entry(self.group_entry, bd =5,  relief="flat")
        self.entry_db.insert(0, "db_voice")
        self.entry_db.pack()        
        
    # show search button below the file entry
    def show_buttons (self):
        root = self.root
        tk.Button(self.group_entry, padx=15, text="Search", command=self.on_button_click).pack()
        
    # on click event for the button
    def on_button_click(self):
        
        self.filename = self.entry_file.get()
        self.clear_canvas()
        if (os.path.isfile(self.filename)):  
            query_wavsound = wavsound(self.filename)            
            self.dbroot = self.entry_db.get()
            samples = self.samples
            partition = int(len(query_wavsound.get_data())/self.samplelength)
            max_split = self.max_split
            
            # repository query time
            start_time = time.time()        
            
            result_lst = run(self.filename, self.samplelength, samples, self.dbroot, max_split)
            
            # output
            output = "Search Result: \n" 
            
            # Tabulate % match (wav files with 0% match are excluded from the result)
            for pair in result_lst:
                    output += pair[0] + " : " + (40-len(pair[0]))*" " + pair[1] + "% match" + "\n"
                        
            # Show search time
            timelapse_parallel = time.time() - start_time   
            output = output + str(timelapse_parallel) + "seconds"            

            self.text_result.insert('1.0', output + "\n" )
            
            self.draw_wavform(query_wavsound.get_data(),"cyan","query")
            
            top_match_wavsoundfile = output.split()[2]
            print( output.split())
            print(top_match_wavsoundfile)
            top_match_wavsound = wavsound(top_match_wavsoundfile)      
            
            self.draw_wavform(top_match_wavsound.get_data(),"white","result")
            
    # quit application       
    def quit(self):
        self.root.destroy()
        
if __name__ == '__main__': 
    my_app = application()







