import os
import time
import pprint
import random
import re
import collections
from os.path import expanduser, join
import sys
import curses



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class ConfigManager:

    @staticmethod
    def read_config(file_name):
        
        task_index = None
        hint_index = None
        
        if not os.path.exists(file_name): 
            task_index = 0
            ConfigManager.write_config(file_name, task_index);
 
        else:
            task_index = next(open(file_name))
            
        return int(task_index)
    
    @staticmethod
    def write_config(file_name, task_index):
        file = open(file_name, 'w')
        file.write(str(task_index))
        file.close()


class Task:
    def __init__(self, message, hint, test_function):
        self.current_hint = 0
        self.message = message
        self.hint = hint
        self.test_function = test_function
    
    def test_solve(self, parameter):
        return(self.test_function(parameter))


class Spark:
    GRAVITY = 1.2
    
    def __init__(self, stdscr, color, x, y, z, xspeed, yspeed, zspeed):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.zspeed = zspeed
        self.stdscr = stdscr
        self.age = 0
    
    def iterate(self):
        self.yspeed += self.GRAVITY
        self.xspeed -= self.xspeed * 0.1
        self.x += self.xspeed
        self.y += self.yspeed
        self.age += 1

    def draw(self):
        xy = self.stdscr.getmaxyx()
    
        maxy = xy[0]
        maxx = xy[1]
        
        modifier = "x"
        char = "*"
        
        if self.age < 4:
           modifier = curses.A_BOLD
        elif self.age < 7:
            modifier = curses.A_NORMAL 
        else:
            modifier = curses.A_DIM
            
        if self.x > 0 and self.y > 0 and self.x < maxx and self.y < maxy and self.age < 12:
            self.stdscr.addstr(int(self.y), int(self.x), char, curses.color_pair(self.color) |  modifier)
        
        
class Firework:
    def __init__(self, stdscr, color, x, y):
        self.sparks = []
        self.color = color
        self.stdscr = stdscr
        for ind in range(0, random.randint(50, 80)):
            self.sparks.append(Spark(stdscr, color, x, y, 0, random.randint(-6,6), random.randint(-6,6),random.randint(-6,6) ))
            
    def draw(self):
        for spark in self.sparks:
            spark.draw()
            spark.iterate()
            

def print_fireworks():
    stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.curs_set(0)
    xy = stdscr.getmaxyx()
    
    x = xy[0]
    y = xy[1]
    print x
    print y
    selected_x = random.randint(0, x )
    selected_y = random.randint(0, y )
    
    fireworks = []
    fireworks.append(Firework(stdscr, 133, 100, 25))
    
    for v in range(0, 30):
        if v == 7:
            fireworks.append(Firework(stdscr, 5 ,25, 50))
        elif v == 17:
            fireworks.append(Firework(stdscr, 230,150, 0))
        elif v == 12:
            fireworks.append(Firework(stdscr, 200,40, 25))
        elif v == 22:
            fireworks.append(Firework(stdscr, 30,125, 40))
        os.system('clear')
        for fw in fireworks:
            fw.draw()
        stdscr.refresh()
        time.sleep(0.1)
    curses.endwin()

def homeDir():
    return

def directoryCreated(parameter):
    return os.path.isdir(os.path.join(expanduser("~"), "newdir"))

def findSecretFile(parameter):
    return parameter == "993"
    
def inCorrectDirectory(parameter):
    return os.getcwd() == os.path.join(expanduser("~"), "target") 

def cipherAnswer(parameter):
    if not parameter:
        print  bcolors.FAIL + "You need to provide the answer\n\n" + bcolors.ENDC
        return False
    return parameter.upper() == "MISTAKES" 

def fileCreatedAndEdited(parameter):
    target_file = os.path.join(expanduser("~"), "edit.txt");
    if not os.path.exists(target_file):
        return False
    first_line = next(open(target_file)).strip()
    print first_line
    return first_line == "Pandora"

def fileDeleted(parameter):
    return not os.path.exists(os.path.join(expanduser("~"), "edit.txt"))

def get_code():
    return """
    KVUKOV MHLZY GUAKWMVSN RLOO YVVK MHVA ESUA AFYLZT ALNMFYVN. MHVD'SV RSUZT. RLMH GUAKWMVSN DUW AFYV ALNMFYVN EFNMVS.

    -FBFA UNJUSZV

    AFYV OUMN UE ALNMFYVN
    """

def analyse_code():
    code = get_code()
    code = re.sub(r"\W", "", code)
    freqs = collections.Counter()
    for letter in code:
        if letter:
            freqs[letter] += 1
            
            
    print bcolors.OKGREEN + "In this code the letter frequencies are:\n\n" + bcolors.ENDC      
    for f in freqs.most_common():
        perc_freq = float( f[1]) / len(code)  * 100
        print f[0] + "   " + str( float("{0:.2f}".format(perc_freq) ) )


    print bcolors.OKGREEN + "\n\nIn English the average letter frequencies are:" + bcolors.ENDC  

    print """
    
E   12.51
T   9.25
A   8.04
O   7.60
I   7.26
N   7.09
S   6.54
R   6.12
H   5.49
L   4.14
D   3.99
C   3.06
U   2.71
M   2.53
F   2.30
P   2.00
G   1.96
W   1.92
Y   1.73
B   1.54
V   0.99
K   0.67
X   0.19
J   0.16
Q   0.11
Z   0.09

"""

def print_success():
    print bcolors.OKGREEN
    print """
YOU DID IT!!! Good work.

To claim your extra present the passphrase is 'Uncle Nick is the king of awesome'
    """
    print bcolors.ENDC
    
def pandoraArt():
    print bcolors.HEADER +  """
                                                                       
 _|_|_|                              _|                                
 _|    _|    _|_|_|  _|_|_|      _|_|_|    _|_|    _|  _|_|    _|_|_|  
 _|_|_|    _|    _|  _|    _|  _|    _|  _|    _|  _|_|      _|    _|  
 _|        _|    _|  _|    _|  _|    _|  _|    _|  _|        _|    _|  
 _|          _|_|_|  _|    _|    _|_|_|    _|_|    _|          _|_|_|  
                                                                       
                                                                       
            """ + bcolors.ENDC



def pandoraProgress(completed, total):
    print bcolors.OKBLUE + "\n\nYou have completed " + str(completed) + " of " + str(total) + " challenges\n"
    print "|" + bcolors.OKGREEN + "x" * completed + bcolors.WARNING + "=" * ( total - completed ) + bcolors.OKBLUE + "|\n\n" + bcolors.ENDC

class Pandora:
    def __init__(self):
        home = expanduser("~")
        self.home_directory = home
        self.config_file = os.path.join(home, ".pandora")
        self.task_index = ConfigManager.read_config(self.config_file)
        self.tasks = [
            Task(
                "You need to go to the directory: " + os.path.join(expanduser("~"), "target") + ". Type 'pandora submit' when you are in the right directory.", 
                "To find out what directory you are in type pwd. Use the 'cd' command to change directory. Google 'Linux change directory' - Google is your friend! :DDDD", 
                inCorrectDirectory),
            Task(
                "There is a hidden file in the " + os.path.join(expanduser("~"), "target")  + " directory.  It has 'secret' in the name followed by numbers.\n\n" +
                "Find the file and provide the numbers: pandora submit <numbers>", 
                "You need to find the right flag to provide to the 'ls' command to show hidden files.  Try typing 'man ls' or search on the internet.", 
                findSecretFile),
            Task(
                "You need to create a new directory.  The new directory should be called 'newdir' and it should be in your home directory(" + home + ").\n\nTo jump straight to your home directory you can type 'cd' without anything else.\n\nType 'pandora submit' when you have created it.",
                "The command to create a directory is mkdir.  Use 'man mkdir' or Google to find out how to use it.",
                directoryCreated
            ),
            Task(
                "You need to create a new file and edit it. Go to your home directory (just type 'cd').  Create and save a file called 'edit.txt' with just the word Pandora in it (make sure it starts with a capital!). Use the text editor nano to do it.\n\nType 'pandora submit' when you have created it.",
                "Use the command 'nano edit.txt' to start editing a new file",
                fileCreatedAndEdited
            ),
            Task(
                "Time to clean up after yourself and remove that file. Be careful!  We don't want to go deleting anything else by accident :D\n\nType 'pandora submit' when you have created it.",
                "Use the rm command followed by the name of the file you want to delete.  Just make sure it's the right one!",
                fileDeleted
            ),
            Task(
                "Nearly there! Time for something a bit different. You need to solve this code:\n\n" +  get_code() + "\n\nSolve the puzzle and find the 8th word. Type 'pandora submit <word>' when you have created it.",
                "This is a substitution cipher - pairs of letters have been swapped and you have to work out the key. You can do it by trial and error but a quicker was is to use the frequencies of letters to get started." +  
                "Type 'pandora code' to analyse the letter frequencies.",
                cipherAnswer
            )
        ]
        

pandora = Pandora()
os.system('clear')

current_task = pandora.tasks[pandora.task_index]

pandoraArt()

if len(sys.argv) == 1:
    print current_task.message + "\n\nFor a hint use 'pandora hint'."
else:
    command = sys.argv[1]
    submission = None
    if len(sys.argv) > 2:
        submission = sys.argv[2]
    if command == "hint":
        print current_task.message + "\n\n"
        print bcolors.WARNING + "HINT\n---------\n\n" + current_task.hint + bcolors.ENDC
    elif command == "submit":
        passed = current_task.test_solve(submission)
        if passed:
            pandora.task_index += 1
            if pandora.task_index < len(pandora.tasks):      
                print bcolors.OKGREEN + "Great work!  You did it :)  Time for a new challenge....\n\n" + bcolors.ENDC
                ConfigManager.write_config(pandora.config_file, pandora.task_index)
                current_task = pandora.tasks[pandora.task_index]
                print current_task.message + "\n\n" + current_task.hint
            else:
                print_fireworks()
                print_success()
        else:
            print bcolors.FAIL + " *** AFRAID NOT! TRY AGAIN! *** \n" + bcolors.ENDC
            print current_task.message + "\n\nFor a hint use 'pandora hint'."
    elif command == "code":
        analyse_code()
    else:
        print "Error: invalid option."

    
pandoraProgress(pandora.task_index, len(pandora.tasks))