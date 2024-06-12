###########################
# install module:         #
# pkg install mpv         #
# pip install python-mpv  #
###########################
# Coded By Your_Name      #
# This tool for play music#
# Free to recode	  #
# Free to change	  #
# Free for Anyone	  #
# Owned By Anyone	  #
###########################


# Mengimport/Memanggil module
import os
import subprocess
import colorama
from colorama import Fore, Back, Style

# Menyetel Tampilan
os.system("clear")
print(Style.BRIGHT, Fore.WHITE)
os.system("figlet SoundPlay")
print(Style.BRIGHT, Fore.YELLOW + "use: example:   " + Fore.WHITE + "  | " + Fore.YELLOW + "Sound: Hack.mp3")
print(Fore.BLUE, Back.WHITE + "Owned By Anyone " + Style.RESET_ALL, Style.BRIGHT, Fore.WHITE + "| " + Fore.YELLOW + "Sound: path/to/file/Hack.mp3")
print(Style.BRIGHT, Fore.WHITE + "                  | type : (exit) to exit")
print()

# Cara kerja play-sound
def play_music(file_path):
    try:
        # Jalankan pemutar sound di latar belakang menggunakan subprocess
        subprocess.Popen(["mpv", "--no-video", file_path])
        print(Fore.GREEN + f"Memutar: {file_path}")
    except Exception as e:
        print(Fore.RED + f"Gagal memutar musik: {e}")

if __name__ == "__main__":
    # Meminta input pengguna untuk jalur file sound
    music_file = input(Fore.BLUE + "Sound: " + Fore.WHITE)
    # membuat program keluar saat mengetik exit di input
    if music_file == "exit":
       os.system("clear")
       print("Thanks For View")
       print()
       quit()
    play_music(music_file)


###########################
#			  #
#			  #
#			  #
#			  #
#			  #
#			  #
###########################
         #       #
        #         #
       #############


########       #       ######### ######## #########
#	      # #      #	 #	  #
#	     #   #     #	 #        #
######	    #     #    ######### ######   #   #####
#	   #########	       # #	  #       #
#	  #         #          # #	  #       #
######## #           # ######### ######## #########





	     #  #   ##   # # #### #####
	     ####  ####  ##  ##     #
	     #  # #    # # # ####   #
